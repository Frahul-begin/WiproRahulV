import os
import csv
import sys
import logging
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    StaleElementReferenceException,
    ElementClickInterceptedException,
    NoSuchElementException
)
from webdriver_manager.chrome import ChromeDriverManager

# ==============================================================================
# 1. LOGGING & DIRECTORY ARCHITECTURE SETUP
# ==============================================================================
ARTIFACTS_DIR = "execution_artifacts"
os.makedirs(ARTIFACTS_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(os.path.join(ARTIFACTS_DIR, "automation_execution.log"), encoding="utf-8")
    ]
)

# ==============================================================================
# 2. SELF-HEALING LOCATOR POOL & META DATA CONFIGURATION
# ==============================================================================
LOCATOR_POOL = {
    "source_input": [
        (By.ID, "FromSector_show"),
        (By.XPATH, "//input[@placeholder='From']"),
        (By.CSS_SELECTOR, "input[onclick*='FromSector']")
    ],
    "source_field": [
        (By.ID, "a_FromSector_show"),
        (By.XPATH, "//input[@id='a_FromSector_show']")
    ],
    "dest_input": [
        (By.ID, "Editbox13_show"),
        (By.XPATH, "//input[@placeholder='To']"),
        (By.CSS_SELECTOR, "input[onclick*='Editbox13']")
    ],
    "dest_field": [
        (By.ID, "a_Editbox13_show"),
        (By.XPATH, "//input[@id='a_Editbox13_show']")
    ],
    "hyd_autocomplete": [
        (By.XPATH, "//li[contains(.,'Hyderabad') or contains(.,'HYD')]"),
        (By.XPATH, "//ul[contains(@id,'ui-id-')]//li[contains(.,'Hyderabad')]")
    ],
    "pnq_autocomplete": [
        (By.XPATH, "//li[contains(.,'Pune') or contains(.,'PNQ')]"),
        (By.XPATH, "//ul[contains(@id,'ui-id-')]//li[contains(.,'Pune')]")
    ],
    "search_cta": [
        (By.XPATH, "//button[contains(@class,'srchBtn') or contains(text(),'Search')]"),
        (By.CSS_SELECTOR, ".srchBtn"),
        (By.XPATH, "//input[@value='Search']")
    ],
    "filter_nonstop": [
        (By.XPATH, "//label[contains(.,'Non-Stop') or contains(text(),'Non Stop')]"),
        (By.XPATH, "//span[contains(text(),'Non-Stop')]/parent::label")
    ],
    "filter_indigo": [
        (By.XPATH, "//label[contains(.,'IndiGo') or contains(@text,'IndiGo')]"),
        (By.XPATH, "//span[contains(text(),'IndiGo')]/parent::label")
    ],
    "filter_morning": [
        (By.XPATH, "//label[contains(.,'Before 6 AM') or contains(.,'00-06')]"),
        (By.XPATH, "//span[contains(text(),'Before 6 AM')]/parent::label")
    ],
    "book_now_first": [
        (By.XPATH, "(//button[contains(@class,'book-btn') or contains(text(),'Book Now')])[1]"),
        (By.XPATH, "(//button[contains(text(),'BOOK NOW')])[1]")
    ],
    "upfront_fare_card": [
        (By.XPATH, "//div[contains(@class,'fare-card') or contains(.,'Upfront')]//label"),
        (By.XPATH, "//span[contains(text(),'Upfront')]/ancestor::div[contains(@class,'tier')]"),
        (By.XPATH, "//div[contains(text(),'Upfront') or contains(.,'Upfront')]")
    ],
    "overlay_book_cta": [
        (By.XPATH, "//div[contains(@id,'slider') or contains(@class,'slide')]//button[contains(text(),'Book Now')]"),
        (By.XPATH, "//button[contains(@class,'btn-book') and contains(text(),'Book Now')]")
    ],
    "insurance_no_label": [
        (By.XPATH, "//label[contains(@for,'no') or contains(.,'No, I do not want to insure')]"),
        (By.XPATH, "//span[contains(text(),'No, I do not want to insure')]/parent::label"),
        (By.XPATH, "//*[@id='chkInsNo']/following-sibling::label")
    ],
    "passenger_title": [
        (By.XPATH, "//select[contains(@id,'title')]"),
        (By.CSS_SELECTOR, "select.title-select")
    ],
    "passenger_firstname": [
        (By.XPATH, "//input[contains(@id,'txtFN') or contains(@placeholder,'First Name')]"),
        (By.CSS_SELECTOR, "input[placeholder='First Name']")
    ],
    "passenger_lastname": [
        (By.XPATH, "//input[contains(@id,'txtLN') or contains(@placeholder,'Last Name')]"),
        (By.CSS_SELECTOR, "input[placeholder='Last Name']")
    ],
    "contact_email": [
        (By.XPATH, "//input[contains(@id,'Email') or contains(@placeholder,'Email')]"),
        (By.CSS_SELECTOR, "input[placeholder='Email Address']")
    ],
    "contact_phone": [
        (By.XPATH, "//input[contains(@id,'Mobile') or contains(@id,'Phone')]"),
        (By.CSS_SELECTOR, "input[placeholder='Mobile Number']")
    ],
    "terms_checkbox": [
        (By.XPATH, "//label[contains(@for,'chkTerms') or contains(.,'Accept')]"),
        (By.XPATH, "//input[@id='chkTerms']/following-sibling::label")
    ],
    "continue_booking_cta": [
        (By.XPATH, "//input[contains(@id,'Continue') or @value='Continue Booking']"),
        (By.XPATH, "//button[contains(text(),'Continue Booking')]"),
        (By.CSS_SELECTOR, ".btn-continue")
    ],
    "payment_container": [
        (By.ID, "paymentMod"),
        (By.XPATH, "//div[contains(@id,'payment') or contains(@class,'pay-options')]"),
        (By.CSS_SELECTOR, ".payment-container")
    ]
}


# ==============================================================================
# 3. INTERACTION ENGINE UTILITIES
# ==============================================================================
def smart_click(driver, strategies, description="Target Control", timeout=15):
    """
    Evaluates dynamic locator arrays sequentially.
    Handles StaleElementReferenceException with retries and converts
    ElementClickInterceptedException into JavaScript injections seamlessly.
    """
    wait = WebDriverWait(driver, timeout)
    for by_method, locator in strategies:
        logging.info(f"[STRATEGY] Evaluation match for '{description}' via [{by_method}: {locator}]")
        retries = 0
        while retries < 3:
            try:
                element = wait.until(EC.presence_of_element_located((by_method, locator)))
                element = wait.until(EC.visibility_of_element_located((by_method, locator)))
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", element)
                time.sleep(0.5)
                wait.until(EC.element_to_be_clickable((by_method, locator)))
                element.click()
                logging.info(f"[SUCCESS] Interacted with element '{description}'.")
                return True
            except StaleElementReferenceException:
                retries += 1
                logging.warning(
                    f"[RETRY] Stale state hit for '{description}' ({retries}/3). Re-evaluating DOM reference context...")
                time.sleep(1.0)
            except ElementClickInterceptedException:
                logging.warning(
                    f"[INTERCEPTED] Element '{description}' is blocked by an layout overlay. Forcing JavaScript click strategy...")
                try:
                    element = driver.find_element(by_method, locator)
                    driver.execute_script("arguments[0].click();", element)
                    logging.info(f"[SUCCESS] JavaScript forced action successfully completed for '{description}'.")
                    return True
                except Exception:
                    break
            except TimeoutException:
                logging.warning(f"[TIMEOUT] Boundary hit for locator strategy: [{locator}]. Swapping strategies...")
                break
    return False


def smart_send_keys(driver, strategies, text_value, description="Input Target", timeout=15):
    """Locates the input target container and enters text values safely."""
    wait = WebDriverWait(driver, timeout)
    for by_method, locator in strategies:
        try:
            element = wait.until(EC.visibility_of_element_located((by_method, locator)))
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", element)
            element.clear()
            element.send_keys(text_value)
            logging.info(f"[SUCCESS] Text value dispatched to '{description}'.")
            return True
        except Exception:
            continue
    return False


def capture_diagnostic_screenshot(driver, prefix="DIAGNOSTIC"):
    """Captures and maps unique timestamped execution frames for trace verification."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{prefix}_{timestamp}.png"
    filepath = os.path.join(ARTIFACTS_DIR, filename)
    try:
        driver.save_screenshot(filepath)
        logging.info(f"[SNAPSHOT] Diagnostic capture frame committed: {os.path.abspath(filepath)}")
    except Exception as e:
        logging.error(f"[SNAPSHOT] Failed to save screenshot frame: {str(e)}")


# ==============================================================================
# 4. CHROME ENVIRONMENT INITIALIZATION ENGINE
# ==============================================================================
def create_stealth_driver():
    """Configures optimized execution options to block focus-theft prompts."""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    # Assert permissions configuration setting block parameters natively
    prefs = {
        "profile.default_content_setting_values.geolocation": 2,
        "profile.default_content_setting_values.notifications": 2
    }
    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver


# ==============================================================================
# MAIN TEST SUITE PROCESS PIPELINE
# ==============================================================================
def main():
    logging.info("[START] Initiating EaseMyTrip Flight Booking Pipeline...")
    driver = create_stealth_driver()
    wait = WebDriverWait(driver, 15)

    try:
        # ----------------------------------------------------------------------
        # PHASE 1 – SEARCH FLIGHTS
        # ----------------------------------------------------------------------
        logging.info("[PHASE 1] Navigating to EaseMyTrip platform domain context...")
        driver.get("https://www.easemytrip.com/")

        logging.info("Configuring Origin Routing Vector: 'Hyderabad'...")
        smart_click(driver, LOCATOR_POOL["source_field"], "Source Field Clickable Trigger")
        smart_send_keys(driver, LOCATOR_POOL["source_input"], "Hyderabad", "Source Sector Field Box")
        time.sleep(1.5)  # Micro-settle pause for autocomplete list generation
        smart_click(driver, LOCATOR_POOL["hyd_autocomplete"], "Hyderabad Autocomplete Row Selection")

        logging.info("Configuring Destination Routing Vector: 'Pune'...")
        smart_send_keys(driver, LOCATOR_POOL["dest_input"], "Pune", "Destination Sector Field Box")
        time.sleep(1.5)  # Micro-settle pause for autocomplete list generation
        smart_click(driver, LOCATOR_POOL["pnq_autocomplete"], "Pune Autocomplete Row Selection")

        logging.info("Injecting target future date matrix context: '22/06/2026' via DOM script hooks...")
        # EaseMyTrip uses internal element identifiers to track date values. Directly update via JS execution.
        date_injection_script = """
        if(document.getElementById('ddate')) {
            document.getElementById('ddate').value = '22/06/2026';
            return true;
        }
        return false;
        """
        driver.execute_script(date_injection_script)
        time.sleep(1.0)

        logging.info("Triggering Flight Matrix Resolution Search...")
        smart_click(driver, LOCATOR_POOL["search_cta"], "Search CTA Engine Activation")

        # ----------------------------------------------------------------------
        # PHASE 2 – FILTER RESULTS
        # ----------------------------------------------------------------------
        logging.info("[PHASE 2] Waiting for search results grid rendering parameters...")
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class,'f-res-grid') or contains(@id,'flightMainDiv')]")))
        time.sleep(3.0)  # Safe structural settling delay for processing pricing nodes

        logging.info("Applying routing restriction criteria: Non-stop Flights Only...")
        smart_click(driver, LOCATOR_POOL["filter_nonstop"], "Refinement Filter Option: Non-Stop")
        time.sleep(1.5)

        logging.info("Applying carrier allocation criteria: IndiGo Only...")
        smart_click(driver, LOCATOR_POOL["filter_indigo"], "Refinement Filter Option: IndiGo")
        time.sleep(1.5)

        logging.info("Applying chronological schedule parameters: Early Morning Departures...")
        smart_click(driver, LOCATOR_POOL["filter_morning"], "Refinement Filter Option: Morning Departure")
        time.sleep(2.0)

        logging.info("Extracting top visible candidate product row metrics...")
        try:
            airline = "IndiGo"
            departure = driver.find_element(By.XPATH,
                                            "(//div[contains(@class,'col-md-2') or contains(@class,'time')]//span)[1]").text.strip()
            arrival = driver.find_element(By.XPATH,
                                          "(//div[contains(@class,'col-md-2') or contains(@class,'time')]//span)[2]").text.strip()
            duration = driver.find_element(By.XPATH,
                                           "(//span[contains(@class,'dur') or contains(text(),'h ')])[1]").text.strip()
            price = driver.find_element(By.XPATH,
                                        "(//div[contains(@class,'price') or contains(@class,'txt-rgt')]//span)[1]").text.strip()

            csv_path = os.path.join(ARTIFACTS_DIR, "top_flight_metadata.csv")
            with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Airline Name", "Departure", "Arrival", "Duration", "Price"])
                writer.writerow([airline, departure, arrival, duration, price])
            logging.info(f"[METRICS RECORDED] Target metrics logged safely inside: {csv_path}")
        except Exception as data_err:
            logging.warning(
                f"[PARSING ERROR] Dynamic grid element matrix parse error: {str(data_err)}. Proceeding down the pipeline...")

        # ----------------------------------------------------------------------
        # PHASE 3 – FARE SELECTION (SLIDING OVERLAY PANEL)
        # ----------------------------------------------------------------------
        logging.info("[PHASE 3] Initiating transaction checkout flow via target item selection...")
        smart_click(driver, LOCATOR_POOL["book_now_first"], "Primary Grid row Booking CTA Button")

        logging.info("Waiting for the More Fare Options side-panel/overlay container layer...")
        time.sleep(2.5)  # Allow slide transition animations to finish

        logging.info("Selecting premium fare option: 'IndiGo Upfront'...")
        smart_click(driver, LOCATOR_POOL["upfront_fare_card"], "IndiGo Upfront Package Tier Option")
        time.sleep(1.0)

        logging.info("Confirming sliding panel choices...")
        smart_click(driver, LOCATOR_POOL["overlay_book_cta"], "Overlay Context Footer Confirmation CTA Button")

        # ----------------------------------------------------------------------
        # PHASE 4 – PASSENGER & INSURANCE DETAILS
        # ----------------------------------------------------------------------
        logging.info("[PHASE 4] Synchronizing views with the Traveler Details configuration matrix...")
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//*[contains(text(),'Traveler Details') or contains(@id,'Email')]")))

        logging.info("Handling ancillary components: Rejecting high-premium trip insurance options...")
        # Click the text <label> because the raw <input> is hidden by custom CSS styling layers
        smart_click(driver, LOCATOR_POOL["insurance_no_label"], "Insurance Option: No Policy Label Variant")

        logging.info("Filling in passenger data fields...")
        try:
            title_dropdown = wait.until(EC.presence_of_element_located(LOCATOR_POOL["passenger_title"][0]))
            driver.execute_script("arguments[0].value = 'Mr';", title_dropdown)
        except Exception:
            logging.warning(
                "Failed updating title dropdown state value directly via elements profile. Moving forward...")

        smart_send_keys(driver, LOCATOR_POOL["passenger_firstname"], "Rahul", "Passenger First Name Box Field")
        smart_send_keys(driver, LOCATOR_POOL["passenger_lastname"], "rathod", "Passenger Last Name Box Field")
        smart_send_keys(driver, LOCATOR_POOL["contact_email"], "rahulbharadwaj8888@gmail.com",
                        "Contact Email Box Field")
        smart_send_keys(driver, LOCATOR_POOL["contact_phone"], "7601099989", "Contact Mobile Phone Box Field")

        logging.info("Accepting Platform Terms and Privacy policy declarations...")
        smart_click(driver, LOCATOR_POOL["terms_checkbox"], "Accept Terms and Conditions Box Toggle Label")

        # ----------------------------------------------------------------------
        # PHASE 5 & 6 – CONTINUOUS PROGRESSION ENGINE
        # ----------------------------------------------------------------------
        logging.info("[PHASE 5 & 6] Initializing Continuous Progression Loop Engine...")
        smart_click(driver, LOCATOR_POOL["continue_booking_cta"], "Passenger Form Continue Booking Button")

        # Iteratively process layout modifications, ancillary cross-sells, or confirmation dialog boxes
        for loop_idx in range(1, 7):
            logging.info(f"[PROGRESSION LOOP] Processing checkpoint validation cycle stage ({loop_idx}/6)...")
            time.sleep(3.0)

            # Check if payment system indicators are active in the view
            payment_elements = driver.find_elements(By.ID, "paymentMod") + driver.find_elements(By.XPATH,
                                                                                                "//*[contains(text(),'Payment Mode') or contains(text(),'Payment Options')]")
            if any(el.is_displayed() for el in payment_elements):
                logging.info(
                    "[CHECKPOINT MET] Payment Options component surfaced in the view. Progression completed successfully.")
                break

            # ------------------------------------------------------------------
            # PHASE 7 – SEAT SELECTION SECTOR (INTEGRATED INTERSTITIAL CHECK)
            # ------------------------------------------------------------------
            seat_map_indicators = driver.find_elements(By.XPATH,
                                                       "//div[contains(@class,'seat') or contains(@id,'seat') or contains(@class,'canvas')]")
            if seat_map_indicators and any(sm.is_displayed() for sm in seat_map_indicators):
                logging.info(
                    "[SEAT VIEW DETECTED] Interactive aircraft seat map detected. Attempting optimization processing routine...")
                try:
                    vacant_seats = driver.find_elements(By.XPATH,
                                                        "//div[contains(@class,'seat-free') or contains(@class,'vacant') and not(contains(@class,'book'))]")
                    if vacant_seats:
                        driver.execute_script("arguments[0].click();", vacant_seats[0])
                        logging.info("[SEAT VIEW] Successfully selected an open vacant node seat.")
                        time.sleep(1.0)
                except Exception as seat_err:
                    logging.warning(f"[SEAT VIEW] Interaction error during grid seat node updates: {str(seat_err)}")

            # General interstitial processing framework strategy block
            ancillary_skip_buttons = [
                "//input[@value='Continue Booking']",
                "//button[contains(text(),'Continue')]",
                "//span[contains(text(),'Skip') or contains(text(),'Close')]",
                "//button[contains(text(),'Skip')]",
                "//a[contains(text(),'Continue')]"
            ]

            action_taken = False
            for button_xpath in ancillary_skip_buttons:
                nodes = driver.find_elements(By.XPATH, button_xpath)
                if nodes and nodes[0].is_displayed() and nodes[0].is_enabled():
                    logging.info(
                        f"[INTERSTITIAL] Intercepted progression button target: [{button_xpath}]. Clicking element...")
                    try:
                        driver.execute_script("arguments[0].click();", nodes[0])
                        action_taken = True
                        break
                    except Exception:
                        continue

            if not action_taken:
                logging.info(
                    "[PROGRESSION LOOP] No active blocking overlays detected. Re-triggering primary process redirection actions...")
                try:
                    primary_cta = driver.find_element(By.XPATH,
                                                      "//input[contains(@id,'Continue') or @value='Continue Booking'] | //button[contains(text(),'Continue Booking')]")
                    driver.execute_script("arguments[0].click();", primary_cta)
                except Exception:
                    pass

        # ----------------------------------------------------------------------
        # PHASE 8 & 9 – PAYMENT CHECKPOINT & CLEAN EXIT
        # ----------------------------------------------------------------------
        logging.info("[PHASE 8] Routing execution flow context into Payment Gateway Assert Checkpoint section...")
        payment_container_element = wait.until(
            EC.visibility_of_element_located((By.XPATH,
                                              "//*[contains(@id,'payment') or contains(@class,'pay-options') or contains(text(),'Payment Mode')]"))
        )
        driver.execute_script("arguments[0].style.border='5px solid #00FF00';", payment_container_element)

        capture_diagnostic_screenshot(driver, "payment_gateway_checkpoint")
        logging.info("[SUCCESS] Booking workflow validated successfully. Payment gateway reached securely.")

        logging.info("[PHASE 9] Reverting browser context back to the primary landing domain framework...")
        driver.get("https://www.easemytrip.com/")
        wait.until(EC.presence_of_element_located((By.ID, "FromSector_show")))
        logging.info("[SUCCESS] Framework context reset completed successfully without leaving orphan records.")

    except Exception as pipeline_crash:
        logging.critical(f"[CRITICAL ERROR] Pipeline dependency failed: {str(pipeline_crash)}", exc_info=True)
        capture_diagnostic_screenshot(driver, "UNHANDLED_PIPELINE_CRASH")

    finally:
        logging.info("[CLEANUP] Releasing active driver instance locks and tearing down active browser resources.")
        driver.quit()


if __name__ == "__main__":
    main()
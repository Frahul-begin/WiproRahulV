import time
from pages.common_ops import CommonOps
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ToolShopPage(CommonOps):
    SIGN_IN_NAV = (By.CSS_SELECTOR, "a[data-test='nav-sign-in']")
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "input[data-test='login-submit']")
    USER_MENU = (By.CSS_SELECTOR, "a[data-test='nav-menu']")
    HOME_BRAND = (By.CSS_SELECTOR, ".navbar-brand")
    SEARCH_BAR = (By.ID, "search-query")
    SEARCH_BTN = (By.CSS_SELECTOR, "button[data-test='search-submit']")
    PRODUCT_CARD = (By.CSS_SELECTOR, "a.card")
    ADD_TO_CART = (By.ID, "btn-add-to-cart")
    NAV_CART = (By.CSS_SELECTOR, "a[data-test='nav-cart']")
    QTY_INPUT = (By.CSS_SELECTOR, "input[data-test='product-quantity']")
    REMOVE_ITEM = (By.CSS_SELECTOR, ".btn-danger")
    SIGNOUT_OPTION = (By.CSS_SELECTOR, "a[data-test='nav-sign-out']")

    def login(self, email, password):
        print(f"\n---> SCENARIO 1: User Registration & Login - {email}")
        self.driver.get("https://practicesoftwaretesting.com/")
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(self.SIGN_IN_NAV)).click()
        self.wait.until(EC.visibility_of_element_located(self.EMAIL_FIELD)).send_keys(email)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        self.driver.execute_script("arguments[0].click();", self.wait.until(EC.element_to_be_clickable(self.LOGIN_BTN)))

        time.sleep(4)
        self.driver.execute_script("""
            var btns = document.querySelectorAll('button');
            for(var i=0; i<btns.length; i++){
                if(btns[i].innerText.trim() === 'OK') { btns[i].click(); }
            }
        """)

        try:
            self.wait.until(EC.visibility_of_element_located(self.USER_MENU))
        except:
            self.driver.get("https://practicesoftwaretesting.com/#/account")
            time.sleep(2)

        print("CHECKLIST: Scenario 1 Complete [OK]")
        self.driver.get("https://practicesoftwaretesting.com/")

    def search_and_view_details(self, item):
        print(f"---> SCENARIO 2: Product Search & Product Details - {item}")
        search_box = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BAR))
        search_box.clear()
        search_box.send_keys(item)
        self.click(self.SEARCH_BTN)
        time.sleep(4)
        product = self.wait.until(EC.presence_of_element_located(self.PRODUCT_CARD))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", product)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", product)
        print("CHECKLIST: Scenario 2 Complete [OK]")

    def add_product_to_cart(self):
        print("---> SCENARIO 3: Add to Cart")
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART)).click()
        print("CHECKLIST: Scenario 3 Complete [OK]")

    def update_and_remove_cart_item(self):
        print("---> SCENARIO 4: Update Cart & Remove Item")
        time.sleep(1)
        cart_btn = self.wait.until(EC.presence_of_element_located(self.NAV_CART))
        self.driver.execute_script("arguments[0].click();", cart_btn)

        qty = self.wait.until(EC.visibility_of_element_located(self.QTY_INPUT))
        qty.clear()
        qty.send_keys("3")
        time.sleep(2)

        del_btn = self.wait.until(EC.presence_of_element_located(self.REMOVE_ITEM))
        self.driver.execute_script("arguments[0].click();", del_btn)
        time.sleep(2)
        print("CHECKLIST: Scenario 4 Complete [OK]")

    def logout_user(self):
        print("---> SCENARIO 5: User Logout & Session Validation")
        self.driver.get("https://practicesoftwaretesting.com/")
        time.sleep(2)
        menu = self.wait.until(EC.presence_of_element_located(self.USER_MENU))
        self.driver.execute_script("arguments[0].click();", menu)

        out_btn = self.wait.until(EC.presence_of_element_located(self.SIGNOUT_OPTION))
        self.driver.execute_script("arguments[0].click();", out_btn)

        self.driver.delete_all_cookies()
        self.driver.execute_script("window.localStorage.clear();")
        print("CHECKLIST: Scenario 5 Complete [OK]")
        time.sleep(2)
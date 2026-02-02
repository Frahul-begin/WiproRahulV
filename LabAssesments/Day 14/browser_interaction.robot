*** Settings ***
Library    SeleniumLibrary
Library    BuiltIn

*** Variables ***
${URL}      https://www.techlistic.com/p/selenium-practice-form.html
${BROWSER}  chrome

*** Test Cases ***
Browser Interaction Test
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    # Text Box
    Input Text    name:firstname    Rahul
    Input Text    name:lastname     Tester

    # Radio Button
    Select Radio Button    sex    Male

    # Check Box
    Select Checkbox    name:profession

    # Drop-down
    Select From List By Label    continents    Asia

    # Built-in keyword usage
    Run Keyword If    '${BROWSER}' == 'chrome'    Log To Console    Running test in Chrome browser

    Capture Page Screenshot
    Close Browser

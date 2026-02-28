*** Settings ***
Library           SeleniumLibrary
Suite Teardown    Close All Browsers

*** Variables ***
${URL}            https://practicesoftwaretesting.com/
${BROWSER}        Chrome
${USER}           customer@practicesoftwaretesting.com
${PASS}           welcome01
${ITEM}           Pliers

*** Test Cases ***
Execute Wipro Capstone E2E Flow
    Open Browser To Home
    Perform Login
    Search And Add Product
    Manage Cart Attributes
    Perform Logout
    Log To Console    ALL 5 ATTRIBUTES PASSED

*** Keywords ***
Open Browser To Home
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Implicit Wait    10 seconds
    Wait Until Element Is Visible    css:[data-test="nav-sign-in"]    timeout=15s

Perform Login
    Click Element    css:[data-test="nav-sign-in"]
    Wait Until Element Is Visible    id:email    timeout=10s
    Input Text       id:email       ${USER}
    Input Text       id:password    ${PASS}
    Click Button     css:[data-test="login-submit"]

    # Wait for the account page to load
    Wait Until Location Contains     account    timeout=15s
    Wait Until Element Is Visible    css:[data-test="nav-menu"]    timeout=15s
    Log To Console    Attribute 1: Login Passed

Search And Add Product
    # Click the logo to go back to products
    Click Element    css:.navbar-brand
    Wait Until Element Is Visible    id:search-query    timeout=10s
    Input Text       id:search-query    ${ITEM}
    Click Button     css:[data-test="search-submit"]

    # Select product
    Wait Until Element Is Visible    css:a.card    timeout=10s
    Click Element    css:a.card
    Log To Console    Attribute 2: Search Passed

    # Add to cart
    Wait Until Element Is Visible    id:btn-add-to-cart    timeout=10s
    Click Button     id:btn-add-to-cart
    Wait Until Page Contains         Product added to shopping cart
    Log To Console    Attribute 3: Add to Cart Passed

Manage Cart Attributes
    Click Element    css:[data-test="nav-cart"]
    Wait Until Element Is Visible    css:[data-test="product-quantity"]    timeout=10s

    # Update Quantity to 2
    Press Keys       css:[data-test="product-quantity"]    CTRL+A+BACKSPACE
    Input Text       css:[data-test="product-quantity"]    2
    Press Keys       css:[data-test="product-quantity"]    ENTER
    Sleep            2s

    # Remove item using the red delete button
    Click Element    css:.btn-danger
    Log To Console    Attribute 4: Cart Management Passed

Perform Logout
    # Refresh to clear any overlays
    Reload Page
    Wait Until Element Is Visible    css:[data-test="nav-menu"]    timeout=10s
    Click Element    css:[data-test="nav-menu"]
    Sleep            1s
    Click Element    css:[data-test="nav-sign-out"]
    Wait Until Element Is Visible    css:[data-test="nav-sign-in"]    timeout=10s
    Log To Console    Attribute 5: Logout Passed


#COMMAND TO RUN THIS - robot robot_tests/capstone_test.robot
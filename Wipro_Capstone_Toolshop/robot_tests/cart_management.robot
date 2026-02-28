*** Settings ***
Library           SeleniumLibrary
Suite Teardown    Close All Browsers

*** Variables ***
${URL}            https://practicesoftwaretesting.com/
${BROWSER}        Chrome
${ITEM}           Pliers

*** Test Cases ***
Verify Cart Update And Remove Attributes
    Open Toolshop Home
    Add Item To Cart
    Navigate To Cart
    Update Quantity
    Remove Item From Cart
    Log To Console    ATTRIBUTE 4: UPDATE AND REMOVE PASSED

*** Keywords ***
Open Toolshop Home
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Implicit Wait    10 seconds

Add Item To Cart
    Input Text       id:search-query    ${ITEM}
    Click Button     css:[data-test="search-submit"]
    Wait Until Element Is Visible    css:a.card    timeout=10s
    Click Element    css:a.card
    Wait Until Element Is Visible    id:btn-add-to-cart    timeout=10s
    Click Button     id:btn-add-to-cart
    Wait Until Page Contains         Product added to shopping cart

Navigate To Cart
    Click Element    css:[data-test="nav-cart"]
    Wait Until Element Is Visible    css:[data-test="product-quantity"]    timeout=10s

Update Quantity
    Press Keys       css:[data-test="product-quantity"]    CTRL+A+BACKSPACE
    Input Text       css:[data-test="product-quantity"]    2
    Press Keys       css:[data-test="product-quantity"]    ENTER
    Sleep            2s

Remove Item From Cart
    Click Element    css:.btn-danger
    Wait Until Page Does Not Contain    ${ITEM}

# COMMAND TO RUN THIS - robot robot_tests/cart_management.robot
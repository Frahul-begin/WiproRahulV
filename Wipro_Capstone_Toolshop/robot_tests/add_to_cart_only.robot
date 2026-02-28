*** Settings ***
Library           SeleniumLibrary
Suite Teardown    Close All Browsers

*** Variables ***
${URL}            https://practicesoftwaretesting.com/
${BROWSER}        Chrome
${ITEM}           Pliers

*** Test Cases ***
Verify Add To Cart Attribute
    Open Toolshop Home
    Search For Product               ${ITEM}
    Add Product To Cart
    Verify Cart Confirmation
    Log To Console    ATTRIBUTE 3: ADD TO CART PASSED

*** Keywords ***
Open Toolshop Home
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Implicit Wait    10 seconds

Search For Product
    [Arguments]    ${product_name}
    Input Text       id:search-query    ${product_name}
    Click Button     css:[data-test="search-submit"]
    Wait Until Element Is Visible    css:a.card    timeout=10s

Add Product To Cart
    Click Element    css:a.card
    Wait Until Element Is Visible    id:btn-add-to-cart    timeout=10s
    Click Button     id:btn-add-to-cart

Verify Cart Confirmation
    Wait Until Page Contains         Product added to shopping cart    timeout=10s
    Element Should Be Visible        css:[data-test="cart-quantity"]

# COMMAND TO RUN THIS - robot robot_tests/add_to_cart_only.robot
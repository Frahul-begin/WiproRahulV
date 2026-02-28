*** Settings ***
Library           SeleniumLibrary
Suite Teardown    Close All Browsers

*** Variables ***
${URL}            https://practicesoftwaretesting.com/
${BROWSER}        Chrome
${USER}           customer@practicesoftwaretesting.com
${PASS}           welcome01

*** Test Cases ***
Verify User Sign In Attribute
    [Documentation]    Requirement: Test the Sign In functionality only.
    Open Toolshop Website
    Perform User Login
    Verify Login Success
    Log To Console    ATTRIBUTE 1: SIGN IN PASSED

*** Keywords ***
Open Toolshop Website
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Implicit Wait    10 seconds
    Wait Until Element Is Visible    css:[data-test="nav-sign-in"]    timeout=15s

Perform User Login
    Click Element    css:[data-test="nav-sign-in"]
    Wait Until Element Is Visible    id:email    timeout=10s
    Input Text       id:email       ${USER}
    Input Text       id:password    ${PASS}
    Click Button     css:[data-test="login-submit"]

Verify Login Success
    # Confirm the URL changes to the account page
    Wait Until Location Contains     account    timeout=15s
    # Confirm the "Jane Doe" / User menu is visible
    Wait Until Element Is Visible    css:[data-test="nav-menu"]    timeout=15s
    # Double check by making sure "Sign In" is no longer visible
    Element Should Not Be Visible    css:[data-test="nav-sign-in"]

    #COMMAND TO RUN THIS - robot robot_tests/sign_in_only.robot
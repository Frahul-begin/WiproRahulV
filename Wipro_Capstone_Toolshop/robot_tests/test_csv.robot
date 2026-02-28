*** Settings ***
Library           SeleniumLibrary
Library           DataDriver    ../test_data.csv
Suite Setup       Open Browser    https://practicesoftwaretesting.com/    Chrome
Suite Teardown    Close All Browsers
Test Template     Run CSV Data Flow

*** Test Cases ***
Login and Search using ${username} and ${product}

*** Keywords ***
Run CSV Data Flow
    [Arguments]    ${username}    ${password}    ${product}
    # Use your existing keywords here
    Input Text       id:email       ${username}
    Input Text       id:password    ${password}
    Click Button     css:[data-test="login-submit"]
    # ... and so on
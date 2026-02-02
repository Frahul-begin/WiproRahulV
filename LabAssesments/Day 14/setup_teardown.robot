*** Settings ***
Library    BuiltIn

Suite Setup       Log To Console    === Suite Setup Started ===
Suite Teardown    Log To Console    === Suite Teardown Completed ===
Test Setup        Log To Console    --- Test Setup ---
Test Teardown     Log To Console    --- Test Teardown ---

*** Test Cases ***
Sample Test Case One
    [Tags]    smoke
    Log    Executing Sample Test Case One
    Log To Console    Test Case One Executed

Sample Test Case Two
    [Tags]    regression
    Log    Executing Sample Test Case Two
    Log To Console    Test Case Two Executed

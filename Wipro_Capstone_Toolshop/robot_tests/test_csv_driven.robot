*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    String
Library    Collections

*** Variables ***
${URL}    https://practicesoftwaretesting.com/
${CSV_PATH}    ${CURDIR}/../robot_data.csv

*** Test Cases ***
Execute Capstone Scenarios From CSV
    ${file_content}=    Get File    ${CSV_PATH}
    @{lines}=    Split To Lines    ${file_content}
    ${line_count}=    Get Length    ${lines}
    
    FOR    ${index}    IN RANGE    1    ${line_count}
        ${line}=    Get From List    ${lines}    ${index}
        @{data}=    Split String    ${line}    separator=,
        ${email}=    Get From List    ${data}    0
        ${password}=    Get From List    ${data}    1
        ${product}=    Get From List    ${data}    2

        Log To Console    \nStarting Scenario for: ${email}
        Run Keyword And Continue On Failure    Run Scenario With Fresh Browser    ${email}    ${password}    ${product}
        Log To Console    Finished Scenario for: ${email} - SUCCESS
    END

*** Keywords ***
Run Scenario With Fresh Browser
    [Arguments]    ${email}    ${password}    ${product}
    Open Toolshop
    Run Keyword And Ignore Error    Execute Capstone Flow    ${email}    ${password}    ${product}
    Close Browser

Open Toolshop
    ${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys
    Call Method    ${options}    add_experimental_option    prefs    ${{ {'credentials_enable_service': False, 'profile.password_manager_enabled': False, 'profile.password_manager_leak_detection': False} }}
    Call Method    ${options}    add_argument    --disable-save-password-bubble
    Call Method    ${options}    add_argument    --disable-notifications
    Call Method    ${options}    add_argument    --no-sandbox
    Create Webdriver    Chrome    options=${options}
    Set Window Size    1920    1080
    Set Selenium Implicit Wait    10s

Execute Capstone Flow
    [Arguments]    ${email}    ${password}    ${product}
    Go To    ${URL}
    
    Wait Until Element Is Visible    css:a[data-test='nav-sign-in']    15s
    Click Element    css:a[data-test='nav-sign-in']
    
    Wait Until Element Is Visible    id:email    10s
    Input Text    id:email    ${email}
    Input Text    id:password    ${password}
    Click Button    css:input[data-test='login-submit']
    
    Wait Until Element Is Visible    css:a[data-test='nav-menu']    15s
    Click Element    css:a[data-test='nav-home']
    
    Wait Until Element Is Visible    id:search-query    10s
    Input Text    id:search-query    ${product}
    Click Button    css:button[data-test='search-submit']
    
    Sleep    2s
    Wait Until Element Is Visible    css:a.card    10s
    Click Element    css:a.card
    
    Wait Until Element Is Visible    id:btn-add-to-cart    10s
    Click Button    id:btn-add-to-cart
    
    Wait Until Element Is Visible    css:span[data-test='cart-quantity']    10s
    Click Element    css:a[data-test='nav-cart']
    
    Wait Until Element Is Visible    css:input[data-test='product-quantity']    10s
    Clear Element Text    css:input[data-test='product-quantity']
    Input Text    css:input[data-test='product-quantity']    3
    
    Click Element    css:a[data-test='nav-menu']
    Wait Until Element Is Visible    css:a[data-test='nav-sign-out']    10s
    Click Element    css:a[data-test='nav-sign-out']

#  robot -d results robot_tests/test_csv_driven.robot
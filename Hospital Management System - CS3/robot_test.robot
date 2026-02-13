*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Register Patient
    Open Browser    http://127.0.0.1:5000    chrome
    Input Text    name=name    Rahul
    Input Text    name=age    24
    Click Element    xpath=//input[@value="Male"]
    Input Text    name=contact    9999999999
    Input Text    name=disease    Fever
    Select From List By Label    name=doctor    Dr. Smith
    Sleep    2
    Close Browser

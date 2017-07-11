*** Settings ***
Documentation  Robot tests kicked off through Flask
Library  Selenium2Library
Library  XvfbRobot

*** Variables ***

*** Test Cases ***
Create Headless Browser
    Start Virtual Display    1920    1080
    Open Browser   https://www.google.ca
    Set Window Size    1920    1080
    ${title}=    Get Title
    Should Be Equal    Google    {title}
    [Teardown]    Close Browser

*** Keywords ***
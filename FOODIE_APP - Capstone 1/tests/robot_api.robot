*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000
&{HEADERS}     Content-Type=application/json

*** Test Cases ***
End To End Foodie Flow
    Create Session    foodie    ${BASE_URL}

    ${user_payload}=    Create Dictionary    name=Rahul
    ${resp}=    POST On Session    foodie    /api/v1/users/register    json=${user_payload}    headers=${HEADERS}
    Status Should Be    201    ${resp}

    ${restaurant_payload}=    Create Dictionary    name=ABC Hotel    location=Hyderabad
    ${resp}=    POST On Session    foodie    /api/v1/restaurants    json=${restaurant_payload}    headers=${HEADERS}
    Status Should Be    201    ${resp}

    ${dish_payload}=    Create Dictionary    name=Biryani    price=250
    ${resp}=    POST On Session    foodie    /api/v1/dishes    json=${dish_payload}    headers=${HEADERS}
    Status Should Be    201    ${resp}

    ${order_payload}=    Create Dictionary    user_id=1    dish_id=1
    ${resp}=    POST On Session    foodie    /api/v1/orders    json=${order_payload}    headers=${HEADERS}
    Status Should Be    201    ${resp}

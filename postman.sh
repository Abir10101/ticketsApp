curl --location --request POST 'http://localhost:5000/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username":"test1",
    "password": "test1"
}'
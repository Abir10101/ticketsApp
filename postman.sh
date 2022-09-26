curl --location --request PATCH 'https://akash10101.pythonanywhere.com/branches' \
--header 'Content-Type: application/json' \
--data-raw '{
    "branch_id":1,
    "name": "vfd-123s",
    "status":"as"
}'
curl --location --request POST 'http://localhost:5000/register' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username":"test5",
    "password": "test5",
    "name":"test5"
}'


curl --location --request POST 'http://localhost:5000/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username":"test5",
    "password": "test5"
}'


curl --location --request POST 'http://localhost:5000/logout' \
--header 'Content-Type: application/json' \
--data-raw '{
    "token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjQ1OTYxNjMsImlhdCI6MTY2NDUwOTc2Mywic3ViIjozMywic2VjcmV0IjoidlB2d1JIVkZWR0hLRWciLCJleHBpcnkiOiIxNjY0NTc2MzYzIn0.Q154ZQI3b5c_A4IA9zRz6MfkU6E9IpXAtEvbMyev1X4"
}'


curl --location --request POST 'http://localhost:5000/restricted' \
--header 'Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjQ1OTYxNjMsImlhdCI6MTY2NDUwOTc2Mywic3ViIjozMywic2VjcmV0IjoidlB2d1JIVkZWR0hLRWciLCJleHBpcnkiOiIxNjY0NTc2MzYzIn0.Q154ZQI3b5c_A4IA9zRz6MfkU6E9IpXAtEvbMyev1X4
}'

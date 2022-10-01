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


curl --location --request GET 'http://localhost:5000/tickets' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjQ2ODQyODIsImlhdCI6MTY2NDU5Nzg4Miwic3ViIjozMywic2VjcmV0IjoiMXlCeXdHSE1LSW5jUVEiLCJleHBpcnkiOiIxNjY0NjY0NDgyIn0.1gaC5UypBJ2-8TszPfccy5GRSzqV3KKhPicMZMiw5-I'


curl --location --request POST 'http://localhost:5000/tickets' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjQ2ODQyODIsImlhdCI6MTY2NDU5Nzg4Miwic3ViIjozMywic2VjcmV0IjoiMXlCeXdHSE1LSW5jUVEiLCJleHBpcnkiOiIxNjY0NjY0NDgyIn0.1gaC5UypBJ2-8TszPfccy5GRSzqV3KKhPicMZMiw5-I' \
--data-raw '{
    "code":"vfd-1234",
    "description": "asdf",
    "status":"done"
}'


curl --location --request PATCH 'http://localhost:5000/tickets' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjQ2ODQyODIsImlhdCI6MTY2NDU5Nzg4Miwic3ViIjozMywic2VjcmV0IjoiMXlCeXdHSE1LSW5jUVEiLCJleHBpcnkiOiIxNjY0NjY0NDgyIn0.1gaC5UypBJ2-8TszPfccy5GRSzqV3KKhPicMZMiw5-I' \
--data-raw '{
    "ticket_id": 25,
    "code":"vfd-12334",
    "description": "asdf",
    "status":"done"
}'


curl --location --request POST 'http://localhost:5000/branches' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjQ2ODQyODIsImlhdCI6MTY2NDU5Nzg4Miwic3ViIjozMywic2VjcmV0IjoiMXlCeXdHSE1LSW5jUVEiLCJleHBpcnkiOiIxNjY0NjY0NDgyIn0.1gaC5UypBJ2-8TszPfccy5GRSzqV3KKhPicMZMiw5-I' \
--data-raw '{
    "ticket_id": 25,
    "name":"b-1234",
    "status": "live"
}'


curl --location --request GET 'http://localhost:5000/branches' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjQ2ODQyODIsImlhdCI6MTY2NDU5Nzg4Miwic3ViIjozMywic2VjcmV0IjoiMXlCeXdHSE1LSW5jUVEiLCJleHBpcnkiOiIxNjY0NjY0NDgyIn0.1gaC5UypBJ2-8TszPfccy5GRSzqV3KKhPicMZMiw5-I' \
--data-raw '{
    "ticket_id": 25
}'

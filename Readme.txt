Api Endpoints:

User API Endpoints
http://127.0.0.1:8000/auth/users  -> GET -> show all the currents users
http://127.0.0.1:8000/auth/users/   -> POST -. create a new user (fields: username and password)
http://127.0.0.1:8000/auth/users/1 -> GET -> show user where id is 1
http://127.0.0.1:8000/auth/users/1 -. DELETE -> delete user where id is 1

Token generating API Endpoints
http://127.0.0.1:8000/api-token-auth/ -> POST -> Create the token for the user whose details is sent in the body.

Menu API Endpoints
http://127.0.0.1:8000/api/menu/ -> GET -> Show all menu items
http://127.0.0.1:8000/api/menu/  -> POST -> create a new menu items(fields:title,price,inventory)
http://127.0.0.1:8000/api/menu/1 -. GET -> show menu item with id 1
http://127.0.0.1:8000/api/menu/1 -> DELETE -> delete menu item with id 1
http://127.0.0.1:8000/api/menu/1 -> PATCH -> update the menu item data, where id is 1

Booking API Endpoints
http://127.0.0.1:8000/restaurant/booking/ -> GET -> show all bookings
http://127.0.0.1:8000/restaurant/booking/ -> POST -> create a new booking(FIELDS: name,no_of_guest,booking_date)
http://127.0.0.1:8000/restaurant/booking/1 -. GET -> show booking with id 1
http://127.0.0.1:8000/restaurant/booking/1 -> DELETE -> delete booking with id 1
http://127.0.0.1:8000/restaurant/booking/1 -> PATCH -> update the booking data, where id is 1


User and Password
Superuser : admindjango
password : employee123


# Final Capstone Project

This project is the final capstone for the Coursera Backend Development specialization. It includes user authentication, menu management, and booking management functionalities.

## API Endpoints

### User API Endpoints

- `GET` - Show all current users:
http://127.0.0.1:8000/auth/users

- `POST` - Create a new user (fields: username and password):
http://127.0.0.1:8000/auth/users/

- `GET` - Show user where id is 1:
http://127.0.0.1:8000/auth/users/1

- `DELETE` - Delete user where id is 1:
http://127.0.0.1:8000/auth/users/1


### Token Generating API Endpoints

- `POST` - Create the token for the user whose details are sent in the body:
http://127.0.0.1:8000/api-token-auth/


### Menu API Endpoints

- `GET` - Show all menu items:
http://127.0.0.1:8000/api/menu/

- `POST` - Create a new menu item (fields: title, price, inventory):
http://127.0.0.1:8000/api/menu/

- `GET` - Show menu item with id 1:
http://127.0.0.1:8000/api/menu/1

- `DELETE` - Delete menu item with id 1:
http://127.0.0.1:8000/api/menu/1

- `PATCH` - Update the menu item data where id is 1: http://127.0.0.1:8000/api/menu/1

### Booking API Endpoints

- `GET` - Show all bookings: http://127.0.0.1:8000/restaurant/booking/

- `POST` - Create a new booking (fields: name, no_of_guest, booking_date):
http://127.0.0.1:8000/restaurant/booking/

- `GET` - Show booking with id 1: http://127.0.0.1:8000/restaurant/booking/1

- `DELETE` - Delete booking with id 1: http://127.0.0.1:8000/restaurant/booking/1

- `PATCH` - Update the booking data where id is 1: http://127.0.0.1:8000/restaurant/booking/1


## Getting Started

To get started with this project, clone the repository and follow the installation instructions.

### Prerequisites

- Python 3.7+
- Django 3.2+
- Virtualenv (optional, but recommended)

### Installation

1. Clone the repository:
 
 `git clone https://github.com/Franklyn883/Littlelemon-capstone-project.git`

 cd capstone-project

2. Create and activate a virtual environment:
`python -m venv venv`
`source venv/bin/activate`  # On Windows use `venv\Scripts\activate`

3. Install dependencies: `pip install -r requirements.txt`

4. Apply migrations: `python manage.py migrate`

5. Create a superuser: `python manage.py createsuperuser`

6. Run the server: `python manage.py runserver` 

7. Visit http://127.0.0.1:8000 in your browser to interact with the application.

## Contact
For any questions or inquiries, please contact Frank Alimimian at frankalimimian@gmail.com.






















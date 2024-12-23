# keyboard-store-backend

Backend APIs for a simple keyboard store. Made using Django Rest Famework (DRF)

## Contents

1. [Features](#features)
2. [How to run this project](#how-to-run-this-project)
3. [API documentation](#api-documentation)
   1. [Authentication](#authentication)
   2. [User Management](#user-management)
   3. [Products](#products)

## Features

- Allows 3 different types of users: customer, staff, admin
- Only staff and admin users are allowed full **CRUD** functionality, customers can only view products
- **JWT authentication**
- **Keyboard** and **Switches** are the 2 products
  - **Keyboard:** Allows 2 types - membrane and mechanical
  - **Switches:** Allows 3 types - linear, tactile, clicky

## How to run this project

**Prerequisites:** Have python 3.x installed

1. Clone the Repository
   ```bash
   git clone https://github.com/Dilpreet-singh-13/keyboard-store-backend.git
   cd keyboard-store-backend
   ```
2. Set Up a Virtual Environment
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Unix or MacOS use `source venv/bin/activate`
   ```
3. Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```
4. Run Migrations

   By default this project uses the SQLite for simplicity. However, you can use other databases such as PostgreSQL, MySQL, or Oracle.

   To do this: Update the DATABASES configuration in settings.py with your database credentials.

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the Development Server
   ```bash
   python manage.py runserver
   ```

## API Documentation

- **Base URL:** `http://127.0.0.1:8000/api`
- Only the **Register User, Obtain Token and Refresh Token** endpoints don't need authentication. Rest of the endpoints need you to have the JWT access token in the request header

### 1. Authentication

#### Obtain Token

- **URL:** `/token/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```
- **Response:**
  ```json
  {
    "refresh": "refresh_token",
    "access": "access_token"
  }
  ```

#### Refresh Token

- **URL:** `/token/refresh/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "refresh": "refresh_token"
  }
  ```
- **Response:**
  ```json
  {
    "access": "new_access_token"
  }
  ```

### 2. User Management

#### Register a new User

- **URL:** `/user/register/`
- **Method:** `POST`
- **Description:** Registers a new user. If no admin exists, the first registered user is assigned the `admin` role.
- **Request Body:**
  ```json
  {
    "username": "new_username",
    "email": "user@example.com",
    "password": "your_password"
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "username": "new_username",
    "email": "user@example.com",
    "user_role": "admin"
  }
  ```

#### Promote a customer to staff

- **URL:** `/user/make-staff/`
- **Method:** `PUT`
- **Description:** Promotes a user with the `customer` role to the `staff role`. _Only admins can perform this action_.

- **Request Body:**
  ```json
  {
    "username": "new_username"
  }
  ```
- **Response:**
  - **Success (200)**
    ```json
    {
      "detail": "User customer_username promoted to staff."
    }
    ```
  - **Failure (400)**
  ```json
  {
    "detail": "Only customers can be promoted to staff."
    // OR
    "detail": "Customer with given username does not exist."
  }
  ```

### 3. Products

#### List & Create Switches

- **URL:** `/switch/`
- **Method:**
  - `GET`: Retrieves a list of all switches.
  - `POST`: Creates a new switch.
- **switch_type:** linear, tactile, clicky
- **Request Body: (For `POST`)**
  ```json
  {
    "name": "Cherry MX Red",
    "description": "A smooth linear switch.", //optional
    "switch_type": "linear",
    "price": 1.2
  }
  ```
- **Response:**
  - `GET`: Retrives list of all switches
  - `POST`: Retrives details of newly created switch

#### Retrieve, Update, and Delete a Switch

- **URL:** `/switch/<int:pk>/`
- **Method:**
  - `GET`: Retrieves details of a specific switch by ID
  - `PUT`: Upadtes an existing switch.
  - `PATCH`: Partially update an existing switch
  - `DELETE`: Delete a switch by ID
- **Request Body: (For `PUT` or `PATCH`)**

  ```json
  {
    "name": "switch 1",
    "description": "New switch yay!",
    "switch_type": "tactile",
    "price": 6.5
  }
  ```

- **Response:**
  - `GET`: All details of the specified switch
  - `PUT`: Updated detials of the specified switch
  - `PATCH`: Updated detials of the specified switch
  - `DELETE`: No response body, only the code `204 No Content`

#### List & Create Keyboards

- **URL:** `/keyboard/`
- **Method:**
  - `GET`: Retrieves a list of all keyboards.
  - `POST`: Creates a new keyboard.
- **keyboard_type:** membrane, mechanical
- **Validation rules for keyboard**
  - Switch is required for mechanical keyboards. Provide either `ID` or `name` of switch.
  - The switch field is automatically set to `null` if provided for membrane keyboards.
- **connectivity_options:** Comma-separated values like `Bluetooth, 2.4GHz, USB-C`.
- **Request Body: (For `POST`)**
  ```json
  {
    "name": "Keeb K69",
    "price": 79.99,
    "description": "RGB mechanical keyboard", // optional
    "keyboard_type": "mechanical",
    "weight": 1.2, // optional
    "connectivity_options": "wired, bluetooth", // optional
    "switch": 1 //Optional for "membrane" type, provide ID/Name for "mechanical" type
  }
  ```
- **Response:**
  - `GET`: Retrives list of all switches.
  - `POST`: Retrives details of newly created switch.

#### Retrieve, Update, and Delete a Keyboard

- **URL:** `/keyboard/<int:pk>/`
- **Method:**
  - `GET`: Retrieves details of a specific keyboard by ID.
  - `PUT`: Upadtes an existing keyboard.
  - `PATCH`: Partially update an existing keyboard
  - `DELETE`: Delete a keyboard by ID
- **Request Body: (For `PUT` or `PATCH`)**
  ```json
  {
    "name": "Keeb K69",
    "price": 79.99,
    "description": "RGB mechanical keyboard", // optional
    "keyboard_type": "mechanical",
    "weight": 1.2, // optional
    "connectivity_options": "wired, bluetooth", // optional
    "switch": 1 //Optional for "membrane" type, provide ID/Name for "mechanical" type
  }
  ```
- **Response:**
  - `GET`: All details of the specified keyboard.
  - `PUT`: Updated detials of the specified keyboard.
  - `PATCH`: Updated detials of the specified keyboard.
  - `DELETE`: No response body, only the code `204 No Content`.

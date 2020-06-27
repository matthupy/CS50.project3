# Project 3 - Pinocchio's Pizza and Subs Website

This project contains a web-based application that allows users to register for the applicaiton, view the menu for Pinocchio's Pizza & Subs, add items to a virtual cart, and place orders.

## Personal Touch - Email

Added functionality for sending order confirmation email, including the total cost of the order when an order is placed.

# Installation

Clone the code repository locally and navigate to the local code folder. Install the required components using:

    python -m pip install -r requirements.txt

# File Descriptions

## Users

File | Description
--- | ---
/users/templates/users/login.html | Login screen
/templates/users/logout.html | Logout confirmation screen
/templates/users/register.html | User Registration screen
/users/forms.py | Form definition for User Registration screen
/users/sviews.py | User Registration logic

## Orders

File | Description
--- | ---
/orders/migrations/\_\_init\_\_.py | System-generated initial file
/orders/migrations/0001_initial.py | Model creation script (Django generated)
/orders/static/jquery.bootstrap.modal.forms.js | Bootstrap jquery module
/orders/static/pinocchio.png | Pinocchio logo used for the application
/orders/static/style.css | CSS Styling used application-wide
/orders/templates/orders/checkout.html | Checkout screen
/orders/templates/orders/index.html | Home page, menu
/orders/templates/orders/layouts.html | Base HTML layout for the applicaiton, contains nav bar code and commonly-used javascript
/orders/templates/order_success.html | Order confirmation screen
/orders/admin.py | Registers custom models with the Django Admin application
/ordrs/forms.py | Contains form logic used in index.html for ordering
/orders/models.py | Contains data model definitions
/orders/urls.py | Registers all URLs used in the application (including internal URLs for updating application elements)
/orders/views.py | Main application logic, contains python code to control price calculations, "add to cart", "place order", and "clear cart" functionality, and logic for updating the number of items in the cart.


## Pizza

File | Description
--- | ---
/pizza/settings.py | Contains application settings, including Email SMTP inforamtion

## Shared

File | Description
--- | ---
/.gitignore | Defines files that should not be tracked by git (contains all \_\_pycache\_\_ folders)
/requirements.txt | All required components with component versions.
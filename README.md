# LMS-Task-
# Library Management System (LMS)

## Overview

The Library Management System (LMS) is a Django-based web application that manages library-related data. The system includes models for users, books, book details, and borrowed books, along with APIs for CRUD operations.

## Project Structure

- **my_site/**: Django project folder.
- **lms/**: Django app folder containing models, serializers, views, and API configurations.

## Setup

1. Install dependencies: `pip install django djangorestframework`.
2. Create Django project and app: `django-admin startproject my_site && python manage.py startapp lms`.
3. Configure settings in `myproject/settings.py`.
4. Create models, serializers, and views in `lms/`.
5. Run migrations: `python manage.py makemigrations && python manage.py migrate`.
6. Start the development server: `python manage.py runserver`.

## Configure PostgreSQL Database for Django Project

In your Django project's `settings.py` file, configure the PostgreSQL database as follows:

```python
# In your my_site/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER':'postgres',
        'PASSWORD':'admin@123',
        'HOST':'localhost',
        'PORT':'5432'
    }
}


## Models

### User Model

- `id`
- `name`
- `email`
- `membership_date`

### Book Model

- `id`
- `title`
- `isbn`
- `published_date`
- `genre`

### BookDetails Model

- `id`
- `bookid` (Foreign Key)
- `number_of_pages`
- `publisher`
- `language`

### BorrowedBooks Model

- `userid` (Foreign Key)
- `bookid` (Foreign Key)
- `borrowed_date`
- `return_date`

## Views

### UserView

- **GET** `/api/users/`: Retrieve all users.
- **POST** `/api/users/`: Create a new user.

### UserIdView
- **GET** `/api/users/<int:id>/`: Retrieve user details by ID.

### BookView

- **GET** `/api/books/`: Retrieve all books.
- **GET** `/api/books/<int:id>/`: Retrieve book details by ID.
- **POST** `/api/books/`: Add a new book.
- **PATCH** `/api/books/<int:id>/`: Assign or update book details.

### BookDetailsView

- **GET** `/api/books/<int:id>/`: Retrieve book details by ID.
- **PUT** `/api/books/<int:id>/`: Assign or update book details.

### BorrowedBooksView

- **GET** `/api/borrow/`: Retrieve all borrowed books.
- **POST** `/api/borrow/`: Borrow a book.
- **PUT** `/api/borrow/`: Return a book.


## Testing

Test the application using tools like Postman,ThunderClients or any HTTP client. Include necessary parameters and headers as documented in the API section.



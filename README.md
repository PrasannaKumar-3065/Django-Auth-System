# Django Custom Authentication Project

A simple Django-based user authentication system with custom session management and password hashing.

## Features

- User registration with password hashing using PBKDF2-HMAC-SHA256.
- User login with session-based authentication.
- Custom authentication decorator to protect views.
- User logout by flushing sessions.
- Basic UI templates for login, signup, home, and error pages.
- Uses Django messages framework for user feedback.

## Technologies Used

- Django (Python web framework)
- Cryptography library for secure password hashing
- Django session framework for login state management

## Project Structure
|--- accounts
|   |--- migrations
|   |   |--- 0001_initial.py
|   |   |--- __pycache__
|   |   |   |--- 0001_initial.cpython-39.pyc
|   |   |   |--- __init__.cpython-39.pyc
|   |   |--- __init__.py
|   |--- admin.py
|   |--- views.py
|   |--- __pycache__
|   |   |--- apps.cpython-39.pyc
|   |   |--- decorators.cpython-39.pyc
|   |   |--- views.cpython-39.pyc
|   |   |--- urls.cpython-39.pyc
|   |   |--- admin.cpython-39.pyc
|   |   |--- __init__.cpython-39.pyc
|   |   |--- models.cpython-39.pyc
|   |--- apps.py
|   |--- __init__.py
|   |--- tests.py
|   |--- decorators.py
|   |--- urls.py
|   |--- models.py
|--- DjangoAuthSystem
|   |--- wsgi.py
|   |--- settings.py
|   |--- asgi.py
|   |--- __pycache__
|   |   |--- settings.cpython-39.pyc
|   |   |--- urls.cpython-39.pyc
|   |   |--- wsgi.cpython-39.pyc
|   |   |--- __init__.cpython-39.pyc
|   |--- __init__.py
|   |--- urls.py
|--- templates
|   |--- IsoHome.html
|   |--- 404.html
|   |--- IsoLogin.html
|   |--- IsoSignUp.html
|--- manage.py


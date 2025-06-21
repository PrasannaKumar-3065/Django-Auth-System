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
| |--- migrations
| | |--- 0001_initial.py
| | |--- init.py
| | |--- pycache
| | |--- 0001_initial.cpython-39.pyc
| | |--- init.cpython-39.pyc
| |--- admin.py
| |--- apps.py
| |--- decorators.py
| |--- models.py
| |--- tests.py
| |--- urls.py
| |--- views.py
| |--- init.py
| |--- pycache
| |--- admin.cpython-39.pyc
| |--- apps.cpython-39.pyc
| |--- decorators.cpython-39.pyc
| |--- models.cpython-39.pyc
| |--- urls.cpython-39.pyc
| |--- views.cpython-39.pyc
| |--- init.cpython-39.pyc
|--- DjangoAuthSystem
| |--- asgi.py
| |--- settings.py
| |--- urls.py
| |--- wsgi.py
| |--- init.py
| |--- pycache
| |--- settings.cpython-39.pyc
| |--- urls.cpython-39.pyc
| |--- wsgi.cpython-39.pyc
| |--- init.cpython-39.pyc
|--- templates
| |--- IsoHome.html
| |--- IsoLogin.html
| |--- IsoSignUp.html
| |--- 404.html
|--- manage.py

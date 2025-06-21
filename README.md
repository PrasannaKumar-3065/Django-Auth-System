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


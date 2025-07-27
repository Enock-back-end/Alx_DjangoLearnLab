# LibraryProject

This is a Django project created during the ALX "Introduction to Django" module. It serves as the foundation for learning how Django works.

##  Project Structure

- `manage.py`: Django's command-line tool to run and manage the project.
- `LibraryProject/settings.py`: Main configuration file.
- `LibraryProject/urls.py`: URL routing file.
- `LibraryProject/wsgi.py` & `asgi.py`: Used for deployment.

# Permissions and Groups:
# - Groups created: Editors, Viewers, Admins
# - Permissions assigned using the Django admin
# - Views protected using @permission_required decorator

# Security Features:
# - DEBUG=False for production
# - CSRF, XSS, and clickjacking protection enabled
# - Cookies marked as secure
# - Views validated inputs via forms


# Security Summary
- HTTPS enforced with SECURE_SSL_REDIRECT
- HSTS configured with preload
- CSRF and session cookies secured
- Clickjacking and MIME-sniffing blocked with headers
- CSP policy applied

# Django Library Project

This project demonstrates advanced Django features including:

- Custom User Model with profile photo and date of birth
- Admin customization
- Permission-based views
- Secure app structure

## Setup Instructions

1. Create virtual environment and activate:
   ```bash
   python3 -m venv env
   source env/bin/activate

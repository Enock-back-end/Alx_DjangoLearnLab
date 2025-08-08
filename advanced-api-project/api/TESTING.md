# API Testing Strategy

## Tools Used:
- Django's built-in TestCase class
- DRF's APIClient for simulating HTTP requests

## Test Cases:
- ✅ List books (unauthenticated)
- ✅ Create book (authenticated vs unauthenticated)
- ✅ Update and delete book (authenticated only)
- ✅ Filter books by title, author, year
- ✅ Search books by partial match
- ✅ Order books by year or title

## How to Run Tests:
```bash
python manage.py test api


## API Endpoints for Book

| Method | Endpoint | Description | Permission |
|--------|----------|-------------|------------|
| GET | /books/ | List all books | Public |
| GET | /books/<id>/ | Retrieve one book | Public |
| POST | /books/create/ | Create a book | Authenticated users |
| PUT | /books/<id>/update/ | Update book | Authenticated users |
| DELETE | /books/<id>/delete/ | Delete book | Authenticated users |

### Custom Behavior:
- `perform_create`: Saves the book instance. Can be customized to assign request.user.
- `perform_update`: Hook for customizing update behavior.
- Permissions enforced using DRF’s `AllowAny` and `IsAuthenticated`.

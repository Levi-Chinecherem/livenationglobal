# LiveNationGlobal API

LiveNationGlobal is a Django-based API for managing musical band teams, developed using Django Rest Framework.

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

### Prerequisites

- Python (3.10 or higher)
- Django
- Django Rest Framework
- CKEditor
- Other dependencies (see requirements.txt)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Levi-Chinecherem/livenationglobal.git
   cd livenationglobal

   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations:

   ```bash
   python manage.py migrate
   ```
4. Create a superuser for admin access:

   ```bash
   python manage.py createsuperuser
   ```
5. Run the development server:

   ```bash
   python manage.py runserver
   ```

   The API will be available at http://127.0.0.1:8000/.

### API Endpoints

Based on the provided `urls.py` files, here's a complete list of API endpoints for your LiveNationGlobal project:

### Accounts Endpoints:

- **POST /api/accounts/register/:** Register a new user.
- **POST /api/accounts/login/:** Log in with email and password.
- **POST /api/accounts/logout/:** Log out the currently logged-in user.
- **PUT /api/accounts/change-password/:** Change the password for the logged-in user.

### Bands Endpoints:

- **GET /api/band/bands/:** List all bands.
- **GET /api/band/bands/[int:pk](int:pk)/:** Retrieve details of a specific band.
- **POST /api/band/join-band/[int:band_id](int:band_id)/:** Join a specific band by creating a membership.
- **GET /api/band/common-fields/:** Retrieve or update common fields for the logged-in user.
- **GET /api/band/bands/[int:band_id](int:band_id)/membership-types/:** List membership types for a specific band.
- **GET /api/band/membership-types/[int:pk](int:pk)/:** Retrieve details of a specific membership type.

### Chat Endpoints:

- **GET /api/chat/user-chats/:** List all chat messages for the logged-in user.
- **GET /api/chat/admin-chats/:** List all chat messages for admin users.
- **GET /api/chat/chats/[int:pk](int:pk)/:** Retrieve details of a specific chat message.
- **POST /api/chat/user-chats/create/:** Create a new chat message for the logged-in user.
- **POST /api/chat/admin-chats/create/:** Create a new chat message for admin users.

### Swagger and ReDoc Documentation:

- **Swagger Documentation:** [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- **ReDoc Documentation:** [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

### Django Admin:

- **Django Admin Interface:** [http://localhost:8000/admin/](http://localhost:8000/admin/)

Ensure you replace `http://localhost:8000/` with the appropriate base URL if your development server is running on a different address.

### Frontend Authentication

Integrate frontend authentication using the provided API endpoints.

## Built With

- [Django](https://www.djangoproject.com/) - Web framework
- [Django Rest Framework](https://www.django-rest-framework.org/) - Toolkit for building Web APIs
- [CKEditor](https://ckeditor.com/) - Rich text editor

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

```

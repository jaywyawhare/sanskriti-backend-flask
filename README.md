# SanskritiBench Backend Flask

## Overview
This is the backend for the [SanskritiBench project](https://discord.com/invite/BK8UmK3xZC). It is a REST API backend built using Flask for managing contributions in multiple languages. It provides endpoints for user authentication, contribution management, and user management with role-based access control.

## Features

- **Authentication**: JWT-based authentication for secure user login and registration.
- **Contributions**: CRUD operations for managing contributions, with role-based access control.
- **Users**: User management endpoints for administrators to manage user accounts.

## Technologies Used

- **Python**: Programming language used for backend development.
- **Flask**: Micro web framework used for building the API.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library for database operations.
- **Flask-JWT-Extended**: Flask extension for JSON Web Tokens (JWT) authentication.
- **Docker**: Containerization platform used for packaging the application and dependencies.

## Setup

To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/jaywyawhare/sanskritibench-backend-flask.git
   cd sanskritibench-backend-flask
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file based on `.env.example` and configure necessary variables.


4. **Run the application**:
   ```bash
   python main.py
   ```

5. **Access the API**:
   The API will be available at `http://localhost:5000/`.

## API Documentation

For detailed API endpoints and usage, refer to the [API Documentation](docs/API.md).

## Testing

Unit tests are implemented using `pytest`. To run tests, use:
```bash
pytest
```

## License

This project is licensed under the **DBaJ-NC-CFL** License - see the [LICENSE](./LICENCE.md) file for details.

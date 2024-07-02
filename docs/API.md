### API Documentation

#### Authentication Endpoints

##### Register User

- **URL:** `/auth/register`
- **Method:** `POST`
- **Description:** Registers a new user with email and password.
- **Request:**
  ```json
  {
      "email": "user@example.com",
      "password": "password"
  }
  ```
- **Response:**
  ```json
  {
      "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
  }
  ```

##### Login

- **URL:** `/auth/login`
- **Method:** `POST`
- **Description:** Logs in an existing user with email and password.
- **Request:**
  ```json
  {
      "email": "user@example.com",
      "password": "password"
  }
  ```
- **Response:**
  ```json
  {
      "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
  }
  ```

##### Logout

- **URL:** `/auth/logout`
- **Method:** `GET`
- **Description:** Logs out the currently logged-in user.
- **Authentication:** Requires JWT token in the Authorization header.
- **Response:**
  ```json
  {
      "message": "Successfully logged out"
  }
  ```

#### User Management Endpoints

##### Get Current User

- **URL:** `/me`
- **Method:** `GET`
- **Description:** Retrieves details of the current logged-in user.
- **Authentication:** Requires JWT token in the Authorization header.
- **Response:**
  ```json
  {
      "id": 1,
      "email": "user@example.com",
      "role": "admin",
      "language": "en"
  }
  ```

##### Get All Users

- **URL:** `/users/`
- **Method:** `GET`
- **Description:** Retrieves a list of all users.
- **Authentication:** Requires JWT token with admin role in the Authorization header.
- **Response:**
  ```json
  [
      {
          "id": 1,
          "email": "user1@example.com",
          "role": "contributor",
          "language": null
      },
      {
          "id": 2,
          "email": "user2@example.com",
          "role": "manager",
          "language": "fr"
      }
  ]
  ```

##### Create User

- **URL:** `/users/`
- **Method:** `POST`
- **Description:** Creates a new user.
- **Request:**
  ```json
  {
      "email": "newuser@example.com",
      "password": "password",
      "role": "contributor"
  }
  ```
- **Response:**
  ```json
  {
      "id": 3,
      "email": "newuser@example.com",
      "role": "contributor",
      "language": null
  }
  ```

##### Update User

- **URL:** `/users/<id>`
- **Method:** `PUT`
- **Description:** Updates an existing user.
- **Request:**
  ```json
  {
      "email": "updateduser@example.com",
      "password": "newpassword",
      "role": "manager"
  }
  ```
- **Response:**
  ```json
  {
      "id": 3,
      "email": "updateduser@example.com",
      "role": "manager",
      "language": null
  }
  ```

##### Delete User

- **URL:** `/users/<id>`
- **Method:** `DELETE`
- **Description:** Deletes an existing user.
- **Response:**
  ```json
  {
      "message": "User deleted"
  }
  ```

#### Contribution Endpoints

##### Get All Contributions

- **URL:** `/contributions/`
- **Method:** `GET`
- **Description:** Retrieves all contributions based on user role.
- **Authentication:** Requires JWT token with appropriate roles in the Authorization header.
- **Response:**
  ```json
  [
      {
          "id": 1,
          "user_id": 1,
          "language": "en",
          "question": "What is Flask?",
          "answer": "Flask is a lightweight WSGI web application framework",
          "created_at": "2024-07-02T10:00:00Z"
      },
      {
          "id": 2,
          "user_id": 2,
          "language": "fr",
          "question": "Qu'est-ce que Flask?",
          "answer": "Flask est un framework web WSGI léger",
          "created_at": "2024-07-02T11:00:00Z"
      }
  ]
  ```

##### Create Contribution

- **URL:** `/contributions/`
- **Method:** `POST`
- **Description:** Creates a new contribution.
- **Request:**
  ```json
  {
      "language": "en",
      "question": "What is SQLAlchemy?",
      "answer": "SQLAlchemy is an SQL toolkit and Object-Relational Mapping (ORM) library"
  }
  ```
- **Response:**
  ```json
  {
      "id": 3,
      "user_id": 1,
      "language": "en",
      "question": "What is SQLAlchemy?",
      "answer": "SQLAlchemy is an SQL toolkit and Object-Relational Mapping (ORM) library",
      "created_at": "2024-07-02T12:00:00Z"
  }
  ```

##### Update Contribution

- **URL:** `/contributions/<id>`
- **Method:** `PUT`
- **Description:** Updates an existing contribution.
- **Request:**
  ```json
  {
      "language": "fr",
      "question": "Qu'est-ce que SQLAlchemy?",
      "answer": "SQLAlchemy est une bibliothèque de cartographie relationnelle d'objets et un outil SQL"
  }
  ```
- **Response:**
  ```json
  {
      "id": 3,
      "user_id": 1,
      "language": "fr",
      "question": "Qu'est-ce que SQLAlchemy?",
      "answer": "SQLAlchemy est une bibliothèque de cartographie relationnelle d'objets et un outil SQL",
      "created_at": "2024-07-02T12:00:00Z"
  }
  ```

##### Delete Contribution

- **URL:** `/contributions/<id>`
- **Method:** `DELETE`
- **Description:** Deletes an existing contribution.
- **Response:**
  ```json
  {
      "message": "Contribution deleted"
  }
  ```

##### Get Contributions by Language

- **URL:** `/contributions/language/<language>`
- **Method:** `GET`
- **Description:** Retrieves contributions filtered by language.
- **Authentication:** Requires JWT token with admin or manager role in the Authorization header.
- **Response:**
  ```json
  [
      {
          "id": 2,
          "user_id": 2,
          "language": "fr",
          "question": "Qu'est-ce que Flask?",
          "answer": "Flask est un framework web WSGI léger",
          "created_at": "2024-07-02T11:00:00Z"
      }
  ]
  ```

### Error Handling

- **401 Unauthorized:**
  ```json
  {
      "message": "Unauthorized"
  }
  ```
- **403 Forbidden:**
  ```json
  {
      "message": "Forbidden"
  }
  ```
- **404 Not Found:**
  ```json
  {
      "message": "Resource not found"
  }
  ```

### Notes

- Ensure to replace placeholder URLs and method descriptions with actual endpoints and specific details from your application.
- Consider adding more detailed descriptions for each endpoint, especially inputs and expected outputs.

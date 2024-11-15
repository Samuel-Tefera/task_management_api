# **Task Management API Documentation**

## **Overview**

The Task Management API enables efficient task management for users, including task creation, updates, statistics, and authentication. The API uses token-based authentication for secure operations.


## **Base URL**
```
http://127.0.0.1:8000/
```

## **Authentication**

- Token-based authentication is required for all endpoints except for user creation and token generation.
- Include the token in the `Authorization` header for authenticated requests:
  ```
  Authorization: Token <your_token>
  ```


## **Endpoints**

### **1. User Endpoints**

#### **1.1 Create a User**
- **URL:** `/user/create`
- **Method:** `POST`
- **Description:** Create a new user account.
- **Body Parameters:**
  ```json
  {
      "first_name": "John",
      "last_name": "Doe",
      "email": "johndoe@example.com",
      "password": "securepassword"
  }
  ```
- **Response:**
  - **201 Created:** User created successfully.
  - **400 Bad Request:** Validation errors.


#### **1.2 Request Token**
- **URL:** `/user/token`
- **Method:** `POST`
- **Description:** Generate an authentication token.
- **Body Parameters:**
  ```json
  {
      "email": "johndoe@example.com",
      "password": "securepassword"
  }
  ```
- **Response:**
  ```json
  {
      "token": "your_token_here"
  }
  ```
  - **200 OK:** Token generated successfully.
  - **401 Unauthorized:** Invalid credentials.


#### **1.3 Get User Info**
- **URL:** `/user/me`
- **Method:** `GET`
- **Description:** Retrieve the authenticated user’s details.
- **Response:**
  ```json
  {
      "first_name": "John",
      "last_name": "Doe",
      "email": "johndoe@example.com"
  }
  ```


#### **1.4 Modify User Info**
- **URL:** `/user/me`
- **Method:** `PATCH` or `PUT`
- **Description:** Update the authenticated user’s information.
- **Body Parameters (example):**
  ```json
  {
      "first_name": "Jane",
      "last_name": "Doe"
  }
  ```
- **Response:**
  - **200 OK:** User info updated successfully.
  - **400 Bad Request:** Validation errors.


### **2. Task Endpoints**

#### **2.1 Create a Task**
- **URL:** `/task/task`
- **Method:** `POST`
- **Description:** Create a new task.
- **Body Parameters:**
  ```json
  {
      "title": "Finish Documentation",
      "due_date": "2024-12-01",
      "category": "Work",
      "priority": "High",
      "status": "Pending",
      "description": "Write detailed API documentation.",
      "user": 1
  }
  ```
- **Response:**
  - **201 Created:** Task created successfully.
  - **400 Bad Request:** Validation errors.


#### **2.2 List All Tasks**
- **URL:** `/task`
- **Method:** `GET`
- **Description:** Retrieve a list of all tasks for the authenticated user.
- **Response Example:**
  ```json
  [
      {
          "id": 1,
          "title": "Task 1",
          "priority": "High",
          "status": "Pending",
          "due_date": "2024-12-01"
      },
      ...
  ]
  ```


#### **2.3 Get Task Details**
- **URL:** `/task/task/<task_id>`
- **Method:** `GET`
- **Description:** Retrieve detailed information about a specific task.
- **Response Example:**
  ```json
  {
      "id": 11,
      "title": "Task Title",
      "category": "Category",
      "status": "Status",
      "priority": "Priority",
      "created_at": "2024-11-03",
      "due_date": "2024-11-12",
      "completed_at": null,
      "duration": "Task not completed yet!",
      "description": "Detailed task description."
  }
  ```


#### **2.4 Update a Task**
- **URL:** `/task/task/<task_id>`
- **Method:** `PATCH` or `PUT`
- **Description:** Update a task’s details.
- **Body Parameters (example):**
  ```json
  {
      "status": "Completed",
      "priority": "Low"
  }
  ```
- **Response:**
  - **200 OK:** Task updated successfully.
  - **400 Bad Request:** Validation errors.

---

#### **2.5 Delete a Task**
- **URL:** `/task/task/<task_id>`
- **Method:** `DELETE`
- **Description:** Delete a specific task.
- **Response:**
  - **204 No Content:** Task deleted successfully.
  - **404 Not Found:** Task not found.

---

#### **2.6 Task Statistics**
- **URL:** `/task/statistic`
- **Method:** `GET`
- **Description:** Retrieve task statistics for the authenticated user.
- **Response Example:**
  ```json
  {
      "total_tasks": 50,
      "completed_tasks": 30,
      "overdue_tasks": 10,
      "in_progress_tasks": 5,
      "pending_tasks": 5,
      "completion_percentage": 60.0,
      "completion_by_priority": {
          "High": 80.0,
          "Medium": 50.0,
          "Low": 40.0
      }
  }
  ```


## **Error Responses**

- **401 Unauthorized:** Authentication credentials are missing or invalid.
- **404 Not Found:** The requested resource does not exist.
- **400 Bad Request:** Invalid input or request data.


## **Notes**

- Ensure a valid token is included for all authenticated endpoints.
- Use appropriate HTTP methods for each endpoint.
- Input validation is critical to prevent errors.


# Task Management API

The **Task Management API** is a robust backend service that helps users organize and monitor their tasks with comprehensive management and tracking features. This API is designed for efficiency, providing essential task operations along with advanced progress tracking, filtering, and sorting capabilities. Built with Django and Django REST Framework (DRF), the API leverages PostgreSQL for data storage and token-based authentication for secure access.


## Table of Contents

1. [Features](#features)
2. [Tech Stack](#tech-stack)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Environment Setup](#environment-setup)
6. [Usage](#usage)
7. [Documentation](#documentation)
8. [Contributing](#contributing)
9. [License](#license)
10. [Acknowledgments](#acknowledgments)

---

## Features

- **User Authentication:** Token-based authentication for secure access.
- **Task Management:** Create, update, delete, and list tasks.
- **Filtering & Sorting:** Filter tasks by status, priority, and category; sort by due date or priority.
- **Progress Tracking:** View statistics like total tasks, completed tasks, overdue tasks, and completion percentage.

---

## Tech Stack

- **Backend:** Django & Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** Token-based (DRF)
- **Environment Management:** Python Decouple

---

## Prerequisites

Ensure the following are installed:
- Python 3.9+
- PostgreSQL

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Samuel-Tefera/task_management_api.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd task_management_api
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up the `.env` file:**
   Refer to `.env.example` for the required variables.
5. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```
6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## Environment Setup

Create a `.env` file in the project root with the following variables:

```plaintext
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=your_db_name
DB_PASSWORD=your_db_password
DB_HOST=locahost
DB_PORT=5432
```

## Usage

- **Start the server:**
  ```bash
  python manage.py runserver
  ```
- Access the API at `http://127.0.0.1:8000/`.


## Documentation

Detailed API documentation, including endpoints and usage, is available in the [API Documentation](docs/api_endpoint.md).


## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to your branch (`git push origin feature-name`).
5. Open a pull request.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


## Acknowledgments

Special thanks to:
- Django and Django REST Framework communities
- OpenAI for technical guidance

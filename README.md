# Bulk Notification API

A Django REST Framework API that allows clients to create a sender and multiple notifications in a single request using efficient bulk database operations.

## Features

- Create one sender and multiple notifications in a single API request
- Uses `bulk_create()` for efficient database inserts
- Request validation with Django REST Framework serializers
- Atomic database transactions to ensure data consistency
- Django Admin for managing senders and notifications
- RESTful API design

## Tech Stack

- Python 3
- Django 6
- Django REST Framework
- SQLite

## Project Structure

```
bulk_notifications/
│
├── bulk_notifications/
├── notifications/
├── manage.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository

```bash
git clone <repository-url>
cd bulk_notifications
```

Create a virtual environment

```bash
python -m venv myenv
```

Activate the environment

Linux/macOS

```bash
source myenv/bin/activate
```

Windows

```bash
myenv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run migrations

```bash
python manage.py migrate # cretes the required db tables
```

Start the server

```bash
python manage.py runserver
```

The API will be available at

```
http://127.0.0.1:8000/
```

---

## API Endpoint

### Create Bulk Notifications

**POST**

```
/api/notifications/bulk/
```

### Sample Request

```json
{
    "name": "Mary",
    "email": "mary@test.com",
    "notifications": [
        {
            "title": "Welcome",
            "message": "Hello Mary",
            "channel": "email"
        },
        {
            "title": "Reminder",
            "message": "Meeting at 2 PM",
            "channel": "sms"
        }
    ]
}
```

### Sample Success Response

```json
{
    "message": "Bulk notifications created successfully.",
    "sender_id": 1,
    "notifications_created": 2
}
```

## Admin Panel

The Django admin interface is available at

```
/admin/
```

Create an administrator account using

```bash
python manage.py createsuperuser
```

## Author

**Mary Mburu**
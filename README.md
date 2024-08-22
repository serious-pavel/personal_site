# Personal Site

This project is my interpretation of tasks from [Python Django - The Practical Guide](https://www.udemy.com/course/python-django-the-practical-guide).
This is a Django-based web application. Below are the steps to set up the project on your local machine.

## Prerequisites

Before you begin, make sure you have the following installed on your system:

- Python (3.12 recommended, should work properly on lower versions, but not tested)
- pip (Python package installer)
- Virtualenv (optional, but recommended)

## Setup Instructions

### 1. Clone the repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/serious-pavel/personal_site.git
cd personal_site
```

### 2. Create a virtual environment (optional but recommended)
To isolate the project dependencies, create a virtual environment:
```bash
# On Windows
python -m venv venv

# On macOS/Linux
python3 -m venv venv
```

Activate the virtual environment:

```bash
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies
With the virtual environment activated, install the required packages:

```bash
pip install -r requirements.txt
```
### 4. Set up the database (skip if you're using an existing database*)

Apply the migrations to set up the database schema:

```bash
# On Windows
python manage.py migrate

# On macOS/Linux
python3 manage.py migrate
```
### 5. Create a superuser (skip if you're using an existing database*)
Create an admin account to access the Django admin panel:

```bash
# On Windows
python manage.py createsuperuser

# On macOS/Linux
python3 manage.py createsuperuser
```

### 6. Run the development server
Start the Django development server:

```bash
# On Windows
python manage.py runserver

# On macOS/Linux
python3 manage.py runserver
```
You can now access the project at http://127.0.0.1:8000/ in your web browser.


### * Using an existing database

Place file `db.sqlite3` in the project folder.
📝 Task Manager
A full-stack Task Manager web app built with Django REST Framework and React.js. Users can register, log in, and manage their personal tasks. Admins and staff can manage users and tasks through the Django admin panel.



🚀 Features
🔐 User registration and JWT authentication

🗒️ Create, update, complete, and delete tasks

📋 Separate views for staff and users

⚙️ Django Admin panel with restricted permissions


🛠️ Tech Stack
Backend:

Django
Django REST Framework
PostgreSQL (via Railway)
JWT Authentication

Frontend:

React.js
Axios
React Router DOM


SETUP INSTRUCTIONS
clone the repo
cd `into you directory`
create vitrual environment
`py -m venv env
source env/Scripts/activate
pip install -r requirements.txt
cd frontend
npm install`

start django server
`cd ..
cd backend`
inside setting.py remove defaul postgresql database and use db.splite3
`DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
`
make migrations`
py manage.py makemigrations
py manage.py migrate`

create a super userfor youself

start frontend

`cd ..
cd frontend
npm run dev `

Follow the given ports
You

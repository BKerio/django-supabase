django_supabase/
│
├── manage.py
├── .env
│
├── config/
│   ├── settings.py
│   ├── urls.py
│
└── core/
    ├── models.py
    ├── views.py
<!-- Setting up a new django app -->
mkdir django_supabase
cd django_supabase

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

django-admin startproject config .
python manage.py startapp core

pip install django psycopg2-binary python-dotenv

<!-- Supabase Credentials -->
Host: aws-0-us-east-1.pooler.supabase.com
Port: 6543
Database: postgres
User: postgres.xxx
Password: ********

SECRET_KEY=django-secret

DB_NAME=postgres
DB_USER=postgres.xxxxxx
DB_PASSWORD=yourpassword
DB_HOST=aws-0-us-east-1.pooler.supabase.com
DB_PORT=6543
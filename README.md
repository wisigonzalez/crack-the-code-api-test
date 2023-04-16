# Crack the code api test

## Stack

- Backend
  - [Python](https://www.python.org/)
  - [Django](https://www.djangoproject.com/)
  - [Django rest framework](https://www.django-rest-framework.org/)

## Highlights

- Clean architecture
- Clean code
- Gitflow
- MVC pattern
- Custom labels for PR on repository
- Follow guidelines

## Requeriments
Mandatory

- Python >= 3.11.3

If you have installed pip3
- pip3 install -r requirements.txt

If you have installed pip
- pip install -r requirements.txt 

## Local configuration
If you wish run the project with python3, then:

1. python3 manage.py makemigrations
2. python3 manage.py migrate
3. python3 manage.py createsuperuser `(follow the instructions)`
4. python3 manage.py runserver
5. go to `http://localhost:8000/`
6. see the magic

If you wish run the project with python, then:

1. python manage.py makemigrations
2. python manage.py migrate
3. python manage.py createsuperuser (follow the instructions)
4. python manage.py runserver
4. go to `http://localhost:8000/`
5. see the magic

If you wish see the api doc, then:

1. go to `http://localhost:8000/crack-the-code/api-docs`

If you wish see the admin, then:

1. go to `http://localhost:8000/crack-the-code/admin`
2. enter the username and password you created previously `(With the command python manage.py createsuperuser)`

If you wish see the api root, then:

1. go to `http://localhost:8000/crack-the-code/api`

If you wish see the api re doc, then:

1. go to `http://localhost:8000/crack-the-code/api-re-docs`

## Folder structure
Explanation of hierarchies in files and layers.

    crack-the-code-api-test/
      ├── crack_the_code_api/              # Settings, urls API folder
      └── crack_the_code_app/              # Controllers, models, views, serializers of application folder
          └── migrations/                  # DB migrations folder

## Branches

- `main` >>> All features
- `feature/initial-configuration-and-endpoints` >>> initial configurations and create CRUD's.
- `bgfix/documentation` >>> Fix the documentation.

## Other details

- This is a basic system of online courses.

# License

MIT
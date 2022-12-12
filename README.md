# Backend

Can be ran either in docker or a python virtual env

```
cd backend
docker-compose up
docker exec -it backend_web_1 python manage.py migrate
```
or

```
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Once running, the database can be populated by running the import submissions command

```
docker exec -it backend_web_1 python manage.py import_submissions

or

python manage.py import_submissions
```

# Frontend

With the backend running, the front end can be seen by loading the submissions.html file in any web browser
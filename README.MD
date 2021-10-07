## TEST TASK

## Admin Catalog
The object of this task is to create a simple flask application using flask-admin and flask-security libraries.

## Set up and run project:

You can do it by 2 ways:
### Using Docker
You should change your working directory to 'admin_catalog' and run commands:
```
docker-compose build --no-cache
docker-compose up
```
After all you will see the link to the application index page.
### Without Docker

You should change your work directory to 'admin_catalog', activate your virtual environment(if you are using it) and run commands:
```
pip install -r requirements.txt
python run.py
```
After all application will be available at  ```http://127.0.0.1:5000/```

On the main page (`````'/'`````) you can find some extra description and instructions.
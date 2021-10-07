## TEST TASK

## Admin Catalog
The object of this task is to create a simple flask application using flask-admin and flask-security libraries.

## Set up and run project:

You can do it by 2 ways:
### Using Docker
You should change your working directory to 'admin_catalog' and run command:
```
docker-compose up
```

### Without Docker

You should change your work directory to 'admin_catalog', activate your virtual environment(if you are using it) and run commands:
```
pip install -r requirements.txt
python run.py
```
After all you will see the link to the application index page in terminal.

On the index page (`````'/'`````) you can find some extra description and instructions.

Don't forget! All vulnerable data, such as SECRET_KEY or SALT for password hash must be hide if you are using application in production. You should also change DEBUG mode to False.
## Chapter 2: Project, app, wsgi, asgi, and the files

### Setting up a Django Project

Its best practice to create a virtual environment to base your project off of. So lets do that first, as we are creating a todo app lets name it and create a folder for it.

```bash
mkdir mocha
```

Im calling the project mocha. After creating the project we move to the created directory.

```bash
cd mocha
```

To create a virtual environment we can excecute

```bash
python -m venv my-virtual-environment
```

This will create a virtual environment called 'my-virtual-environment` in the folder. To activate this virtual environment we run

```bash
source my-virtual-environment/bin/activate
```

once the virtual environment is active, we will see

![virtual_environment](./assets/Screenshot_2024-07-23_at_5.12.41_PM.png)

> We don’t push the virtual environment related files to git. So its better to add a `.gitignore` to the project now

TODO: ADD `.gitignore` DOCS HERE

To deactivate the virtual environment we can just run:

```bash
deactivate
```

Once that is done we can install Django and set up our project. To install Django

```bash
pip install django
```

Once django is installed we can start a project.

```bash
django-admin startproject mocha .
```

> Note the `.` in the end? If that is missing django will enclose the app in a folder. We don't want that hence the `.` . We want it to scaffold it in the CWD(current working directory)

Now run

```
python manage.py runserver
```

head to `localhost:8000` you'll be treated with the django starter page.

Now lets talk about the files and the structure

The main Django app structure will look like:

```
mocha/
    manage.py
    mocha/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

- `manage.py` is program used to manage the django project.
- `mocha/__init__.py` is an empty file that tells Python that this directory should be considered a Python package.
- `mocha/settings.py` is the settings/configuration for this Django project.
- `mocha/urls.py` is the list of urls declarations for the django project.
- `mocha/asgi.py` An entry-point for ASGI-compatible web servers to serve your project. ASGI (Asynchronous Server Gateway Interface)
- `mocha/wsgi.py` An entry-point for WSGI-compatible web servers to serve your project. WSGI (Web Server Gateway Interface)


Now we need to create an app for the todo, this will help modularize the app.

```
django-admin startapp todo
```

the todo app would look something like this
```
todo/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

- `todo/admin.py` used for wiring the app to django admin
- `todo/apps.py` contains the app config for the app
- `migrations/` contains all the generated db migrations
- `todo/models.py` used to configure the db models for the app
- `todo/tests.py` used to write tests for the app
- `todo/views.py` used to write the views for the app

see [this pull request](https://github.com/xenomech/learn-django/pull/2)

[Next chapter](chapter_3.md)

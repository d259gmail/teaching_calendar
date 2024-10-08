# Teaching Calendar

Simple Teaching Calendar with Django We aim to develop a straightforward teaching calendar application using the Django framework. This application will provide teachers with a personalized view of their teaching schedule, including the subjects they teach and the lesson names scheduled for specific dates.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

License: MIT

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Running this project
      $ docker compose -f docker-compose.local.yml up -d --build

#### Make Migrations and migrate
      $ docker compose -f docker-compose.local.yml run --rm django python manage.py makemigrations 
      $ docker compose -f docker-compose.local.yml run --rm django python manage.py migrate

### Stopping
      $ docker compose -f docker-compose.local.yml down --remove-orphans

### Checking the logs
      $ docker compose -f docker-compose.local.yml logs -f --tail 100

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ docker compose -f docker-compose.local.yml run --rm django python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Setting up the teacher, lessons and subjects
      - After logging into the platform and creating the superuser, log in to the Django admin portal. 
      - In the Django admin, create the user, then add subjects and lessons. 
      - Once this is done, return to the platform and click on the "My Profile" button. 
      - You will be able to see your schedule and other details there. 
      - A download option will also be available on the same page to download the teacher's schedule. 
      - Please note that all these pages are authenticated, and you will not be able to access them without logging in.

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).

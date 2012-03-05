Django basic setup

* Twitter bootstrap
* HTML5-Boilerplate

----

Setup
=====

- Create new project directory
- Setup and activate virtualenv
- Install dependencies (`pip install -r requirements.txt`)

- Setup Django project (`django-admin.py startproject boilerplate`)


- Create the database and add config to settings.py
- Sync db and create admin user (`python manage.py syncdb`)


- Start app (`python manage.py startapp helloworldapp`)
- Create models
- Add app to installed_apps in settings.py (also enable the admin url's if you want)


- Inspect app's SQL structure (`python manage.py sql helloworldapp`)
- Sync db again

----------------
Well done. Now lets dive into the app (https://docs.djangoproject.com/en/1.3/intro/tutorial02/)
----------------

- Add custom `urls.py` file to the app and include from main `urls.py` file




Django basic setup with some goodies!

* [Twitter bootstrap](http://twitter.github.com/bootstrap/)
* [LessCSS](http://lesscss.org/)


How to do it yourself
---------------------

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


Well done. Now lets dive into the app (https://docs.djangoproject.com/en/1.3/intro/tutorial02/)

- Add custom urls to the `urls.py` file, and some views, perhaps even templates


Setting up static files (https://docs.djangoproject.com/en/dev/howto/static-files/)

* Create a /static/ direectory and update settings.py


-----------------------------------

Enabling Twitter-Bootstrap
--------------------------

It's added as a git submodule (into `boilerplate/static/twitter-bootstrap`), so just do

    $ git submodule init
    $ git submodule update

Make sure you have the LessCSS compiler (`lessc`) installed, as well as `uglifyjs`.

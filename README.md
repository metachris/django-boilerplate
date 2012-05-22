Django Boilerplate is a fast, robust and future-proof base template to get your project off the ground quickly and right-footed.

* [Twitter bootstrap](http://twitter.github.com/bootstrap/) (uses [LessCSS](http://lesscss.org/)) and jQuery
* Split settings files for dev/test/prod environments
* [South](http://south.aeracode.org/) for database migrations
* Caching with [Redis](https://github.com/sebleier/django-redis-cache/) and [Cache Machine](https://github.com/jbalogh/django-cache-machine)
* Custom template tags, Forms examples, etc.
* [django-debug-toolbar](https://github.com/django-debug-toolbar)


Quick Start
===========
Create a project directory, setup virtualenv, clone the project and setup the dependencies:

	# Create and activate virtual env
	$ virtualenv <ENV_DIR>
	$ . <ENV_DIR>/bin/activate

	# Clone django-boilerplate and install dependencies
    $ git clone django-boilerplate
    $ cd django-boilerplate
    $ pip install -r dependencies.txt

    # Setting up Twitter Bootstrap
    $ git submodule init
    $ git submodule update

    # finally setup bootstrap dependencies and build bootstrap


Twitter-Bootstrap
=================

Bootstrap is added as a git submodule (into `boilerplate/static/twitter-bootstrap`). Make sure you have the LessCSS compiler (`lessc`) and `uglifyjs` installed for the build toolchain to work. To build bootstrap, execute the following command in `boilerplate/static/twitter-bootstrap`:

    $ make build


South: Easy Database Schema Migrations
======================================

South detects model changes and makes schema migrations extremely easy as well as reversible and documented. It is basically used as a replacement for `syncdb`. The [South tutorial](http://south.readthedocs.org/en/latest/index.html) shows how to easily setup South for an
all new app or converting an existing one.

South with a brand new app
--------------------------
Before any models are created, run syncdb once to add the tables for the apps.

    $ python manage.py syncdb

After the initial db setup, store the schema:

    $ python manage.py schemamigration <APP_NAME> --initial


South with an existing app
--------------------------
When models are already saved in the database, we need to run `syncdb` to add the tables for the
south app, and then `convert_to_south <appname>`:

    $ python manage.py syncdb
    $ python manage.py convert_to_south <APP_NAME>


Schema Migrations
-----------------
After changing a model we need to create the migration file, and then apply it to update the schema in the database:

    # Create migration file
    $ ./manage.py schemamigration <APP_NAME> --auto

    # Apply migration
    $ ./manage.py migrate <APP_NAME>


# vodka-soda-server

> Casual without compromise

## Set Up Local Dev Environment

Install tools and dependencies:

```bash
# Install [homebrew](https://brew.sh/)
> /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
> brew tap homebrew/bundle
> brew bundle
# Note: brew bundle installs deps from Brewfile (like PostGIS)

# Install [pyenv](https://github.com/pyenv/pyenv) (optional)
> brew install pyenv
> pyenv install 3.6.3

# Install [virtualenv-burrito](https://github.com/brainsik/virtualenv-burrito) (optional)
> curl -sL https://raw.githubusercontent.com/brainsik/virtualenv-burrito/master/virtualenv-burrito.sh | $SHELL

# Create a virtualenv and install python deps
> mkvirtualenv -p /usr/local/bin/python3.6 vodka-soda-server
> workon vodka-soda-server
(vodka-soda-server) > pip install -r requirements.txt
```

Add environment variables:

```bash
export DJ_DB_NAME=vodka-soda
export DJ_DB_USER=tom
export DJ_DB_PASSWORD=root
export DJ_DB_HOST=localhost
export DJ_DB_PORT=5432
export DJ_SECRET_KEY=+cg9iso$a55f3ay&)pdg3k&=lq_c*55j7oyuib=a(pi#2$oj^0
export DJ_SOCIAL_AUTH_FACEBOOK_KEY=234928371610299
export DJ_SOCIAL_AUTH_FACEBOOK_SECRET=3731939d837s7b1b0b772a64c7570edb
```

Create database:

```bash
(vodka-soda-server) > python manage.py makemigrations
```

Update migration file (`migrations/0001_initial.py`) to [create extension for `postgis`](https://docs.djangoproject.com/en/2.0/ref/contrib/gis/install/postgis/#creating-a-spatial-database):

```python
...
from django.contrib.postgres.operations import CreateExtension

class Migration(migrations.Migration):

    operations = [
        CreateExtension('postgis'),
        ...
    ]
```

Migrate and create an admin user

```bash
(vodka-soda-server) > python manage.py migrate
# Create an admin user
(vodka-soda-server) > python manage.py createsuperuser --email tom@meagher.co --username admin
```

If everything worked as planned, you should be able to `runserver` and access the admin app.

```bash
(vodka-soda-server) > python manage.py runserver
Starting development server at http://127.0.0.1:8000/
```

Go to the [admin site](http://127.0.0.1:8000/admin/oauth2_provider/application/add/) to create a new `Application` for the API to connect to.

## Creating/Updating DB Models

Whenever you make changes to a model, the database needs to be kept in sync.

```bash
> python manage.py makemigrations
> python manage.py migrate
```

See [Django Migrations Worflow](https://docs.djangoproject.com/en/2.0/topics/migrations/#workflow) for more info.

## Helpful links

+ [Django OAuth Toolkit with Django REST Framework Tutorial](https://django-oauth-toolkit.readthedocs.io/en/latest/rest-framework/rest-framework.html)
+ [Django REST Framework Social Oauth2 Facebook Example](https://github.com/PhilipGarnero/django-rest-framework-social-oauth2#facebook-example)
+ [dry-rest-permissions](https://github.com/dbkaplan/dry-rest-permissions)
+ [GeoDjango Installation](https://docs.djangoproject.com/en/2.0/ref/contrib/gis/install/)
+ [GeoDjango Tutorial](https://docs.djangoproject.com/en/2.0/ref/contrib/gis/tutorial/)
+ [Installing PostGIS](https://docs.djangoproject.com/en/2.0/ref/contrib/gis/install/postgis/)
+ [Facebook Developer Access Tokens](https://developers.facebook.com/tools/accesstoken/)
+ [Facebook App Dashboard](https://developers.facebook.com/apps/234319953810299/dashboard/)
+ [Tinder API](https://gist.github.com/rtt/10403467)

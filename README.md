# This is a Advisor Selection System written in django

## Quick Start (Linux / OS X)

### Install pip

```shell
curl -O https://bootstrap.pypa.io/get-pip.py && python get-pip.py
```

### Install Django

```shell
pip install django
```

### Install Virtual Environment of Python

```shell
pip install virtualenv
```

### Create project root directory

```shell
mkdir -p $Workspace/mysite
cd $Workspace/mysite
```

### Setup Python venv

```shell
virtualenv venv && . ./venv/bin/activate
```

### Setup project
#### Create a Django project
```shell
django-admin startproject mysite
```
And then you can go into the root directory of mysite, playing with manage.py with commands like `python manage.py runserver`.

#### Use the Django project in this repo
```shell
git clone https://github.com/chaopli/advisor-selection
```
And then you can use `python manage.py runserver` to start the Django http server locally.

After the server is started successfully, you can use any browser, use `http://localhost:8000` to test the site.

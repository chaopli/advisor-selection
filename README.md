# Advisor Selection System 
## Introduction
This is an advisor selection system I was asked to build from a friend, though was not used in production eventually. I learned many web development knowledge from this project. The main source of the knowledge is from the Django official [tutorial](https://docs.djangoproject.com/en/1.9/contents/). As you can see the app in this project has the same name as it is in the tutorial, but the functionality is quite different.

## Project Overview
This project is very simple in functionality. The administrator creates users for students, and create information for advisors. Students could log into the website with the username and password assigned to them by default. Each advisor could take at most 5 students. The full advisors and available advisors could be shown separately.
I am no web dev expert and I don't know much principals in developing web service, so there are many security issue and many bugs in this project. But personaly I think it's a good start for people who has no experience in full stack development at all before and want to dive in.

## Prerequisites
- Python
- pip
- virtualenv
- Django

## Quick Start (Linux / OS X)

### Install pip
A lot of tools we will use can be installed from pip, which is a package management tools for python. To install pip, use the following command.

```shell
[sudo] curl -O https://bootstrap.pypa.io/get-pip.py && python get-pip.py
```

### Install Virtual Environment of Python
To config a development environment for Django project, we often create a virtual environment for isolation purpose. First, we use `pip` to install `virtualenv` for python

```shell
pip install virtualenv
```

Next, we will start creating our project.

### Create project root directory
First, create a directory for our project, and change into it.

```shell
mkdir -p $Workspace/mysite
cd $Workspace/mysite
```

### Setup Python venv
Within this directory, we will create our python virtual environment with the following command.

```shell
virtualenv venv && . ./venv/bin/activate
```

Once the virtual environment has been activated successfully, you will see the name of the venv at the beginning of your command line.
### Install Django
Now we can install Django within the virtual environment we just created and activated.

```shell
pip install django
```

### Setup project
#### Create a Django project

```shell
django-admin startproject mysite
```

And then you can go into the root directory of mysite, playing with manage.py with commands like `python manage.py runserver`.

#### Use the Django project in this repo
##### Clone the repository

```shell
git clone https://github.com/chaopli/advisor-selection
```

##### Migrate database
In the root directory of our project, which has the `manage.py` file, we can migrate our database with the following command.

###### Migrate Django models

```shell
python manage.py migrate
```

###### Migrate our models

```shell
python manage.py makemigrations polls
python manage.py migrate 
```

Each time we make changes to our polls.models, we need to use `python manage.py makemigrations polls` to update the database.
Then django will parse our `model` modules to create corresponding schema, table, etc.

#### Create a super user
Use the `manage.py` to create a super user with `python manage.py createsuperuser`. You will be prompted to set the username and password.

#### Run the Django server locally
Finally, you can use `python manage.py runserver` to start the Django http server locally.

After the server is started successfully, you can use any browser, use `http://localhost:8000` to test the site.
To log into the admin page for your project, use `http://localhost:8000/admin` with the super user you just created.

### Deploy on openshift
This project has been deployed on openshift successfully. You can try registering for a account. One account can be used to create at most three projects.
Once you created a project, you will be provided with a git url. You can add that git url to your local git remote url and push your repo to that url.
Your project will be deployed automatically on openshift.

# a Advisor Selection System written in Django
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

### Install Django

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
```shell
python manage.py migrate
```
Then django will parse our `model` modules to create corresponding schema, table, etc.

##### Run the Django server locally
Finally, you can use `python manage.py runserver` to start the Django http server locally.

After the server is started successfully, you can use any browser, use `http://localhost:8000` to test the site.

############################# ِDjango installation ##############################

import os
from time import sleep

from django.db import models


def django_install():
    create_virtual_env = 'python -m venv 11_env'
    # activate_enviroment_linux_mac = 'source ll_env/bin/activate'
    activate_enviroment_windows = 'll_env\Scripts\\activate'
    install_django = 'pip install Django'
    commands = [create_virtual_env, activate_enviroment_windows, install_django]
    for command in commands:
        os.system(f'cmd /c "{command}"')
        sleep(0.5)


# django_install()

############################# Create a project #######################################
project_dir = 'project_dir_name'

project_name = "Custom_project_name"

app_name = 'Custom_app_name'


def create_django_project(project_name, app_name):
    create_project = f'django-admin startproject {project_name}'
    # example command : django-admin startproject calcApp
    create_app = f'python manage.py startapp {app_name}'
    create_database = 'python manage.py migrate'
    create_project_commands = [create_app, create_database]
    # os.mkdir(project_dir)
    # os.system(f'cmd /c "cd {project_dir}"')
    os.system(f'cmd /c "{create_project}"')
    for command in create_project_commands:
        os.system(f'cmd /c "cd {project_name} & {command}"')


# create_django_project(project_name=project_name, app_name=app_name)


##################################### add wanted files and app directories ###################
def add_files_and_dirs(project_name, app_name):
    open(f'{project_name}/{app_name}/urls.py', 'w')
    # template and static folder in the app
    os.mkdir(f'{project_name}/{app_name}/templates')
    os.mkdir(f'{project_name}/{app_name}/static')


# url file in the apps
# add_files_and_dirs(project_name=project_name, app_name=app_name)

##################################### MODELS ################################################

class ExampleModel(models.Model):
    '''
    this is and example model
    it could have some fields
    '''
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# with open(f'{project_name}/{project_name}/settings.py', 'w+') as f:
#     setting = ""
#     for line in f.readlines():
#         this_line = ""
#         if line.rstrip() == 'INSTALLED_APPS = [':
#             this_line += f'INSTALLED_APPS = [ \n ' \
#                    f'\t"{app_name}"'


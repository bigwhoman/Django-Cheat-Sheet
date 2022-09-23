############################# ِDjango installation ##############################

import os

# from time import sleep
#
# create_virtual_env = 'python -m venv 11_env'
#
# # activate_enviroment_linux_mac = 'source ll_env/bin/activate'
#
# activate_enviroment_windows = 'll_env\Scripts\\activate'
#
# install_django = 'pip install Django'
#
# commands = [create_virtual_env, activate_enviroment_windows, install_django]
#
# for command in commands:
#     os.system(f'cmd /k "{command}"')
#     sleep(2)

############################# Create a project #######################################
project_dir = 'project_dir_name'

project_name = "Custom_project_name"

create_project = f'django-admin startproject {project_name}'
# example command : django-admin startproject calcApp

app_name = 'Custom_app_name'

create_app = f'python manage.py startapp {app_name}'

create_database = 'python manage.py migrate'

create_project_commands = [create_app, create_database]

# os.mkdir(project_dir)

# os.system(f'cmd /c "cd {project_dir}"')

os.system(f'cmd /c "{create_project}"')

for command in create_project_commands:
    os.system(f'cmd /c "cd {project_name} & {command}"')

##################################### add wanted files and app directories ###################

# url file in the apps 
open(f'{project_name}/{app_name}/urls.py', 'w')

# template and static folder in the app
os.mkdir(f'{project_name}/{app_name}/templates')
os.mkdir(f'{project_name}/{app_name}/static')

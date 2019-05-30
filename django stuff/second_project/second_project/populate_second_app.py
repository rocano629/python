import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','second_project.settings')

import django
django.setup()


##FAKE POP SCRIPT

import random
from second_app.models import User
from faker import Faker

fakegen =  Faker()



def populate(N=5):

    for entry in range(N):
       
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        us = User.objects.get_or_create(FirstName = fake_name,LastName = fake_last_name,Email = fake_email)[0]


if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("population complete!")


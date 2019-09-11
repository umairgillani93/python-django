import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings') # setting the environment

import django
django.setup() # set up the django to start populating the database

from appTwo.models import User # importing the model to be populated with fake data
from faker import Faker # importing faker to add fake data with

fakegen = Faker()

def populate(N = 5):

    for entry in range(N):

        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        # New Entry
        user = User.objects.get_or_create(first_name = fake_first_name,
                                          last_name = fake_last_name,
                                          email = fake_email)[0] # this will return tuple, and we need that first 0th index of tuple
if __name__ == '__main__':
    print('POPULATING THE DATABASE!')
    populate(20)
    print('COMPLETE!')

# Now we'll go ahead and this file 'populate_users.py' we just created!

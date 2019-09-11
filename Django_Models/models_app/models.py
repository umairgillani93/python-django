from django.db import models

# Create your models here.
class Topic(models.Model): # Name of table inside data base
    top_name = models.CharField(max_length = 264, unique = True) # columns inside data base

    def __str__(self):
        return self.top_name # string representation of the table

class Webpage(models.Model): # table name
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE) # table column inherited from 'Topic' class
    name = models.CharField(max_length = 264)
    url = models.URLField(unique = True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete = models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

class Handle_urls(models.Model):


# In order to populate our database with the models we just created
# we need to run the following commands in terminal
# 1. python manage.py migrate
# 2. python manage.py makemigrations
# 3. python manage.py migrate (make sure that before applying the commands
# you are in main project directory. In my case it's Django_Models)

# Now that we have set the models and populated our data base,
# Let's go ahead and connect with our data base!

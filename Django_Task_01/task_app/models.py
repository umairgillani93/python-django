from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 1))

    #def __init__(self, question_text, pub_date):
        #self.question_text = question_text
        #self.pub_date = pub_date

    def __repr__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length = 300)
    votes = models.IntegerField(default = 0) # think of it as interger field
    question = models.ForeignKey(Question, on_delete = models.CASCADE)

    #def __init__(self, choice_text, votes, question):
        #self.choice_text = choice_text
        #self.question = question
        #self.votes = votes

    def __repr__(self):
        return self.choice_text

class Student(models.Model):
    name = models.CharField(max_length = 64)
    age = models.IntegerField()

# class Parent(models.Model):
    # parent_name = models.CharField(max_length =64)
    # parent_id = models

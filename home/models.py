from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    household = models.CharField(max_length=200,default=('what is the name of your pastor'))
    redemmed = models.CharField(max_length=200,default=('what is the name of your pastor'))
    mountain = models.CharField(max_length=200,default=('what is the name of your pastor'))
    christ = models.CharField(max_length=200,default=('what is the name of your pastor'))
    apostolic = models.CharField(max_length=200,default=('what is the name of your pastor'))
    pub_date = models.DateTimeField('date published')


    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


    


from django.db import models
from django.utils import timezone

class user(models.Model):
    username = models.CharField(max_length=20)
    email_id = models.EmailField(max_length=30)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name+'---'+self.email_id

class Questions(models.Model):
    Question_id = models.ForeignKey('user', on_delete= models.CASCADE)
    ans = models.ManyToManyField('Answers')
    Question = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.Question

class Answers(models.Model):
    ans_id =models.ForeignKey('user', on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return str(self.answer)
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f'{self.question_text}'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.question.question_text} - {self.choice_text} - {self.votes}'

class Cat(models.Model):
    cat_name = models.CharField(max_length=200)
    cat_type = models.CharField(max_length=200)
    cat_age = models.CharField(max_length=200)
    cat_gender = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.cat_name} - {self.cat_type} - {self.cat_age} - {self.cat_gender}'
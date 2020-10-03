from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f'{self.question_text}'

#################################################################################################################

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.question.question_text} - {self.choice_text} - {self.votes}'

#################################################################################################################

class top10cat(models.Model):
    Cat_Species = models.CharField(max_length=100) #สายพันธุ์
    CS_information = models.CharField(max_length=500)

    General_appearance_and_behavior = models.CharField(max_length=100) #ลักษณะและพฤติกรรมทั่วไป
    Gaab_information = models.CharField(max_length=500)

    husbandry = models.CharField(max_length=100) #การดูแล
    h_information = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.Cat_Species} - {self.CS_information} - {self.General_appearance_and_behavior} - {self.Gaab_information} - {self.husbandry} - {self.h_information}'

#################################################################################################################
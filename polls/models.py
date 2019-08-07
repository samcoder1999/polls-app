from django.db import models
class question(models.Model):
   question_text=models.CharField(max_length=400)
   pub_date=models.DateTimeField('date:')
class choice(models.Model):
   question=models.ForeignKey(question, on_delete=models.CASCADE)
   choice= models.CharField(max_length=200)
   votes=  models.IntegerField(default=0)
# Create your models here


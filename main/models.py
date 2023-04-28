from django.db import models


class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=256)
    number = models.BigIntegerField()
    secret_answer = models.CharField(max_length=300, null=True)
    sign_date = models.DateTimeField(auto_now_add=True)

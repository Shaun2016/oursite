from django.db import models

# Create your models here.
from django.forms import ModelForm


class User(models.Model):
    nickname = models.CharField(max_length=200)
    phone = models.CharField(max_length=11)
    password = models.CharField(max_length=20)

    def __str__(self):
        return 'nick_name:' + self.nickname + ', phone:' + self.phone


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['nickname', 'phone', 'password']
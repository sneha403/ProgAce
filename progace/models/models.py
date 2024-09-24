from django.db import models
from django.contrib.auth.models import AbstractUser

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.country.name}'

class AgeGroup(models.Model):
    age_group_code = models.CharField(max_length=10, unique=True)
    age_group_name = models.CharField(max_length=50)
    age_range = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.age_group_name} ({self.age_range})'

class Subject(models.Model):
    subject_code = models.CharField(max_length=10, unique=True)
    subject_name = models.CharField(max_length=50)

    def __str__(self):
        return self.subject_name

class Question(models.Model):
    question_text = models.TextField()
    age_group = models.ForeignKey(AgeGroup, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    option_4 = models.CharField(max_length=255)
    correct_answer = models.IntegerField()

    def __str__(self):
        return f'Question: {self.question_text[:50]}...'

    def get_correct_option(self):
        return getattr(self, f'option_{self.correct_answer}')

class User(AbstractUser):
    username = None 
    email = models.EmailField(unique=True) 

    age_group = models.ForeignKey('AgeGroup', on_delete=models.CASCADE, null=True, blank=True)
    school = models.CharField(max_length=100, null=True, blank=True)
    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True, blank=True)
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = []  

    def __str__(self):
        return f'{self.email} - {self.school}, {self.city}, {self.country}'

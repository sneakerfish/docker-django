from django.db import models

# Create your models here.
class Office(models.Model):
    code = models.CharField(max_length=1, db_index=True)
    name = models.CharField(max_length=30)

class StateOffice(models.Model):
    code = models.CharField(max_length=3, db_index=True)
    name = models.CharField(max_length=30)

class Party(models.Model):
    code = models.CharField(max_length=4, db_index=True)
    name = models.CharField(max_length=100)

class State(models.Model):
    code = models.CharField(max_length=2, db_index=True)
    name = models.CharField(max_length=30, db_index=True)
    area = models.CharField(max_length=30)
    year = models.CharField(max_length=4, null=True)

class Candidate(models.Model):
    num = models.CharField(max_length=2,

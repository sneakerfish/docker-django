from django.db import models

# Create your models here.
class Office(models.Model):
    code = models.CharField(max_length=1, db_index=True)
    name = models.CharField(max_length=40)

class StateOffice(models.Model):
    code = models.CharField(max_length=3, db_index=True)
    name = models.CharField(max_length=40)

class Party(models.Model):
    code = models.CharField(max_length=4, db_index=True)
    name = models.CharField(max_length=100)

class State(models.Model):
    code = models.CharField(max_length=2, db_index=True)
    name = models.CharField(max_length=40, db_index=True)
    area = models.CharField(max_length=40)
    year = models.CharField(max_length=4, null=True)

class Candidate(models.Model):
    num = models.CharField(max_length=2)
    year = models.CharField(max_length=4, null=True)
    state_code = models.CharField(max_length=2, db_index=True)
    office_code = models.CharField(max_length=3, db_index=True)
    district_no = models.CharField(max_length=3, null=True)
    asterisk = models.CharField(max_length=1, null=True)
    candidate_vote = models.CharField(max_length=8, null=True)
    election_month = models.CharField(max_length=2, null=True)
    election_type = models.CharField(max_length=1, null=True)
    party_code = models.CharField(max_length=4, db_index=True, null=True)
    name = models.CharField(max_length=50, db_index=True)

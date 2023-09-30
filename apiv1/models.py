from django.db import models


class TestData(models.Model):
    testname = models.CharField(max_length=100)
    testvalue = models.IntegerField()

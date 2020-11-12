from django.db import models


class randomobjects(models.Model):
	name = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	age = models.IntegerField()



from django.db import models
import mysql.connector

# Create your models here.

class smovie(models.Model):
	name=models.CharField(max_length=30)
	link=models.CharField(max_length=50)
	body=models.CharField(max_length=200)
	def __str__(self):
		return self.name
	class Meta:
		db_table='movies'
	# def __str__(self):
        # return self.name
	# class Meta:
        # db_table = 'movies'
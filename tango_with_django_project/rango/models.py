from django.db import models
import datetime
from django.utils import timezone

# taken from the django tutorials

'''
This just makes a little question thing. Then it takes answers.
So am I to believe that this will create a little SQL Database with these as the data models?
If so, how do I declare something a primary key? I don't know.
More generally, what if I want to set up my own SQL Database
on my terms. How do I do that? 
Remember to come back to this.
Also I prefer camelcase to _
'''

#Inheritance in python looks sort of like taking an argument. Remember that Akira.
#Also every model has to inherit from models.Model. Not sure why.
class Topic(models.Model):
	name = models.CharField(max_length=128, unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)

	def __unicode__(self):
		return self.name

class Site(models.Model):
	topic = models.ForeignKey(Topic)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)

	def __unicode__(self):
		return self.title
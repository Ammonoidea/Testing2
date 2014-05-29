from django.db import models

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
class Question(models.Model):
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published') #'date published' is the human readable name, optional argument.

class Decision(models.Model):
	question = models.ForeignKey(Question) #So could I do models.PrimaryKey? Do they have GUID support?
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default = 0)

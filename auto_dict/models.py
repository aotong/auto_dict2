from django.db.models import (
	Model, 
	CharField, 
	TextField,
	ForeignKey
)
from django.contrib.auth.models import User



# Create your models here.
class Word(Model):
    word = CharField(max_length=160,default="No Word Entry")
    definition = TextField(default="No Example Entry")
    
    def __str__(self):
        return self.word


# Create your models here.
class Sentence(Model):
    sentence = TextField(default="No Sentence Entry")
    user = ForeignKey(User, null=True, blank=True)

    def __str__(self):
        return self.sentence


class Translation(Model):
    sentence = ForeignKey('Sentence', null=True, blank=True)
    translation = TextField()
    user = ForeignKey(User, null=True, blank=True)
    
    def __str__(self):
        return self.translation
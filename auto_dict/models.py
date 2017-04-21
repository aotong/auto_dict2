from django.db.models import (
	Model, 
	CharField, 
	TextField
)


# Create your models here.
class Word(Model):
    word = CharField(max_length=160,default="No Word Entry")
    definition = TextField(default="No Example Entry")
    
    def __str__(self):
        return self.word

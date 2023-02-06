from django.db import models

class Team (models.Model):

    name = models.CharField(max_length=30)
    titles = models.PositiveBigIntegerField(default=0,null=True)
    top_scorer = models.CharField(max_length=50)
    fifa_code = models.CharField(max_length=3, unique=True)
    first_cup = models.DateField(null=True)
    
    def __repr__(self):
        
        id = self.id
        nome = self.name
        codigo = self.fifa_code

        retorno = f"<[{id}] {nome.title()} - {codigo.upper()}>"

        return retorno
         



# Create your models here.

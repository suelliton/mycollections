from django.db import models
from django import forms

class Usuario(models.Model):
    nome = models.CharField(blank=False, null=False,max_length=30,default="")  # This field type is a guess.
    id = models.IntegerField(primary_key=True, blank=True, null=False)  # AutoField?
    senha = models.CharField(blank=False, null=False,max_length=30,default="")  # This field type is a guess.
    email = models.EmailField(max_length=254,null=False,blank=True)
    
    class Meta:
        managed = True
        db_table = 'Usuario'
    

class Usuario_temp(models.Model):
    nome = models.CharField(blank=False, null=False,max_length=30,default="")  # This field type is a guess.
    id = models.IntegerField(primary_key=True, blank=True, null=False)  # AutoField?
    senha = models.CharField(blank=False, null=False,max_length=30,default="")  # This field type is a guess.
    email = models.EmailField(max_length=254,null=False,blank=True)
    class Meta:
        managed = True
        db_table = 'Usuario_temp'
   



class Video(models.Model):
    id = models.IntegerField(primary_key=True, blank=True, null=False)  # AutoField?
    id_usuario = models.IntegerField(null = False, default=0)
    nome = models.CharField(max_length=50,default='')
    url = models.CharField(blank=True, null=True,max_length=1000)  # This field type is a guess.

    Forro = 'Forró'
    Rock =  'Rock'
    Pop = 'Pop'
    Swingueira = 'Swingueira'
    Eletrohits = 'Eletrohits'
    Sertanejo = 'Sertanejo'
    Palestras = 'Palestras'
    Romântica ='Romântica'
    Outros = 'Outros'
    CHOICES = (
            (Forro, 'Forró'),
            (Rock, 'Rock'),
            (Pop, 'Pop'),
            (Swingueira, 'Swingueira'),
            (Sertanejo,'Sertanejo'),
            (Eletrohits,'Eletrohits'),
            (Romântica,'Romântica'),            
            (Palestras,'Palestras'),
            (Outros,'Outros'),
        )
    categoria = models.CharField(max_length=30,choices=CHOICES,default=Rock)

    class Meta:
        managed = True
        db_table = 'Video'
      



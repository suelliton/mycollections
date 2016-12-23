from django.db import models
from django import forms

class Usuario(models.Model):
    nome = models.CharField(blank=True, null=True,max_length=30)  # This field type is a guess.
    id = models.IntegerField(primary_key=True, blank=True, null=False)  # AutoField?
    senha = models.CharField(blank=True, null=True,max_length=30)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'Usuario'
    def _str_(self):
        return self.id
    def _unicode_(self):
        return self.id


class Video(models.Model):
    id = models.IntegerField(primary_key=True, blank=True, null=False)  # AutoField?
    id_usuario = models.IntegerField(null = False)
    nome = models.CharField(max_length=50,default='')
    url = models.CharField(blank=True, null=True,max_length=1000)  # This field type is a guess.

    Forro = 'Forró'
    Rock =  'Rock'
    Pop = 'Pop'
    Swingueira = 'Swingueira'
    Eletrohits = 'Eletrohits'
    Asmr = 'Asmr'
    Palestras = 'Palestras'
    Romântica ='Romântica'
    CHOICES = (
            (Forro, 'Forró'),
            (Rock, 'Rock'),
            (Pop, 'Pop'),
            (Swingueira, 'Swingueira'),
            (Eletrohits,'Eletrohits'),
            (Romântica,'Romântica'),
            (Asmr,'Asmr'),
            (Palestras,'Palestras'),
        )
    categoria = models.CharField(max_length=30,choices=CHOICES,default=Rock)

    class Meta:
        managed = True
        db_table = 'video'
"""class Categoria(models.Model):
    Forro = 'fr'
    Rock =  'rc'
    Pop = 'pp'
    Swingueira = 'sw'
    CHOICES = (
            (Forro, 'Forró'),
            (Rock, 'Rock'),
            (Pop, 'Pop'),
            (Swingueira, 'Swingueira'),
        )



    nome = models.CharField(max_length=30,choices=CHOICES,default=Rock,)
    id = models.IntegerField(primary_key = True,null=False)
    class Meta:
        managed =True
        db_table = 'categoria'
    def _str_(self):
        return self.nome

    def is_upperclass(self):
        return self.nome in (self.Rock, self.Forro,self.Pop,self.Swingueira)
"""

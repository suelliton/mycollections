from django import forms
from .models import Usuario, Video

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nome', 'senha',)
       

class VideoForm(forms.ModelForm):
    #cat = forms.ModelChoiceField(queryset= Categoria.objects.all())    
    class Meta:
        model = Video
        fields = ('url','categoria',)

class UsuarioCadastroForm(forms.ModelForm):
	rsenha = forms.CharField(max_length = 20)
	class Meta:
		model = Usuario 
		fields = ('nome','senha','rsenha')       

from django.shortcuts import render
from django import forms
from .models import Usuario, Video
from .forms import UsuarioForm, VideoForm, UsuarioCadastroForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
import requests
from bs4 import BeautifulSoup


def login(request):
    if request.method == 'POST':            #se o metodo for post
        form = UsuarioForm(request.POST)    #pega o form que chegou
        if form.is_valid():                 # se o formulario for valido
            logado = form.save(commit=False)     #pega o objeto usuario que veio no post
            usuarios = Usuario.objects.all()    #pega todos usuarios cadastrados no banco
            for usu in usuarios:                #percorre os usuarios
                if usu.nome == request.POST['nome'] and usu.senha == request.POST['senha']: # verifica senha e usuario são validos                    
                    request.session['id_logado'] = usu.id   #se o usuario for valido seta o id do usuario_logado na sessão
                    request.session['usuario_logado'] = usu.nome
                    return HttpResponseRedirect("index")  #chama o index
                else:# se não achar não faz nada passa direto
                    pass
            mensagem = "Usuário ou senha inválido"        
            return render(request,"collection_app/login.html",{'mensagem':mensagem, 'form':form}) # se não achar o usuario limpa o formulario
    else:   # se o metodo or GET
        if request.session.get('id_logado'):    #se tiver um usuario logado
            return HttpResponseRedirect("index")  #chama o index
        else: # se não tiver usuario logado
            form = UsuarioForm() # cria um form limpo
            return render(request,"collection_app/login.html",{'form':form}) # chama o logim passando o form limpo

def logout(request):
    try:
        del request.session['id_logado']
        del request.session['usuario_logado']
    except KeyError:
        pass
    form = UsuarioForm()
    return HttpResponseRedirect("http://localhost:8000/")#apos ologout retorna pro login

def index(request):
    videos = []
    if request.session.get('id_logado'):#se tiver usuario logado
        id_logado = request.session.get('id_logado')
        usuario_logado = request.session.get('usuario_logado')
        if request.method == 'GET':
            videos = Video.objects.filter(id_usuario = id_logado)#pega todos videos do banco do usuario q esta logado
            form = VideoForm()
            return render(request,"collection_app/index.html",{'usuario_logado':usuario_logado,'videos':videos,'form':form})
        else:
            form = VideoForm(request.POST)
            if form.is_valid():
                 video = form.save(commit=False)
                 link = "https://www.youtube.com/watch?v="+str(video.url)
                 video.nome = getTitulo(link)
                 embed = "https://www.youtube.com/embed/"+str(video.url)
                 video.url = embed
                 video.id_usuario = id_logado
                 video.save()
                 videos = Video.objects.filter(id_usuario = id_logado)
                 form = VideoForm()
        return render(request,"collection_app/index.html",{'usuario_logado':usuario_logado,'videos':videos,'form':form})


    else:#se não tiver logado
        form = UsuarioForm()
        return render(request,"collection_app/login.html",{'form':form})


def getTitulo(url):
    req = requests.get(url)
    html = BeautifulSoup(req.text, "html.parser")
    entradas = html.find_all('span',{'class':'watch-title'})
    return entradas[0].getText()

def excluirVideo(request):
    pk =request.GET['pk']
    Video.objects.filter(id=pk).delete()
    return HttpResponseRedirect('http://localhost:8000')

def filtraVideo(request):
    cat = request.GET['cat']
    id_logado = request.session.get('id_logado')
    usuario_logado = request.session.get('usuario_logado')
    videos = Video.objects.filter(categoria = cat, id_usuario = id_logado)
    form = VideoForm()
    return render(request,"collection_app/index.html",{'usuario_logado':usuario_logado,'videos':videos,'form':form})


def cadastra_usuario(request):
    if request.method == 'GET':
        form = UsuarioCadastroForm(request.POST)
        return render(request,"collection_app/cadastra_usuario.html",{'form':form})
    else:
        form = UsuarioCadastroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit = False)
            if usuario.senha == request.POST['rsenha']:
                novo_usuario = Usuario()
                novo_usuario.senha = usuario.senha
                novo_usuario.nome = usuario.nome
                novo_usuario.save()
                form = UsuarioForm()
                return HttpResponseRedirect('http://localhost:8000')           
            else:
                mensagem = "Senhas não coincidem"
                form = UsuarioCadastroForm()
                return render(request,"collection_app/cadastra_usuario.html",{'form':form,'mensagem':mensagem})           





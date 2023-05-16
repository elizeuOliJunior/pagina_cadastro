from django.shortcuts import render
from.models import Usuario

def home (request):
    return render (request , 'usuarios/home.html')

#salvar os dados inseridos no banco de dados
def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    #todos usuarios cadastrados
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    
    #retornar os dados segunda pag
    return render (request , 'usuarios/usuarios.html' , usuarios)
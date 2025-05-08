from django.shortcuts import render, redirect
from usuarios.forms import UsuarioForm
from sistema.models import Usuario

# Create your views here.

def login(request): #request é requisição
    return render(
        request,
        'usuarios/login.html',
    )
    
def mostrarUsuarios(request):
    usuarios = Usuario.objects.all()

    context = {
        'usuarios': usuarios
    }

    return render(
        request,
        'usuarios/listar.html',
        context, 
    )

def criarUsuario(request):
    # Verificar se a requisição será do tipo GET ou POST
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES) # Será criada um objeto Usuario(model) com os dados enviados 
        #POST -> são os campos do forms (nome, sobrenome, etc.) preenchidos
        #FILES -> é para passar as imagens
        
        #Fazendo validação dos forms
        if form.is_valid():
            form.save()
            return redirect('/usuarios/login') #você só vai redirecionar caso o formulário SEJA válido
    
    else:
        # Se a requisição for GET, exibir o formulário de cadastro
        form = UsuarioForm() #mostra o formulário em branco, afinal nenhum 

    return render(
        request,
        'usuarios/cadastro.html',
        {'form': form}
    )


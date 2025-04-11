from django.shortcuts import render

# Aqui irão ficar todas as views (controladores) referente ao sistema 

def index(request): #request é requisição
    return render(
        request,
        'sistema/sistema.html',
    )

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Produto
from django.http import HttpResponse
from django.template import loader

def index(request):
    # print("COMANDO:" + str(request))
    # print(dir(request.user.last_login))
    # print(f"User: {request.user}")
    # print("Último login: " + str(request.user.last_login.day)+"/"+ str(request.user.last_login.month)+"/"+ str(request.user.last_login.year))

    produtos = Produto.objects.all()

    if str(request.user) == 'AnonymousUser':
        logado = 0
        teste = 'Usuário não logado'
    else:
        logado = 1
        teste = 'Usuário logado: ' + request.user.username
        ultimo_login = 'Último login:' + str(str(request.user.last_login.day)+"/"+ str(request.user.last_login.month)+"/"+ str(request.user.last_login.year))

    context = {
        'curso':'Programação Web com Django',
        'livro' : 'Introdução a Python',
        'logado' : teste,
        'ultimo_login' : ultimo_login if logado == 1 else "Sem registro",
        'produtos' : produtos,
    }
    return render(request, 'index.html', context)

def contato(request):
    contextContato = {
        'livro' : 'Bíblia do Django'
    }
    return render(request, 'contato.html', contextContato)


def produto(request, pk):

    #prod = Produto.objects.get(id=pk)

    prod = get_object_or_404(Produto, id=pk)

    context = {
        'produto' : prod
    }

    print('PK:', str(pk))
    return render(request, 'produto.html', context)


def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)

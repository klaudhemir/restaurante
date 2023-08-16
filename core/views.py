from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def view_home(request):
    return render(request, 'home.html')

def pagina_pratos(request):
    # 1 - Pegar a lista de pratos do banco de dados
    pratos = Prato.objects.all()

    # 2 - Renderizar a página passando os pratos para o template
    return render(request, 'pratos.html', {'pratos': pratos})

def pagina_cadastro(request):
    return render(request, "cadastro_pratos.html")

def cadastrar_pratos(request):
    # - receber valores do request e savaldo em variaveis
    Novo_nome = request.POST.get('nome_produto')
    Novo_descriçao = request.POST.get('descriçao_produto')
    Novo_preço = request.POST.get('preço_produto')

    # - Cadastrar o preço no banco de dados
    # - INSERT do SQL
    Prato.objects.create(nome=Novo_nome, descricao=Novo_descriçao, preco=Novo_preço)
    return redirect(pagina_cadastro)

def pagina_cadastro_comanda(request):
    return render(request, "comanda.html")

def cadastro_comanda(request):
    # - receber valores do request e savaldo em variaveis
    Novo_numero = request.POST.get('numero_comanda')
    
    Comanda.objects.create(numero=Novo_numero)
    return redirect(pagina_cadastro_comanda)
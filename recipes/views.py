from django.shortcuts import render
from django.http import HttpResponse #Importação do método Response para poder enviar uma pagina web para a requisição

# Create your views here.

#Forma correta de endereçar uma arquivo HTML. Pasta template padrão
def home(request):  
    return render(request, 'recipes/pages/home.html')
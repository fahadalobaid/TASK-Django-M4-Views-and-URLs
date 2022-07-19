from django.http import HttpResponse

from .models import Pokemon

def get_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    return HttpResponse(pokemon)

def get_pok_list(request) :
    poks = Pokemon.objects.all().values_list("name", flat=True)
    poks_list = "\n".join(f"<li>{pokemon}</li>" for pokemon in poks)
    return HttpResponse({poks_list})




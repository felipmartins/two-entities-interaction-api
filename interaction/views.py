from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from .models import Participant


def check_if_participants_exists(request):
    if request.method == "GET":
        if "alexaid" in request.GET:
            participant = Participant.objects.all().filter(
                alexa_id=request.GET["alexaid"]
            )
            if len(participant) == 0:
                return JsonResponse(
                    {"answer": "Por qual nome você quer que eu te chame?"}
                )
            else:
                return JsonResponse(
                    {
                        "answer": f"Olá {participant[0].name}. Diga: Criar uma conexão caso deseje começar uma conexão. Ou. Diga: Conectar à. e em seguida o número da conexão"
                    }
                )
        else:
            return JsonResponse({"answer": "missing id"})
    else:
        return JsonResponse({"answer": "not found"})


@csrf_exempt
def create_participant(request):
    if request.method == "POST":
        if "alexaid" in request.POST:
            if "name" in request.POST:
                participant = Participant.objects.all().filter(alexa_id=request.POST["alexaid"])

                if len(participant) > 0:
                    return JsonResponse({"answer": f"Já existe um cadastro vinculado ao seu dispositivo Alexa. Ele foi feito no nome de {participant[0].name}. Você pode escolher excluir esse cadastro dizendo: Quero excluir meu cadastro, ou pode iniciar uma conexão, para isso, diga: Criar uma conexão caso deseje começar uma conexão. Ou. Diga: Conectar à. e em seguida o número da conexão"})
                else:
                    participant = Participant(alexa_id=request.POST["alexaid"], name=request.POST["name"])
                    participant.save()
                    return JsonResponse({"answer": f"Olá {participant.name}. Diga: Criar uma conexão caso deseje começar uma conexão. Ou. Diga: Conectar à. e em seguida o número da conexão"})
            else:
                return JsonResponse({"answer": "missing name"})
        else:
            return JsonResponse({"answer": "missing id"})
    else:
        return JsonResponse({"answer": "not found"})


def check_if_connection_exists(request):
    ...


def check_number_of_participants(request):
    ...


def check_whos_turn_is(request):
    ...


def send_message(request):
    ...

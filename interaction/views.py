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
            return JsonResponse({"error": "missing necessary parameter"})


def create_participant(
    request,
):  # recebe via post o alexaid e o nome da pessoa e cria o participante
    if request.method == "POST":
        ...


def check_if_connection_exists(request):
    ...


def check_number_of_participants(request):
    ...


def check_whos_turn_is(request):
    ...


def send_message(request):
    ...

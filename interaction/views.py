from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from .models import Participant, InteractionConnection


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
                participant = Participant.objects.all().filter(
                    alexa_id=request.POST["alexaid"]
                )

                if len(participant) > 0:
                    return JsonResponse(
                        {
                            "answer": f"Já existe um cadastro vinculado ao seu dispositivo Alexa. Ele foi feito no nome de {participant[0].name}. Você pode escolher excluir esse cadastro dizendo: Quero excluir meu cadastro, ou pode iniciar uma conexão, para isso, diga: Criar uma conexão caso deseje começar uma conexão. Ou. Diga: Conectar à. e em seguida o número da conexão"
                        }
                    )
                else:
                    participant = Participant(
                        alexa_id=request.POST["alexaid"], name=request.POST["name"]
                    )
                    participant.save()
                    return JsonResponse(
                        {
                            "answer": f"Olá {participant.name}. Diga: Criar uma conexão caso deseje começar uma conexão. Ou. Diga: Conectar à. e em seguida o número da conexão"
                        }
                    )
            else:
                return JsonResponse({"answer": "missing name"})
        else:
            return JsonResponse({"answer": "missing id"})
    else:
        return JsonResponse({"answer": "not found"})


def check_if_connection_exists(request):
    if request.method == "GET":
        if "alexaid" in request.GET:

            if "pin" in request.GET:
                participant = Participant.objects.all().filter(
                    alexa_id=request.GET["alexaid"]
                )
                if len(participant) == 0:
                    return JsonResponse(
                        {
                            "answer": "Você só pode criar, ou entrar, em uma conexão se estiver com seu cadastro em dia. Como você quer que eu te chame?"
                        }
                    )
                else:
                    con = InteractionConnection.objects.all().filter(
                        pin=request.GET["pin"]
                    )
                    participant = participant[0]
                    if len(con) > 0:
                        con = con[0]
                        if len(con.participants) > 1:
                            return JsonResponse(
                                {
                                    "answer": "Essa conexão está cheia. Diga: Criar uma conexão caso deseje começar uma conexão. Ou. Diga: Conectar à. e em seguida o número da conexão"
                                }
                            )
                        else:
                            con.participants["two"] = participant.alexa_id
                            con.connection_status = "Conexão estabelecidada"
                            con.save()
                            return JsonResponse(
                                {
                                    "answer": "Conexão estabelecida, podemos começar a comunicação"
                                }
                            )
                    else:
                        return JsonResponse(
                            {
                                "answer": f"Olá {participant.name}, a conexão na qual você está tentando entrar não existe, tente novamente"
                            }
                        )
            else:
                return JsonResponse({"answer": "missing pin"})
        else:
            return JsonResponse({"answer": "missing id"})
    else:
        return JsonResponse({"answer": "not found"})

@csrf_exempt
def create_connection(request):
    if request.method == "POST":
        if "alexaid" in request.POST:
            
            participant = Participant.objects.all().filter(
                    alexa_id=request.POST["alexaid"]
            )

            if len(participant) == 0:
                return JsonResponse(
                    {
                        "answer": "Você só pode criar, ou entrar, em uma conexão se estiver com seu cadastro em dia. Como você quer que eu te chame?"
                    }
                )
            else:
                participant = participant[0]
                con = InteractionConnection(connection_status="Aguardando participantes",participants={"one":participant.alexa_id},turn=participant)
                con.save()
                return JsonResponse({"answer": f"Conexão criada com sucesso, aguardando outra pessoa para começar. O pin para conexão é {con.pin}"})
        else:
            return JsonResponse({"answer": "missing id"})
    else:
        return JsonResponse({"answer": "not found"})


def check_number_of_participants(request):
    ...


def check_whos_turn_is(request):
    ...


def send_message(request):
    ...

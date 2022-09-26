from django.shortcuts import render


def check_if_participants_exists(
    request,
):  # verifica se existe e caso exista retorna mensagem de sucesso e pedido de número
    if (
        request.method == "GET"
    ):  # para conexão, caso contrário, pede para a pessoa dizer seu nome para criar a pessoa participante;
        ...


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

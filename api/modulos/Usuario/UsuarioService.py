from django.contrib.auth.models import User


def criar_usuario(usuario):
    validacao_usuario = validar_usuario(usuario)
    if (validacao_usuario != None): return validacao_usuario
    user = User.objects.create(username=usuario['cpf'])
    user.set_password(usuario['senha'])
    user.save()
    return None


def deletar_usuario(cpf):
    usuario = User.objects.get(username=cpf)
    usuario.delete()


def validar_usuario(usuario):
    if not validar_cpf(usuario["cpf"]):
        return 'CPF invalido'
    elif User.objects.filter(username=usuario["cpf"]):
        return 'CPF já cadastrado'
    elif usuario['senha'] != usuario['senha2']:
        return 'As senhas não são compativeis'
    else:
        return None


def validar_cpf(cpf: str):
    numbers = [int(digit) for digit in cpf if digit.isdigit()]
    if len(numbers) != 11 or len(set(numbers)) == 1:
        return False
    sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False
    sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False
    return True
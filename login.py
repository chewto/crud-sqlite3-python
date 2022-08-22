from datetime import date, datetime

diccionario_datos = {
    'primer_nombre': '',
    'segundo_nombre': '',
    'primer_apellido': '',
    'segundo_apellido': '',
    'numero_telefono': '',
    'email': '',
    'ci': '',
    'fecha de nacimiento': '',
    'mayor de edad': ''
}


def comprobacion_caracteres(campo_de_texto):
    caracteres_no_permitidos = '!@#$%^&*()_+-=|[]\:";<>?,./1234567890 '
    contador = 0
    for caracter in caracteres_no_permitidos:
        if caracter in campo_de_texto:
            contador += 1
            print(f"el caracter {caracter} es invalido")
    if contador > 0:
        return True
    else:
        return False


def comprobacion_primer_nombre():
    primer_nombre = input("introduce tu primer nombre: ").title()

    if len(primer_nombre) >= 3 or len(primer_nombre) >= 20:
        if comprobacion_caracteres(primer_nombre):
            return False
        else:
            diccionario_datos["primer_nombre"] = primer_nombre
            return True
    else:
        print("primer nombre invalido")
        return False


def comprobacion_segundo_nombre():
    segundo_nombre = input("introduce tu segundo nombre: ").title()

    if len(segundo_nombre) >= 3 or len(segundo_nombre) >= 20:
        if comprobacion_caracteres(segundo_nombre):
            return False
        else:
            diccionario_datos["segundo_nombre"] = segundo_nombre
            return True
    else:
        print("segundo nombre invalido")
        return False


def comprobacion_primer_apellido():
    primer_apellido = input("introduce tu primer apellido: ").title()

    if len(primer_apellido) >= 3 or len(primer_apellido) >= 20:
        if comprobacion_caracteres(primer_apellido):
            return False
        else:
            diccionario_datos["primer_apellido"] = primer_apellido
            return True
    else:
        print("primer apellido invalido")
        return False


def comprobacion_segundo_apellido():
    segundo_apellido = input("introduce tu segundo apellido: ").title()

    if len(segundo_apellido) >= 3 or len(segundo_apellido) >= 20:
        if comprobacion_caracteres(segundo_apellido):
            return False
        else:
            diccionario_datos["segundo_apellido"] = segundo_apellido
            return True
    else:
        print("segundo apellido invalido")
        return False


def comprobacion_numero_telefono():
    numero_telefono = input("introduce tu numero de telefono: ")

    if len(numero_telefono) <= 30:
        if "0424" in numero_telefono or "0414" in numero_telefono or "0412" in numero_telefono or "0426" in numero_telefono or "0416" in numero_telefono:
            diccionario_datos["numero_telefono"] = numero_telefono
            return True
        else:
            print("no es un numero de telefeno movil")
            return False
    else:
        print("el numero no es valido")
        return False


def comprobacion_email():
    correo_electronico = input("introduce tu correo electronico: ").lower()

    if "@" in correo_electronico and ".com" in correo_electronico:
        print("el correo electronico es valido")
        diccionario_datos["email"] = correo_electronico
        return True
    else:
        print("el correo electronico no es valido")
        return False


def comprobacion_CI():
    ci = input("introduce tu numero de cedula: ")

    if ci.isnumeric():
        if len(ci) >= 5 and len(ci) <= 20:
            print("la cedula es valida")
            diccionario_datos["ci"] = ci
            return True
    else:
        print("la cedula tiene que ser numerica")
        return False


def comprobacion_edad():
    fecha_nacimiento_input = input(
        "introduce tu fecha de nacimiento (dd/mm/aa)[el año tiene que ser completo]: ")
    fecha_nacimiento = datetime.strptime(
        fecha_nacimiento_input, '%d/%m/%Y').date()
    fecha_actual = date.today()
    resultado_edad_dias = fecha_actual - fecha_nacimiento
    resultado_edad_dias_str = str(resultado_edad_dias)

    if fecha_nacimiento <= fecha_actual:
        diccionario_datos["fecha de nacimiento"] = fecha_nacimiento_input
        if resultado_edad_dias_str >= "6570 days":
            diccionario_datos["mayor de edad"] = True
            return True
        else:
            diccionario_datos["mayor de edad"] = False
            return True
    else:
        print("la fecha es invalida")
        return False


def login():
    while(True):
        if comprobacion_primer_nombre() == True:
            print("\n")
            break

    while(True):
        if comprobacion_segundo_nombre() == True:
            print("\n")
            break

    while(True):
        if comprobacion_primer_apellido() == True:
            print("\n")
            break

    while(True):
        if comprobacion_segundo_apellido() == True:
            print("\n")
            break

    while(True):
        if comprobacion_numero_telefono() == True:
            print("\n")
            break

    while(True):
        if comprobacion_email() == True:
            print("\n")
            break

    while(True):
        if comprobacion_CI() == True:
            print("\n")
            break

    while(True):
        if comprobacion_edad() == True:
            print("\n")
            break

    return diccionario_datos

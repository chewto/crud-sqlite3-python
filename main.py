from crud import create, read, read_all, update, delete
from login import *


def main():
    option = 0

    while option != 6:

        option = int(input('1-para crear un usuario, pulse 1\n2-para buscar un usuario, pulse 2\n3-para ver a todos los usuarios en la base de datos, pulse 3\n4-para actualizar un usuario, pulse 4\n5-para eliminar un usuario, pulse 5\n6-para salir del programa, pulse 6\nque desea hacer?: '))
        if option == 1:
            login()

            first_name = diccionario_datos['primer_nombre']
            second_name = diccionario_datos['segundo_nombre']
            first_last_name = diccionario_datos['primer_apellido']
            second_last_name = diccionario_datos['segundo_apellido']
            phone_number = diccionario_datos['numero_telefono']
            email = diccionario_datos['email']
            ci = diccionario_datos['ci']
            fecha_nacimiento = diccionario_datos['fecha de nacimiento']
            mayoria_edad = diccionario_datos['mayor de edad']

            create(first_name, second_name, first_last_name, second_last_name,
                   phone_number, email, ci, fecha_nacimiento, mayoria_edad)

        elif option == 2:
            first_name_search = input(
                'introduzca el nombre del usuario que desea buscar: ').title()
            ci_search = input(
                'introduzca la ceula del usuario que desea buscar: ')

            if read(first_name_search, ci_search):
                print('usuario encontrado')
            else:
                print('no se ha encontrado el usuario')

        elif option == 3:
            read_all()

        elif option == 4:

            old_first_name = input(
                'introduzca el nombre del usuario a actualizar: ').title()
            old_ci = input(
                'introduzca la cedula del usuario a actualizar: ').title()

            print('ahora introduzca los nuevos datos')

            login()

            new_first_name = diccionario_datos['primer_nombre']
            new_second_name = diccionario_datos['segundo_nombre']
            new_first_last_name = diccionario_datos['primer_apellido']
            new_second_last_name = diccionario_datos['segundo_apellido']
            new_phone_number = diccionario_datos['numero_telefono']
            new_email = diccionario_datos['email']
            new_ci = diccionario_datos['ci']
            new_fecha_nacimiento = diccionario_datos['fecha de nacimiento']
            new_mayoria_edad = diccionario_datos['mayor de edad']

            update(new_first_name, new_second_name, new_first_last_name,
                   new_second_last_name, new_phone_number, new_email, new_ci, new_fecha_nacimiento, new_mayoria_edad, old_first_name, old_ci)

        elif option == 5:
            first_name_del = input(
                'introduzca el nombre del usuario que deses eliminar: ').title()

            first_last_name_del = input(
                'introduzca el apellido del usuario que deses eliminar: ').title()

            email_del = input(
                'introduzca el email del usuario que deses eliminar: ').lower()

            ci_del = input(
                'introduzca la cedula del usuario que deses eliminar: ')

            delete(first_name_del, first_last_name_del, email_del, ci_del)

        elif option == 6:
            break

        else:
            print('la opcion no esta disponible')


if __name__ == '__main__':
    main()

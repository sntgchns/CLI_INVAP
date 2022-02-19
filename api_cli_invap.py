#!/usr/bin/env python
import click, requests


click.echo('Bienvenido a la API de INVAP.')

@click.group()
def apiinvap():
    pass

@click.command(name='invap', help='Obtener datos de INVAP.')
def obtener_dato():
    def cerrar_programa():
        programa = click.prompt('Desea realizar otra consulta? (s/n)', type=str, default='s')
        if programa == 's' or programa == 'S':
            apiinvap()
        else:
            print('Gracias por utilizar la API de INVAP.')
    click.echo('Para obtener datos, ingrese el nombre de la ruta: ')
    resultado_rutas = requests.get('https://invap.herokuapp.com/').json()
    click.echo(resultado_rutas[1])
    ruta = click.prompt('Ingrese la ruta', type=str)
    resultado_ruta = requests.get('https://invap.herokuapp.com/{}'.format(ruta)).json()
    click.echo(list(resultado_ruta[ruta.capitalize()]))
    valor = click.prompt('Ingrese el dato a buscar', type=str)
    click.echo(resultado_ruta[ruta.capitalize()][valor])
    cerrar_programa()

apiinvap.add_command(obtener_dato)

if __name__ == '__main__':
    apiinvap()
1) api_cli_invap.py:

para obtener datos ingresar:

    $ api_cli_invap.py invap

Aparecerán las rutas disponibles para navegar por terminal.
Luego, al ingresar el nombre de la ruta se obtienen los datos del diccionario de esa ruta.
Para obtener el valor buscado ingrese el dato mostrado en pantalla.


2) api_cli_directo_invap.py:

el uso es similar, pero se pasan los comandos directamente.

api_cli_directo_invap.py buscar ruta <ruta_a_obtener> -v <dato_a_buscar>

ejemplos:

        $ api_cli_directo_invap.py buscar ruta nuclear -v reactores_de_investigacion

    Se obtienen datos de los reactores de investigación desarrollados por INVAP.

        $ api_cli_directo_invap.py buscar ruta social -v instagram
    
    Se obtiene el link al Instagram de INVAP.

Para navegar en la web se puede ingresar en https://invap.herokuapp.com/

Desarrollo en Python, Flask, mongoDB Atlas y Heroku.
#   PROYECTO DEL SEPTIMO SRPINT
## INTRODUCCIÓN A LA AUTOMATIZACIÓN DE PRUEBAS. 
TESTS DE PRUEBAS PARA EL PARAMETRO NAME EN LA CREACIÓN DEL KIT.

>>      SEDANO SANCHEZ KARLA GUADALUPE.
## Requisitos previos

- Instalar librerias pytest y requests:
  > > pip3 install pytest  
  > > pip3 install requests
- o instalar desde requests.txt
  > > pip3 install -r requirements.txt


## Formas de ejecutar las pruebas
1.  python3 -m pytest <Path-to-test-file>.py -vv -s
2.  Ejecución por medio del IDE


## DESCRIPCIÓN DEL PROYECTO

En el proyecto del Sprint 7 se realizaron nueve pruebas de una lista de comprobación enviando una solicitud para crear un kit personal, probando el parametro "name".

DESCRIPCIONES DE LAS PRUEBAS.
- El número permitido de caracteres (1): kit_body = { "name": "a"} Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud

- El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"} Código de respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud

- El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" } Código de respuesta: 400

- El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” } Código de respuesta: 400

- Se permiten caracteres especiales: kit_body = { "name": ""№%@"," } Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud

- Se permiten espacios: kit_body = { "name": " A Aaa " } Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud

- Se permiten números: kit_body = { "name": "123" } Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud

- El parámetro no se pasa en la solicitud: kit_body = { } Código de respuesta: 400

- Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 } Código de respuesta: 400
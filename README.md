#   PROYECTO DEL SEPTIMO SRPINT
## AUTOMATIZACIÓN DE PRUEBAS DE LA API DE LA APLICACIÓN "URBAN GROCERS". 


>>      SEDANO SANCHEZ KARLA GUADALUPE.
 
## DESCRIPCION DEL PROYECTO

En el sector de e-commerce, la confiabilidad y eficiencia de las APIs son fundamentales para garantizar una experiencia fluida para los usuarios. **Urban.Grocers** está actualizando su back-end, incorporando nuevas funcionalidades para mejorar la gestión de pedidos y la disponibilidad del servicio de entrega. Para garantizar que estos cambios sean robustos y sin errores, se requiere un proceso de prueba riguroso que valide cada test para el parametro name de la creación del kit de la API antes de su implementación.

## TECNOLOGÍAS UTILIZADAS

* Herramientas :

- Python para scripting.
- Pytest para estructurar y ejecutar las pruebas.
- PyCharm como entorno de desarrollo.

## INSTRUCCIONES PARA EJECUTAR LAS PRUEBAS 

- Instalar librerias pytest y requests:
  > > pip3 install pytest  
  > > pip3 install requests
- o instalar desde requests.txt
  > > pip3 install -r requirements.txt


## EJECUCIÓN DE PRUEBAS 
1.  python3 -m pytest <Path-to-test-file>.py -vv -s
2.  Ejecución por medio del IDE

* Para ejecutar las Pruebas Asegúrate de estar en el directorio "main.py", donde se encuentran las pruebas. Luego, ejecuta las pruebas utilizando pytest
* Al finalizar las pruebas, pytest mostrará un resumen de los resultados en la terminal.

## FUNCIONALIDAD DE LAS PRUEBAS 

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

 ## ANÁLISIS Y HALLAZGOS

✅ Casos exitosos:

El sistema acepta nombres con longitudes entre 1 y 511 caracteres, devolviendo un código 201 (Creado) y confirmando que el valor en la respuesta coincide con la solicitud.
Se permite el uso de caracteres especiales, números y espacios, lo que ofrece flexibilidad en la creación de kits.

⚠️ Errores detectados:

Solicitudes con menos de 1 o más de 511 caracteres en el parámetro "name" retornan correctamente un código 400 (Solicitud incorrecta), asegurando la validación de límites.
No enviar el parámetro "name" en la solicitud también genera un error 400, evitando creaciones inválidas.
Se identificó que pasar un número en lugar de un string como valor de "name" también causa un error 400, lo que confirma que el sistema aplica validaciones de tipo de dato.

🔍 Tendencias observadas:

El sistema sigue las reglas esperadas en la validación del parámetro "name", permitiendo variaciones comunes en la entrada del usuario, pero bloqueando valores inválidos.
La API maneja correctamente los códigos de respuesta, lo que facilita la depuración y el control de errores en el desarrollo.

## RECOMENDACIONES Y CONCLUSIÓN 

Para fortalecer la validación y robustez de la API de Urban.Grocers, se sugieren las siguientes mejoras:

* Ampliar las pruebas con diferentes conjuntos de datos: Incluir caracteres de distintos alfabetos (como cirílico, chino o árabe) para asegurar compatibilidad global.
  
* Validación más detallada de caracteres especiales: Aunque se permite su uso, se recomienda definir una lista de caracteres aceptados y restringidos para evitar posibles vulnerabilidades de seguridad.

* Manejo de errores más descriptivo: Personalizar los mensajes de error en las respuestas del código 400, indicando específicamente por qué la solicitud es inválida (longitud incorrecta, tipo de dato erróneo, etc.).

* Automatización en integración continua: Implementar la ejecución automática de estas pruebas en cada actualización del back-end para detectar fallos de inmediato

Las pruebas automatizadas realizadas sobre la API de Urban.Grocers demostraron que el sistema maneja correctamente las validaciones del parámetro "name" al crear kits personales. Se confirmaron las reglas de longitud, caracteres permitidos y tipo de dato, garantizando que solo valores válidos sean aceptados.
Sin embargo, para fortalecer la confiabilidad del sistema, se recomienda ampliar la cobertura de pruebas con caracteres de distintos idiomas y reforzar la claridad en los mensajes de error. Implementar estas mejoras contribuirá a una API más estable, segura y preparada para su uso en diversos entornos.

import sender_stand_request
import data

#DEFINIR FUNCION PARA CREAR UN NUEVO USUARIO
def get_user_body(user_body):
   current_body = data.user_body.copy()
   current_body["user_body"] = user_body
   return current_body

def positive_assert (user_body):
    user_body = get_user_body(user_body)
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""
#FUNCION PARA CREAR UN NUEVO KIT
def positive_kit_assert (kit_body):
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

#FUNCION DE PRUEBAS NEGATIVAS PARA CREAR UN KIT
def negative_kit_assert (kit_body):
    kit_negative_response= sender_stand_request.post_new_client_kit(kit_body)
    assert kit_negative_response.status_code == 400
    assert kit_negative_response.json()["name"] == kit_negative_response["name"]

#Prueba 1. Crear un kit.
#El numero permitido de caracteres es 1 en el campo "name"#
def test_create_kit_1_letter_in_name_get_succes_response():
   positive_kit_assert({"name": "a"})
#Prueba 2.
#El numero permitido de caracteres (511)
def test_create_kit_511_letter_in_name_get_succes_response():
    positive_kit_assert({"name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"})
#Prueba 3.
#El número de caracteres es menor que la cantidad permitida (0)
def test_create_kit_0_letter_in_name_get_negative_response():
    negative_kit_assert({"name":""})
#Prueba 4.
#El número de caracteres es mayor que la cantidad permitida (512)
def test_create_kit_512_letter_in_name_get_negative_respone():
    negative_kit_assert({"name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"})
#Prueba 5.
#Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }.
def test_create_kit_special_letter_in_name_get_succes_response():
    positive_kit_assert({"name":"\"№ % @\","})
#Prueba 6,
#Se permiten espacios: kit_body = { "name": " A Aaa " }.
def test_create_kit_space_allow_in_name_get_succes_response():
    positive_kit_assert({"name":" A Aaa"})
#Prueba 7.
#Se permiten números: kit_body = { "name": "123" }
def test_create_kit_numbers_in_name_get_succes_response():
    positive_kit_assert({"name": "123"})
#Prueba 8.
#El parámetro no se pasa en la solicitud: kit_body = { }
def test_create_kit_parameter_in_name_get_negative_response():
    negative_kit_assert({"name":"{}"})
#Prueba 9.
#Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }
def test_create_kit_different_parameter_in_name_get_negative_response():
    negative_kit_assert({"name":123})
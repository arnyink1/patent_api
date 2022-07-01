import string
from app.serializers import patent


def list_alphabet():
    """Entrega el alfabeto en mayuculas dentro de una lista Excluye letra Ñ."""
    return list(string.ascii_uppercase)

def list_patent_alphabet():
    """Lista de placas patentes"""
    DOM = [] #Lista que almacena las platas patentes

    #Obtiene el alfabeto.
    alphabet = list_alphabet()
    
    #Concatena la letra del alfabeto para formar la estrucutra  de placa patente pedida ej: AAA000
    for alph in alphabet:
        a = 0
        while a <= 999:
            x = str(a).zfill(3)
            placa = "{}{}{}{}{}".format(alph,alph,alph,alph,x)
            DOM.append(placa)
            a = a + 1

    #Serializa las placas patentes dandoles un identificador unico.
    serialize = patent.serialize_patent_id(DOM)

    return serialize
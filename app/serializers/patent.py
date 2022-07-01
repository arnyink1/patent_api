"""Module with fields for serializers."""


def serialize_patent_id(patent_list):
    """Serializa la lista de placas patentes en un lista con identificador unico."""
    a = 0 
    list_patent_id = []
    for patent in patent_list:
        a = a + 1
        list_patent_id.append({"id":a,"patente":patent})

    return list_patent_id
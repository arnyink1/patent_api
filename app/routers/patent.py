from fastapi import APIRouter,status,Depends
from app.schemas import Patent
from app.oauth import get_current_user
from app.resources import patent_vehicle



router = APIRouter(
    prefix="/patent",
    tags=["Placa patente"]
)



patents = []
@router.get('/', status_code=status.HTTP_200_OK)
def patent(current_user: Patent = Depends(get_current_user)):
    """Endopoint que entrega toda la lista de placas patentes."""
    
    list_patent = patent_vehicle.list_patent_alphabet()
    return list_patent
    

@router.get('/{id}', status_code=status.HTTP_200_OK)
def patent_id(id:int,current_user: Patent = Depends(get_current_user)):
    """Endpoint que entrega la PLACA PATENTE del ID enviado."""

    list_patent = patent_vehicle.list_patent_alphabet()
    for patent_id in list_patent:
        if patent_id["id"] == id:
            return patent_id["patente"]
    return f"No se encuentra PATENTE para el ID: {id}"



@router.get('/placa/{patente}', status_code=status.HTTP_200_OK)
def patent_patente(patente:str,current_user: Patent = Depends(get_current_user)):
    """Endpoint que entrega el ID de la PLACA PATENTE enviada."""

    list_patent = patent_vehicle.list_patent_alphabet()
    for patent_id in list_patent:
        if patent_id["patente"] == patente:
            return patent_id["id"]
    return f"No se encuentra ID para Patente: {patente}"
        


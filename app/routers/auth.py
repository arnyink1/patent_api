
from fastapi import APIRouter,status,Depends
# from app.schemas import Login
from app.resources import auth
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/login",
    tags=["Auth"]
)

@router.post('/',status_code=status.HTTP_200_OK)
def login(login:OAuth2PasswordRequestForm = Depends()):
    """Endpoint necesario para obtener el token para realizar llamados mediante API."""
    auth_token = auth.auth_user(login)
    return auth_token
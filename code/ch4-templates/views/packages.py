import fastapi
from fastapi_chameleon import template

router = fastapi.APIRouter()

@router.get('/packages')
def index():
    return {}
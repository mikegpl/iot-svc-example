from fastapi import APIRouter, Response,status

router = APIRouter(
    prefix="/healthcheck",
    tags=["Healthcheck"],
)

@router.get("/healthy")
async def healthy():
    return Response(status.HTTP_200_OK)

@router.get("/ready")
async def ready():
    return Response(status.HTTP_200_OK)
from fastapi import APIRouter, Depends, Response,status
from app import dependencies

from app.service.activity import ActivityService, DeviceActivity, TimeRange

router = APIRouter(
    prefix="/activity",
    tags=["Activity"],
    responses={404: {"description": "Not found"}},
)

@router.post("/purge")
def purge(activity_service: ActivityService = Depends(dependencies.get_activity_service)):
    activity_service.purge_activities()
    return Response(status_code=status.HTTP_200_OK)

@router.get("/{device}")
def get_for_device(device: str, activity_service: ActivityService = Depends(dependencies.get_activity_service)):
    return activity_service.get_for_device(device)

@router.post("")
def log_activity(activity: DeviceActivity, activity_service: ActivityService = Depends(dependencies.get_activity_service)):
    activity_service.log_activity(activity)
    return Response(status_code=status.HTTP_200_OK)


@router.post("/uniqueCount")
def unique_count(range: TimeRange, activity_service: ActivityService = Depends(dependencies.get_activity_service)):
    return activity_service.unique_devices(range)
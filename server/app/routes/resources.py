from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status

from ..dependencies import get_resources_dependency
from ..schemas import Category, Resource, ResourceCreate
from ..services.resource_service import ResourceService

router = APIRouter(prefix="/resources", tags=["resources"])


@router.get("/", response_model=List[Resource])
def list_resources(
    *,
    category: Optional[Category] = Query(None, description="Filter by resource category."),
    search: Optional[str] = Query(None, description="Full-text search across titles, descriptions, tags."),
    service: ResourceService = Depends(get_resources_dependency),
) -> List[Resource]:
    return service.list_resources(category=category, search=search)


@router.post("/", response_model=Resource, status_code=status.HTTP_201_CREATED)
def create_resource(
    payload: ResourceCreate,
    service: ResourceService = Depends(get_resources_dependency),
) -> Resource:
    return service.add_resource(payload)


@router.get("/{resource_id}", response_model=Resource)
def get_resource(
    resource_id: int,
    service: ResourceService = Depends(get_resources_dependency),
) -> Resource:
    resource = service.get_resource(resource_id)
    if not resource:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")
    return resource

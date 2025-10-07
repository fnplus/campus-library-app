from collections.abc import Generator

from .services.resource_service import ResourceService, get_resource_service


def get_resources_dependency() -> Generator[ResourceService, None, None]:
    """Provide a ResourceService instance for request scope."""
    service = get_resource_service()
    try:
        yield service
    finally:
        service.close()

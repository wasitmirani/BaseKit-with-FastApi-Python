"""API package — HTTP routes and shared FastAPI dependencies.

Example: re-export the main router so callers can import from the package root:

    from app.api import api_router

instead of:

    from app.api.router import api_router
"""

from app.api.router import api_router

__all__ = ["api_router"]

"""
Exception handlers for the application.
"""

from fastapi import Request
from fastapi.responses import JSONResponse
from app.core.exceptions import NotFoundException, BadRequestException, DomainException


def domain_exception_handler(_, exc: DomainException):
    """
    Handle Common Domain level Exception and return a 400 JSON response.
    Function for new scalable custom exception too
    """
    return JSONResponse(status_code=400, content={"detail": exc.message})


def bad_request_handler(_: Request, exc: BadRequestException):
    """
    Handle BadRequestException and return a 400 JSON response.
    """
    return JSONResponse(
        status_code=400,
        content={"detail": exc.message},
    )


def not_found_handler(_: Request, exc: NotFoundException):
    """
    Handle NotFoundException and return a 404 JSON response.
    """
    return JSONResponse(
        status_code=404,
        content={"detail": exc.message},
    )

"""
Module for custom exceptions.
"""


class AppException(Exception):
    """Base application exception"""


class NotFoundException(AppException):
    """Exception raised when a resource is not found."""

    def __init__(self, message: str = "Resource not found"):
        self.message = message


class BadRequestException(AppException):
    """Exception raised for bad requests."""

    def __init__(self, message: str):
        self.message = message

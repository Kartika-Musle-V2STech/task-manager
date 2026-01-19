"""
Module for custom exceptions.
"""


class DomainException(Exception):
    """Base application exception can be used if created new custom exceptions in future"""


class NotFoundException(DomainException):
    """Exception raised when a resource is not found."""

    def __init__(self, message: str = "Resource not found"):
        self.message = message


class BadRequestException(DomainException):
    """Exception raised for bad requests."""

    def __init__(self, message: str):
        self.message = message

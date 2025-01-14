from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import Optional

class VendorBase(BaseModel):
    """
    Base schema for vendor data.
    Attributes:
        - name: Name of the vendor
        - type: Type of the vendor
    """
    name: str = Field(..., max_length=255, description="Vendor name")
    type: str = Field(..., max_length=50, description="Vendor type (e.g., Airline, Hotel)")

class VendorCreate(VendorBase):
    """
    Schema for creating a new vendor.
    """
    pass

class Vendor(VendorBase):
    """
    Schema for returning vendor data.
    """
    id: int

    class Config:
        orm_mode = True   # Enables ORM-to-Pydantic conversion

class BookingBase(BaseModel):
    """
    Base schema for booking data.
    Attributes:
        - booking_id: Unique booking identifier
        - customer_name: Customer's name
        - booking_date: Date of booking
        - amount: Booking amount
        - vendor_id: Vendor's ID
    """
    booking_id: str = Field(..., max_length=50, description="Unique Booking ID")
    customer_name: str = Field(..., max_length=255, description="Customer's full name")
    booking_date: datetime = Field(..., description="Booking date in ISO format (YYYY-MM-DDTHH:MM:SS)")
    amount: float = Field(..., gt=0, description="Booking amount (must be greater than 0)")
    vendor_id: int = Field(..., gt=0, description="Vendor ID (must be a positive integer)")

    # Pydantic root validation
    # @validator("booking_date")
    # def validate_booking_date(cls, value):
    #     """
    #     Ensures the booking date is not in the future.
    #     """
        
        # if value > datetime.utcnow():
        #     raise ValueError("Booking date cannot be in the future.")
        # return value

class BookingCreate(BookingBase):
    """
    Schema for creating a new booking.
    """
    pass

class Booking(BookingBase):
    """
    Schema for returning booking data.
    """
    id: int
    vendor: Vendor

    class Config:
        orm_mode = True

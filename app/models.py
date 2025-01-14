from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .db import Base

class Vendor(Base):
    """
    Represents a travel vendor.
    Columns:
        - id: Primary key
        - name: Unique name of the vendor
        - type: Type of vendor (e.g., Airline, Hotel)
    """
    __tablename__ = "vendors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    type = Column(String, nullable=False)

class Booking(Base):
    """
    Represents a booking made by a customer.
    Columns:
        - id: Primary key
        - booking_id: Unique booking identifier
        - customer_name: Name of the customer
        - booking_date: Date of booking
        - amount: Amount for the booking
        - vendor_id: Foreign key referencing Vendor table
    Relationships:
        - vendor: Links the booking to a vendor
    """
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(String, unique=True, index=True, nullable=False)
    customer_name = Column(String, nullable=False)
    booking_date = Column(DateTime, nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    vendor_id = Column(Integer, ForeignKey("vendors.id"), nullable=False)
    vendor = relationship("Vendor")

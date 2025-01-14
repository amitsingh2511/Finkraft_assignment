from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from . import models, schemas

def create_vendor(db: Session, vendor: schemas.VendorCreate):
    """
    Creates a new vendor in the database.
    """
    db_vendor = models.Vendor(name=vendor.name, type=vendor.type)
    db.add(db_vendor)
    try:
        db.commit()
        db.refresh(db_vendor)
    except IntegrityError:
        db.rollback()
        raise ValueError("Vendor with this name already exists.")
    return db_vendor

def create_booking(db: Session, booking: schemas.BookingCreate):
    """
    Creates a new booking in the database.
    """
    db_booking = models.Booking(**booking.dict())
    db.add(db_booking)
    try:
        db.commit()
        db.refresh(db_booking)
    except IntegrityError:
        db.rollback()
        raise ValueError("Booking with this ID already exists.")
    return db_booking

def get_bookings(db: Session, skip: int = 0, limit: int = 10):
    """
    Retrieves a list of bookings with pagination.
    """
    return db.query(models.Booking).offset(skip).limit(limit).all()

def get_booking(db: Session, booking_id: int):
    """
    Retrieves a booking by its ID.
    """
    return db.query(models.Booking).filter(models.Booking.id == booking_id).first()

def delete_booking(db: Session, booking_id: int):
    """
    Deletes a booking by its ID.
    """
    booking = db.query(models.Booking).filter(models.Booking.id == booking_id).first()
    if not booking:
        raise ValueError("Booking not found.")
    db.delete(booking)
    db.commit()
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud
from .db import engine, Base, get_db

# Initialize database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/vendors", response_model=schemas.Vendor)
def create_vendor(vendor: schemas.VendorCreate, db: Session = Depends(get_db)):
    """
    Adds a new vendor to the database.
    Args:
        vendor: VendorCreate schema containing vendor details.
        db: Database session dependency.
    Returns:
        The newly created vendor.
    """
    try:
        return crud.create_vendor(db=db, vendor=vendor)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))



@app.post("/bookings", response_model=schemas.Booking)
def create_booking(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    """
    Adds a new booking to the database.
    Args:
        booking: BookingCreate schema containing booking details.
        db: Database session dependency.
    Returns:
        The newly created booking with vendor details.
    """
    try:
        return crud.create_booking(db=db, booking=booking)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))



@app.get("/bookings", response_model=list[schemas.Booking])
def read_bookings(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Retrieves a list of bookings from the database.
    Args:
        skip: Number of records to skip (pagination).
        limit: Number of records to return (pagination).
        db: Database session dependency.
    Returns:
        A list of bookings with vendor details.
    """
    return crud.get_bookings(db=db, skip=skip, limit=limit)



@app.get("/bookings/{booking_id}", response_model=schemas.Booking)
def read_booking(booking_id: int, db: Session = Depends(get_db)):
    """
    Retrieves a booking by its ID.
    Args:
        booking_id: The ID of the booking to retrieve.
        db: Database session dependency.
    Returns:
        The booking details if found, or raises a 404 error.
    """
    booking = crud.get_booking(db=db, booking_id=booking_id)
    if booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking



@app.delete("/bookings/{booking_id}")
def delete_booking(booking_id: int, db: Session = Depends(get_db)):
    """
    Deletes a booking by its ID.
    Args:
        booking_id: The ID of the booking to delete.
        db: Database session dependency.
    Returns:
        A success message if the booking is deleted, or raises a 404 error.
    """
    try:
        crud.delete_booking(db=db, booking_id=booking_id)
        return {"message": "Booking deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

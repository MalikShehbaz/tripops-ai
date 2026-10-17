


from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.booking_inquiry import BookingInquiryCreate, BookingInquiryResponse
from app.services.booking_inquiry_service import BookingInquiryService


router = APIRouter(prefix="/inquiries", tags=["Booking Inquiries"])

@router.post("", response_model= BookingInquiryResponse)
def create_inquiry(
    inquiry_data: BookingInquiryCreate,
    db: Session = Depends(get_db)
):
    service = BookingInquiryService(db)
    return service.create_inquiry(inquiry_data)

@router.get("/{inquiry_id}", response_model=BookingInquiryResponse)
def get_inquiry(
    inquiry_id: int,
    db: Session = Depends(get_db),
):
    service = BookingInquiryService(db)
    inquiry = service.get_booking_inquiry(inquiry_id)

    if inquiry is None:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail = "Booking inquiry not found"
        )

    return inquiry
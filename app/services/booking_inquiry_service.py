


from sqlalchemy.orm import Session

from app.repositories.booking_inquiry_repository import BookingInquiryRepository
from app.schemas.booking_inquiry import BookingInquiryCreate, BookingInquiryResponse


class BookingInquiryService():
    def __init__(self, db: Session) -> None:
        self.repository = BookingInquiryRepository(db)


    def create_inquiry(self, inquiry_data: BookingInquiryCreate):
        inquiry = self.repository.create(inquiry_data)

        return BookingInquiryResponse.model_validate(inquiry)


    def get_booking_inquiry(self, inquiry_id: int):
        inquiry = self.repository.get_by_id(inquiry_id)

        if inquiry is None:
            return None

        return BookingInquiryResponse.model_validate(inquiry)


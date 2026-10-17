from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.booking_inquiry import BookingInquiry
from app.schemas.booking_inquiry import BookingInquiryCreate


class BookingInquiryRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, inquiry: BookingInquiryCreate) -> BookingInquiry:
        booking_inquiry = BookingInquiry(**inquiry.model_dump())

        self.db.add(booking_inquiry)
        self.db.commit()
        self.db.refresh(booking_inquiry)
        return booking_inquiry


    def get_by_id(self, inquiry_id: int)-> BookingInquiry | None:
        statement = select(BookingInquiry).where(BookingInquiry.id == inquiry_id)

        return self.db.scalar(statement)





import json

from app.schemas.booking_inquiry import BookingInquiryCreate
from app.services.booking_inquiry_service import BookingInquiryService


def test_create_inquiry(db_session):
    service = BookingInquiryService(db_session)

    inquiry_data = BookingInquiryCreate(
            name= "Ali Khan",
            contact_number = "+923001234567",
            destination= "Sri Lanka",
            number_of_travelers= 2,
            duration_days= 7,
        )

    result = service.create_inquiry(inquiry_data)

    assert result.id is not None
    assert result.name == inquiry_data.name
    assert result.contact_number == inquiry_data.contact_number
    assert result.status == "new"


def test_get_inquiry(db_session):
    service = BookingInquiryService(db_session)

    inquiry_data = BookingInquiryCreate(
                name= "Malik Shehbaz",
                contact_number = "+923001234567",
                destination= "Sri Lanka",
                number_of_travelers= 2,
                duration_days= 7,
            )

    created = service.create_inquiry(inquiry_data)

    result = service.get_booking_inquiry(created.id)

    assert result is not None
    assert result.name == inquiry_data.name
    assert result.contact_number == inquiry_data.contact_number
    assert result.status == "new"
    

def test_get_missing_inquiry_returns_none(db_session):
    service = BookingInquiryService(db_session)

    result = service.get_booking_inquiry(99999)

    assert result is None


    



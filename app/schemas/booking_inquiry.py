from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


InquiryStatus = Literal[
    "new",
    "in_progress",
    "completed",
    "cancelled"
]

class BookingInquiryCreate(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    contact_number: str = Field(max_length=32)
    destination: str = Field(max_length=255)
    number_of_travelers: int = Field(gt=0)
    duration_days: int = Field(gt=0)


class BookingInquiryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    contact_number: str
    destination: str
    number_of_travelers: int
    duration_days: int
    status: InquiryStatus
    created_at: datetime

from datetime import datetime

from sqlalchemy import DateTime, Integer, String, func, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from pgvector.sqlalchemy import Vector


from app.core.database import Base


class DocumentChunk(Base):
    __tablename__ = "document_chunks"

    __table_args__ = (
        UniqueConstraint(
            "source_name",
            "chunk_index",
        ),
    )

    id:Mapped[int] = mapped_column(primary_key=True)

    source_name:Mapped[str] = mapped_column(
        String(255),
        nullable= False,
    )

    chunk_index:Mapped[int] = mapped_column(
        Integer,
        nullable= False,
    )

    content:Mapped[str] = mapped_column(
        String,
        nullable= False,
    )

    embedding:Mapped[list[float]] = mapped_column(
        Vector(768),
        nullable= False
    )

    created_at:Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default= func.now()
    )
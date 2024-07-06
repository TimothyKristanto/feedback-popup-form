from db import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

# declare model class for database migration
class Feedback(Base):
    __tablename__ = "feedbacks"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    rating: Mapped[int] = mapped_column(nullable=False)
    date_created: Mapped[datetime] = mapped_column(default=datetime.now())

    def __repr__(self) -> str:
        return f"<Feedback rating {self.rating} at {self.date_created}>"
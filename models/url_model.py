from sqlalchemy import Column, Integer, String, DateTime
from db.database import Base
from datetime import datetime

class URLMapping(Base):
    __tablename__ = "url_mapping"

    id = Column(Integer, primary_key=True, index=True)
    short_code = Column(String(10), unique=True, index=True)
    full_url = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    expires_at = Column(DateTime, nullable=True)
    click_count = Column(Integer, default=0)



from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime
import enum

# ---------- Enums ----------
class RoleEnum(str, enum.Enum):
    manager = "manager"
    employee = "employee"

class SentimentEnum(str, enum.Enum):
    positive = "positive"
    neutral = "neutral"
    negative = "negative"

# ---------- User Table ----------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)
    role = Column(Enum(RoleEnum), nullable=False)

    given_feedbacks = relationship("Feedback", foreign_keys='Feedback.manager_id', back_populates="manager")
    received_feedbacks = relationship("Feedback", foreign_keys='Feedback.employee_id', back_populates="employee")

# ---------- Feedback Table ----------
class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    manager_id = Column(Integer, ForeignKey("users.id"))
    employee_id = Column(Integer, ForeignKey("users.id"))
    strengths = Column(Text, nullable=False)
    improvement_areas = Column(Text, nullable=False)  # ✅ Use consistent field name
    sentiment = Column(Enum(SentimentEnum), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    manager = relationship("User", foreign_keys=[manager_id], back_populates="given_feedbacks")
    employee = relationship("User", foreign_keys=[employee_id], back_populates="received_feedbacks")

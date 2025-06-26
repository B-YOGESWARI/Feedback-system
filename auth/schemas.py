from pydantic import BaseModel, EmailStr
from enum import Enum
from typing import Optional
from datetime import datetime

# ---------- Enums ----------
class RoleEnum(str, Enum):
    manager = "manager"
    employee = "employee"

class SentimentEnum(str, Enum):
    positive = "positive"
    neutral = "neutral"
    negative = "negative"

# ---------- Auth Schemas ----------
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: RoleEnum

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: RoleEnum

    class Config:
        from_attributes = True  # ✅ updated from `orm_mode = True` for Pydantic v2

# ---------- Feedback Schemas ----------
class FeedbackCreate(BaseModel):
    employee_id: int
    strengths: str
    improvement_areas: str
    sentiment: SentimentEnum

class FeedbackOut(FeedbackCreate):
    id: int
    timestamp: datetime
    manager_id: Optional[int]  # optional to display if needed

    class Config:
        from_attributes = True  # ✅ to allow ORM -> Pydantic conversion
# ---------- Token Schema ----------
class Token(BaseModel):
    access_token: str
    token_type: str

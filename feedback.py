from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from auth import schemas
from database import get_db
from models import Feedback

router = APIRouter()

@router.post("/feedback", response_model=schemas.FeedbackOut)
def give_feedback(feedback: schemas.FeedbackCreate, db: Session = Depends(get_db)):
    feedback_entry = Feedback(
        employee_id=feedback.employee_id,
        strengths=feedback.strengths,
        areas_to_improve=feedback.areas_to_improve,  # ⚠️ Match this field name exactly
        sentiment=feedback.sentiment
    )
    db.add(feedback_entry)
    db.commit()
    db.refresh(feedback_entry)
    return feedback_entry

@router.get("/feedback", response_model=list[schemas.FeedbackOut])
def get_all_feedback(db: Session = Depends(get_db)):
    return db.query(Feedback).all()

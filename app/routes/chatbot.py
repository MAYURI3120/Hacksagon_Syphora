from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User

router = APIRouter(
    prefix="/chatbot",
    tags=["Chatbot"]
)


class ChatRequest(BaseModel):
    message: str
    user_id: int


@router.post("/")
def chatbot_reply(request: ChatRequest, db: Session = Depends(get_db)):
    # Fetch user data
    user = db.query(User).filter(User.id == request.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Custom logic based on user profile
    user_message = request.message.lower()
    response = "Sorry, I didn't understand that."

    if "how much water" in user_message or "drink" in user_message:
        if user.age and user.age > 60:
            response = "Since you're over 60, it's important to drink at least 2.5 liters daily."
        elif user.age and user.age < 18:
            response = "You should drink about 1.5 to 2 liters of water per day."
        else:
            response = "Aim for 2 to 3 liters of water daily based on your activity level."

    elif "diabetes" in user_message or "sugar" in user_message or (
        user.medical_conditions and "diabetes" in user.medical_conditions
    ):
        response = "As a diabetic, it's crucial to stay hydrated. Avoid sugary drinks and drink water regularly."

    elif "heat" in user_message or "hot" in user_message:
        response = "In hot weather, drink water more frequently. Carry a bottle and avoid outdoor activity during noon."

    elif "headache" in user_message:
        response = "Dehydration can cause headaches. Drink a glass of water and take rest."

    elif "hello" in user_message or "hi" in user_message:
        response = f"Hello {user.username}! I'm your hydration assistant. Ask me anything about water intake, heat safety, or health tips."

    return {"response": response}

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/chatbot", tags=["Chatbot"])


class ChatRequest(BaseModel):
    message: str
    age: int
    conditions: list[str] = []


@router.post("/reply")
def get_chatbot_reply(req: ChatRequest):
    text = req.message.lower()
    age = req.age
    conditions = req.conditions

    bot_response = "I'm not sure how to help with that."

    if "hydration" in text or "water" in text:
        bot_response = "Drink 2-3L of water daily."
        if age > 60:
            bot_response += " As a senior, take small sips frequently."
        if "diabetes" in conditions:
            bot_response += " Avoid sugary drinks if diabetic."

    elif "heatstroke" in text:
        bot_response = "Avoid heat. Stay in shade, drink water."
        if age > 60:
            bot_response += " Seniors are more prone to heatstroke."

    elif "food" in text:
        bot_response = "Eat watermelon, cucumber, and oranges."
        if "diabetes" in conditions:
            bot_response += " Prefer low-sugar fruits like apples."

    elif "emergency" in text:
        bot_response = "Find a cool place and seek help immediately."

    return {"reply": bot_response}

from fastapi import APIRouter, HTTPException
from app.llm import chat
from app.schemas import ChatRequest, ChatResponse

router = APIRouter()

TEACHER_PROMPT = "You are a friendly school teacher. Answer clearly and briefly."


@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(body: ChatRequest):
    messages = [{"role": "user", "content": body.message}]

    try:
        reply = chat(messages, system=TEACHER_PROMPT)
    except Exception as error:
        print("LLM call failed:", error)
        raise HTTPException(status_code=502, detail="The teacher is unavailable. Try again.")

    return ChatResponse(teacher="general", reply=reply)


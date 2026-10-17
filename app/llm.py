from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

from app.config import get_settings

settings = get_settings()

model = init_chat_model(
    settings.llm_model,
    model_provider=settings.llm_provider,
    api_key=settings.llm_api_key,
)


def get_text(content):
    # Sometimes the model returns a plain string, sometimes a list of pieces.
    # This turns either one into a plain string.
    if isinstance(content, str):
        return content

    text = ""
    for piece in content:
        if isinstance(piece, dict):
            text = text + piece.get("text", "")
    return text


def chat(messages, system=None):
    # Step 1: convert our simple dicts into LangChain message objects
    lc_messages = []

    if system:
        lc_messages.append(SystemMessage(content=system))

    for m in messages:
        if m["role"] == "assistant":
            lc_messages.append(AIMessage(content=m["content"]))
        else:
            lc_messages.append(HumanMessage(content=m["content"]))

    # Step 2: ask the model
    reply = model.invoke(lc_messages)

    # Step 3: pull the plain text out of the reply
    return get_text(reply.content)
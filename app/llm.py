from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

from app.config import get_settings

settings = get_settings()

# One model object, built from config. Switching provider = change .env.
_model = init_chat_model(
    settings.llm_model,
    model_provider=settings.llm_provider,
    api_key=settings.llm_api_key,
)


def _as_text(content) -> str:
    # Some providers return a list of content blocks instead of a string.
    if isinstance(content, str):
        return content
    return "".join(
        block.get("text", "") for block in content if isinstance(block, dict)
    )


def chat(messages: list[dict], system: str | None = None) -> str:
    """Send a conversation to the model and return the reply text.

    messages: [{"role": "user" | "assistant", "content": "..."}]
    system:   the teacher's persona / instructions (optional)
    """
    lc_messages = []
    if system:
        lc_messages.append(SystemMessage(content=system))
    for m in messages:
        message_class = AIMessage if m["role"] == "assistant" else HumanMessage
        lc_messages.append(message_class(content=m["content"]))

    reply = _model.invoke(lc_messages)
    return _as_text(reply.content)
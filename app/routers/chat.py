from fastapi import APIRouter, status
from pydantic import BaseModel
from app.agents.ex_2.response_format import gerar_resposta
from typing import Optional
import uuid

router = APIRouter(prefix="/chat", tags=["Chat"])
class ChatQuestion(BaseModel):
    mensagem: str
    session: Optional[str] = None

class ChatResponse(BaseModel):
    pergunta: str
    resposta: str
    session: str

@router.post("/", response_model=ChatResponse, status_code=status.HTTP_200_OK, summary="Enviar nova Mensagem de Consulta")
def enviar_mensagem(pergunta: ChatQuestion):

    session = str(uuid.uuid4())

    resposta = gerar_resposta(pergunta.mensagem)

    return {
        "pergunta": pergunta.mensagem,
        "resposta": resposta,
        "session": session
    }

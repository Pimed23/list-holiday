from typing import List, Optional
from pydantic import BaseModel, field_validator
from datetime import datetime

class Laws(BaseModel):
    nombre: str
    url: str

class Holiday(BaseModel):
    nombre: str
    comentarios: Optional[str]
    fecha: datetime
    irrenunciable: bool
    tipo: str
    leyes: Optional[List[Laws]] = []

    @field_validator("comentarios")
    def validate_comments(cls, comment):
        if comment is None or comment.strip() == "":
            return None
        else:
            return comment
    
    @field_validator("fecha", mode="before")
    def validate_date(cls, date):
        return datetime.strptime(date, '%Y-%m-%d')


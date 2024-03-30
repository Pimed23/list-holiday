from typing import List, Optional
from pydantic import BaseModel, field_validator
from datetime import datetime


# Data model for laws
class Laws(BaseModel):
    nombre: str
    url: str


# Data model for holidays
class Holiday(BaseModel):
    nombre: str
    comentarios: Optional[str]
    fecha: datetime
    irrenunciable: bool
    tipo: str
    leyes: Optional[List[Laws]] = []

    # Validator for 'comentarios' field 
    @field_validator("comentarios")
    def validate_comments(cls, comment):
        # If comments are None or empty string returns null
        if comment is None or comment.strip() == "":
            return None
        else:
            return comment

    # Validator for 'fecha' field executed before assignment
    @field_validator("fecha", mode="before")
    def validate_date(cls, date):
        # Validate and at the same time parse the information
        return datetime.strptime(date, "%Y-%m-%d")

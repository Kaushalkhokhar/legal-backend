from typing import Optional
from pydantic import BaseModel

class Esearch(BaseModel):
    user_query : Optional[str]


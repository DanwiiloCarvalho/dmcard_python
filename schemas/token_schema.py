from pydantic import BaseModel as SCBaseModel


class Token(SCBaseModel):
    access_token: str
    token_type: str

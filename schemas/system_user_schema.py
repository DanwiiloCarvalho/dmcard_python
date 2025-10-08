from pydantic import BaseModel as SCBaseModel
from pydantic import EmailStr, field_validator


class BaseSystemUser(SCBaseModel):
    id: int | None = None
    username: str
    full_name: str
    email: EmailStr

    @field_validator('username')
    def validate_username(cls, username: str) -> str:
        if len(username) < 3:
            raise ValueError(
                'Nome de usuário deve ter pelo menos 3 caracteres')
        if not username.isalnum():
            raise ValueError(
                'Nome de usuário deve conter apenas letras e números')
        return username

    @field_validator('full_name')
    def validate_full_name(cls, full_name: str) -> str:
        if len(full_name.split()) < 2:
            raise ValueError(
                'Nome completo deve conter pelo menos nome e sobrenome')
        return full_name


class CreateSystemUser(BaseSystemUser):
    password: str

    @field_validator('password')
    def validate_password(cls, password: str) -> str:
        if len(password) < 8:
            raise ValueError('A senha deve ter pelo menos 8 caracteres')
        if not any(char.isupper() for char in password):
            raise ValueError(
                'A senha deve conter pelo menos uma letra maiúscula')
        if not any(char.islower() for char in password):
            raise ValueError(
                'A senha deve conter pelo menos uma letra minúscula')
        if not any(char.isdigit() for char in password):
            raise ValueError('A senha deve conter pelo menos um número')
        if not any(not char.isalnum() for char in password):
            raise ValueError(
                'A senha deve conter pelo menos um caractere especial')
        return password


class LoginSystemUser(SCBaseModel):
    email: EmailStr
    password: str

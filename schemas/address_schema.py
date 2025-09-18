from pydantic import BaseModel as SCBaseModel
from pydantic import field_validator


class AddressSchema(SCBaseModel):
    id: int | None = None
    street: str
    number: str
    area: str
    city: str
    state: str
    cep: str

    model_config = {'from_attributes': True}

    @field_validator('cep')
    def validate_cep(cls, cep: str) -> str:
        import re
        cep_pattern = re.compile(r'^\d{5}-?\d{3}$')

        if cep_pattern.match(cep):
            return cep
        raise ValueError(f'O cep {cep} não é válido.')

    @field_validator('state')
    def validate_state(cls, state: str) -> str:
        if len(state) < 2:
            raise ValueError('O estado possui menos de 2 caracteres.')
        if not state.isupper():
            raise ValueError('O estado deve estar em caixa alta.')
        return state

    @field_validator('city')
    def validate_city(cls, city: str) -> str:
        if not city.istitle():
            raise ValueError('O nome da cidade deve estar capitalizado.')
        return city

    @field_validator('number')
    def validate_number(cls, number: str) -> str:
        if int(number) < 0:
            raise ValueError('O número deve ser maior que zero.')
        return number

    @field_validator('street')
    def validate_street(cls, street: str) -> str:
        if len(street) < 0:
            raise ValueError('A rua não pode ser vazia.')
        return street

    @field_validator('area')
    def validate_area(cls, area: str) -> str:
        if len(area) < 0:
            raise ValueError('O bairro não pode ser vazio.')
        return area

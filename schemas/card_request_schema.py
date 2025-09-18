from datetime import date, datetime
from decimal import Decimal
from schemas.address_schema import AddressSchema
from pydantic import BaseModel as SCBaselModel, Field
from pydantic import field_validator


class CardRequestSchema(SCBaselModel):
    name: str
    birth_date: date
    cpf: str
    occupation: str
    income: Decimal
    address: AddressSchema

    @field_validator('name')
    def name_validate(cls, name: str) -> str:
        if not len(name) > 0:
            raise ValueError('O nome deve ter comprimento maior que zero.')
        return name

    @field_validator('birth_date')
    def birth_date_validate(cls, birth_date: date) -> date:
        if birth_date > datetime.now().date():
            raise ValueError(
                'A data de nascimento não pode ser uma data futura.')
        return birth_date

    @field_validator('cpf')
    def cpf_validate(cls, cpf: str) -> str:
        # Validações básicas
        if len(cpf) != 11:
            raise ValueError('O cpf deve conter 11 digitos.')
        if not cpf.isdigit():
            raise ValueError('O cpf deve conter apenas números.')
        if cpf == cpf[0] * 11:
            raise ValueError('O cpf não pode ter todos os dígitos iguais.')

        # Cálculo do primeiro dígito verificador
        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)
        resto = soma % 11
        digito1 = 0 if resto < 2 else 11 - resto

        if int(cpf[9]) != digito1:
            raise ValueError(
                'CPF inválido: primeiro dígito verificador incorreto.')

        # Cálculo do segundo dígito verificador
        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)
        resto = soma % 11
        digito2 = 0 if resto < 2 else 11 - resto

        if int(cpf[10]) != digito2:
            raise ValueError(
                'CPF inválido: segundo dígito verificador incorreto.')

        return cpf

    @field_validator('occupation')
    def occupation_validate(cls, occupation: str) -> str:
        if not len(occupation) > 0:
            raise ValueError('A ocupação deve ter comprimento maior que zero.')
        return occupation

    @field_validator('income')
    def income_validate(cls, income: Decimal) -> Decimal:
        if income.as_tuple().exponent < -2:
            raise ValueError('Renda não pode ter mais de 2 casas decimais.')
        if income < 0:
            raise ValueError('A renda não pode ter valor negativo.')
        return income

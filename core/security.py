from pwdlib import PasswordHash

password_hash: PasswordHash = PasswordHash.recommended()


def generate_password_hash(password: str) -> str:
    hash: str = password_hash.hash(password)

    return hash


def verify_password(password: str, hashed_password: str) -> bool:
    return password_hash.verify(password, hashed_password)

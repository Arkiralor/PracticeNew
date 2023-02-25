"""
Python module to test out JWT token generation/decryption.
"""

from dataclasses import dataclass
from os import environ
from jwt import encode, decode

from dotenv import load_dotenv


@dataclass
class User:
    id: str = None
    username: str = None
    email: str = None
    password: str = None


class JWTUtils:
    load_dotenv(".env")
    SECRET_KEY = environ['SECRET_KEY']
    ALGORITHM = environ['JWT_ALGORITHM']

    @classmethod
    def generate_token(cls, user: User, *args, **kwargs):
        payload = {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }

        token = encode(
            payload=payload,
            key=cls.SECRET_KEY,
            algorithm=cls.ALGORITHM
        )

        return token

    @classmethod
    def authenticate_token(cls, token: any = None, *args, **kwargs):
        payload = decode(jwt=token, key=cls.SECRET_KEY,
                         algorithms=[cls.ALGORITHM])
        return payload


def main():
    load_dotenv(".env")

    user_data = {
        "id": "1123581321",
        "username": "arkiralor",
        "email": "fablelordarkalon11235@gmail.com",
        "password": "P@ssword11235"
    }

    user = User(**user_data)
    print(f"User:\t{user}")

    token = JWTUtils.generate_token(user=user)
    print(f"JWT:\t{token}")

    decoded = JWTUtils.authenticate_token(token=token)
    print(f"Payload:\t{decoded}")


if __name__ == "__main__":
    main()

from pprint import pprint
from typing import Generator, LiteralString

import requests


VALIDATE_ADDRESS_API_KEY: LiteralString = r"7b5c4117e3614f9ab85fcf4e09b458cf"


def validate_address(address) -> str:
    url: str = f"https://api.opencagedata.com/geocode/v1/json?q={address}&key={VALIDATE_ADDRESS_API_KEY}"
    response: requests.Response = requests.get(url)
    data: dict = response.json()
    # pprint(data)
    if data.get("results"):
        first_result: dict = data["results"][0]
        confidence: int = first_result.get("confidence", 0)
        formatted_address: str = first_result.get("formatted", "")

        if confidence >= 5:
            return formatted_address

    raise ValueError("Address is not valid")


def identity_generator() -> Generator[int, None, None]:
    new_id: int = 0
    while True:
        yield new_id
        new_id += 1


id_generator: Generator[int, None, None] = identity_generator()


class Entity:
    name: str
    _identity: int

    def __init__(self, name) -> None:
        self.name = name
        self._identity = id_generator.__next__()


class Content:
    _identity: int


class Collection:
    pass


class Store:
    name: str
    _address: str
    _rating: int
    _identity: int

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, value: str) -> None:
        # validate if address is valid
        self._address = validate_address(value)

    @property
    def rating(self) -> int:
        return self._rating

    @rating.setter
    def rating(self, value: int):
        if value < 0 or value > 10:
            raise ValueError("Rating must be between 0 and 10")
        self._rating = value

    def __init__(self, name) -> None:
        self.name = name
        self._rating = 0
        self._identity = id_generator.__next__()


pája = Entity("Pája")
kája = Entity("Kája")
tája = Entity("Tája")
jája = Entity("Jája")

print(pája._identity)
print(kája._identity)
print(tája._identity)
print(jája._identity)

bb = Store("Blockbuster")
bb.address = "7, Říčanská 2414, Vinohrady, 101 00 Praha"
bb.rating = 5

print(bb.address)
print(bb.rating)

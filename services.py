from tibiadatabase import Monsters


def create(monster: dict[str, str | int]) -> int:

    query = Monsters.insert(**monster)
    name = query.execute()
    return name


def read(name: str):
    return Monsters.get_by_name(name)


def update(name: str, monstermodify: dict[str, str | int]):
    return Monsters.update_by_name(name, monstermodify)


def delete(name: str):
    return Monsters.delete_by_name(name)

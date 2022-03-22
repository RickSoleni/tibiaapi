from peewee import CharField, IntegerField, SqliteDatabase, Model, DoesNotExist

db = SqliteDatabase('monsters.db')


class BaseModel(Model):
    class Meta:
        database = db


class Abilities(BaseModel):   # create table monster
    name = CharField(max_length=100)
    ability_type = CharField(max_length=20)   # types Healing, Damage
    ability_range = IntegerField()   # number of squares
    damage = IntegerField()
    self_healing = IntegerField()
    healing = IntegerField()


class Monsters(BaseModel):   # create table monster
    name = CharField(max_length=20)
    hp = IntegerField()
    exp = IntegerField()
    charms = IntegerField()
    speed = IntegerField()
    armor = IntegerField()
    abilities = IntegerField()

    @classmethod
    def get_as_dict(cls, where):
        try:
            query = cls.select().where(where).dicts()
            return query.get()
        except DoesNotExist:
            return None

    @classmethod
    def get_by_name(cls, name):
        try:
            query = (
                cls.select(
                    Monsters.name,
                    Monsters.hp,
                    Monsters.exp,
                    Monsters.charms,
                    Monsters.speed,
                    Monsters.armor,
                    Monsters.abilities,
                )
                .where(Monsters.name == name)
                .dicts()
            )
            return query.get()
        except DoesNotExist:
            return None

    @classmethod
    def update_by_name(cls, name, modify):
        try:
            query = cls.update(**modify).where(Monsters.name == name)
            return query.execute()
        except Exception as err:
            print(f'DEU PAU NO BANCO DE DADOS: {err}')
            return None

    @classmethod
    def delete_by_name(cls, name):
        try:
            query = cls.delete().where(Monsters.name == name)
            return query.execute()
        except Exception as err:
            print(f'DEU PAU NO BANCO DE DADOS: {err}')
            return None


db.connect()
db.create_tables([Monsters, Abilities])

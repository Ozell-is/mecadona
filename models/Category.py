import json

from app import db


class Category(db.Model):
    __tablename__ = "Category"

    _id_category = db.Column("id_category", db.Integer, primary_key=True, autoincrement=True, nullable=False)
    _libelle = db.Column("libelle", db.String(20),nullable=False)
    # relationship one-to-many
    _products = db.relationship("Product", backref="category")

    def __init__(self, id_category: int, libelle: str, ):
        self._id_category = id_category
        self._libelle = libelle


    @property
    def id_category(self):
        return self._id_category

    @property
    def libelle(self):
        return self._libelle

    @libelle.setter
    def libelle(self, libelle: str):
        self._libelle = libelle


    def to_json(self):
        return self.__str__()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __iter__(self):
        yield from {
            "id_category": self._id_category,
            "libelle": self._libelle,

        }.items()

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def from_json(json_dct):
        id_category = None
        if json_dct.get('id_category'):
            id_category: int = int(json_dct["id_category"])
        return Category(id_category, json_dct.get("libelle"))


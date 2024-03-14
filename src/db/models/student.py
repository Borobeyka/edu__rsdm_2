import datetime
from typing import List

import sqlalchemy.orm as orm

from .base import Base, intpk


class StudentORM(Base):
    __tablename__ = "students"

    id: orm.Mapped[intpk]
    name: orm.Mapped[str]
    surname: orm.Mapped[str]
    birth_date: orm.Mapped[datetime.date]
    gradebook: orm.Mapped[List["SubjectORM"]] = orm.relationship(lazy="selectin")

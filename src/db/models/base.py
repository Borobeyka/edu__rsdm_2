from pathlib import Path
from typing import Annotated

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapped_column
from sqlalchemy_repr import RepresentableBase

MODELS_PATH = Path(__file__).parent.resolve()
intpk = Annotated[int, mapped_column(primary_key=True)]


DeclarativeBase = declarative_base(cls=RepresentableBase)


class Base(DeclarativeBase):
    __abstract__ = True

import datetime

import sqlalchemy as sa
import sqlalchemy.orm as orm

from .base import Base, intpk


class SubjectORM(Base):
    __tablename__ = "subjects"

    id: orm.Mapped[intpk]
    title: orm.Mapped[str]
    estimation: orm.Mapped[int]
    exam_date: orm.Mapped[datetime.date]
    tutor_fullname: orm.Mapped[str]

    student_id: orm.Mapped[int] = orm.mapped_column(
        sa.ForeignKey("students.id", ondelete="CASCADE")
    )
    student: orm.Mapped["StudentORM"] = orm.relationship(
        back_populates="gradebook", lazy="selectin"
    )

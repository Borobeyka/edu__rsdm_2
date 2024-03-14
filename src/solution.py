from sqlalchemy import func
from tabulate import tabulate

from db.base import NewSession
from src.db.models.subject import SubjectORM


class Solution:
    def __init__(self):
        result = []
        headers = ["title", "count"]
        with NewSession() as db:
            subjects = db.query(
                SubjectORM.title,
                func.count(SubjectORM.id).label("count")
            ).group_by(SubjectORM.title).all()
        for subject in subjects:
            result.append(
                ["", subject.title, subject.count]
            )
        print("Result:")
        print(tabulate(result, headers=headers))

import random

from faker import Faker
from faker.providers import date_time

from db.base import NewSession
from db.models import StudentORM, SubjectORM


class Generator:
    GROUP_SIZE = 10
    MIN_GRADEBOOK_SIZE = 3
    MAX_GRADEBOOK_SIZE = 5
    SUBJECTS = ("Математика", "Информатика", "Русский язык", "Литература")

    def __init__(self):
        faker = Faker("ru_RU")
        faker.add_provider(date_time)
        print("GENERATING...")
        for _ in range(self.GROUP_SIZE):
            student = StudentORM(
                name=faker.first_name(),
                surname=faker.last_name(),
                birth_date=faker.date_of_birth(minimum_age=18, maximum_age=23),
            )

            for _ in range(self.MIN_GRADEBOOK_SIZE, self.MAX_GRADEBOOK_SIZE):
                student.gradebook.append(
                    SubjectORM(
                        title=random.choice(self.SUBJECTS),
                        estimation=random.randint(2, 5),
                        exam_date=faker.date_time_between(
                            start_date="-90d", end_date="now"
                        ),
                        tutor_fullname=faker.name(),
                    )
                )
            print(student)
            print(student.gradebook)
            print("=" * 90)
            self.add_to_db(student)
        print("GENERATE COMPLETED")

    def add_to_db(self, model: StudentORM) -> StudentORM:
        with NewSession() as db:
            db.add(model)
            db.flush()
            db.commit()
        return model

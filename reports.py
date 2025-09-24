from abc import ABC, abstractmethod
from statistics import mean


class Report(ABC):

    @abstractmethod
    def create(self, data):
        pass


class StudentPerformanceReport(Report):

    def create(self, data):
        grades_of_students = {}
        for row in data:
            grades_of_students.setdefault(
                row["student_name"], []
            ).append(int(row["grade"]))
        result = [["student_name", "grade"]]
        for student, grades in sorted(
            grades_of_students.items(),
            key=lambda item: mean(item[1]),
            reverse=True
        ):
            result.append([student, round(mean(grades), 1)])
        return result

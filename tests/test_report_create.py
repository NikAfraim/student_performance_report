from statistics import mean
from main import StudentPerformanceReport

def test_student_performance_report_create():
    data = [
        {"student_name": "Семенова Елена", "grade": "5"},
        {"student_name": "Титов Владислав", "grade": "4"},
        {"student_name": "Титов Владислав", "grade": "3"},
        {"student_name": "Семенова Елена", "grade": "2"},
    ]

    report = StudentPerformanceReport()
    result = report.create(data)

    assert result[0] == ["student_name", "grade"]
    assert len(result) == 3
    assert result[1][0] == "Семенова Елена"
    assert result[1][1] == round(mean([5, 2]), 1)
    assert result[2][0] == "Титов Владислав"
    assert result[2][1] == round(mean([4, 3]), 1)

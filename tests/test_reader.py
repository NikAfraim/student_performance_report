from main import read_csv_files

def test_read_csv_files(tmp_path):
    csv_file = tmp_path / "students.csv"
    csv_file.write_text(
        "student_name,subject,teacher_name,date,grade\n"
        "Семенова Елена,Английский язык,Ковалева Анна,2023-10-10,5\n"
        "Титов Владислав,География,Орлов Сергей,2023-10-12,4\n",
        encoding="utf-8"
    )

    data = read_csv_files([csv_file])
    assert len(data) == 2
    print(data)
    assert data[0]["student_name"] == "Семенова Елена"
    assert data[0]["grade"] == "5"
    assert data[1]["student_name"] == "Титов Владислав"
    assert data[1]["grade"] == "4"

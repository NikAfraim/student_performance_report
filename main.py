import argparse
import csv
from tabulate import tabulate
from reports import StudentPerformanceReport

REPORT = {
    "student-performance": StudentPerformanceReport
}


def args_parse():
    parser = argparse.ArgumentParser(
        description="Формирования отчета о студентах"
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Файлы с данными студентов"
    )
    parser.add_argument(
        "--report",
        required=True,
        choices=REPORT.keys(),
        help="Тип отчета"
    )
    return parser.parse_args()


def read_csv_files(files):
    data = []
    for file in files:
        with open(file, 'r', encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data.extend(list(reader))
    return data


def main():
    args = args_parse()
    data = read_csv_files(args.files)
    report = REPORT[args.report]()
    result = report.create(data)
    print(tabulate(result, headers="firstrow"))


if __name__ == "__main__":
    main()

import copy
import sys
import json


def load_json(path: str) -> dict:
    with open(path, 'r') as f:
        return json.load(f)


def save_json(path: str, data: dict) -> None:
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)


def insert_values(tests: list[dict], values_map: dict[int, str]) -> None:
    for test in tests:
        test_id = test.get('id')
        if test_id in values_map and test_id is not None:
            test['value'] = values_map[test_id]

        if 'values' in test:
            insert_values(test['values'], values_map)


def main(tests_path: str, values_path: str, report_path: str) -> None:
    tests = load_json(tests_path)
    values = load_json(values_path)
    values_map = {item['id']: item['value'] for item in values['values']}

    report = copy.deepcopy(tests)

    insert_values(report['tests'], values_map)
    save_json(report_path, report)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
    print("Файл report.json успешно создан")

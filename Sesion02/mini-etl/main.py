from typing import List, Dict
from reader import read_file
from validator import validate_line
from transformer import transform_line
from writer import write_file

def process_data(path: str ) ->List[Dict[str, object]]:
    """
    Orchestrates the ETL process:
    Read -> Validate -> Transform
    """

    lines = read_file(path)
    clean_data = []

    for idx, line in enumerate(lines, start=1):
        if validate_line(line):
            person = transform_line(line)
            if person:
                clean_data.append(person)
        else:
            print(f"[INVALID LINE {idx}] {line}")

    return clean_data


if __name__ == "__main__":
    data = process_data('../data/data.txt')
    write_file(data, "../data/data_clean.txt")

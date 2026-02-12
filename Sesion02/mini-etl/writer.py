# writer

from typing import List, Dict

def write_file(data: List[Dict[str, object]], path: str ) -> None:
    """
    Writes cleaned data into a new file

    """

    with open(path, 'w') as file:
        line = f"Name, Age, City\n"
        file.write(line)
        for item in data:
            line = f"{item['name']}, {item['age']}, {item['city']}\n"
            file.write(line)
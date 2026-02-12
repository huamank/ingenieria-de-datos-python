# transformer
from typing import Dict

def clean_text(text: str) -> str:
    """
    Cleans text  by removing extra spaces
    """
    return text.strip().title()


def transform_line(line: str) -> Dict[str, object]:
    """
    Transforms a valid line into a structured dictionary
    """

    try:
        name, age, city = line.strip().split(',')
        return {
            "name": clean_text(name).upper(),
            "age": int(age),
            "city": clean_text(city)
        }
    except  Exception as e:
        print('[Error]: ', line)
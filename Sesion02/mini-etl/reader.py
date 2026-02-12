# reader
from typing import List

def read_file(path: str) -> List[str]:
    """
    Reads a text file and return all lines.
    
    :param path: Path to the input file
    :type path: str
    :return: List of lines read from teh file
    :rtype: List[str]
    """

    try:
        with open(path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print("[ERROR] File not found", path)
        return[]
# validator
def validate_line(line: str) -> bool:
    """
    Validates if a line has the correct structure and valid data.

    Expected format: name, age, city
    
    Conditions:
    - Must hace exactly 3 value
    - Age must be numeric
    - Age must be >= 18
    - City must not be empty
    """

    # Gabriela,20,Cusco
    parts = line.strip().split(',') # -> retorna una lista ['Gabriela', 20, 'Cusco']
    
    if len(parts) != 3:
        return False
    
    name, age, city = parts

    if not age.isdigit():
        return False
    
    if int(age) < 18:
        return False
    
    if not city.strip():
        return False

    return True
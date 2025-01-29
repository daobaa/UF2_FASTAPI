from typing import List, Dict

def abc_schema(letter) -> Dict[str, str]:
    return{"letter": letter[0]}

def abcs_schema(letters) -> List[Dict[str, str]]:
    return [abc_schema(letter) for letter in letters]
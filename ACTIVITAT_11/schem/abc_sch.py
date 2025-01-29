def abc_schema(letter) -> dict:
    return{"type": letter[0],
           "letter": letter[1]
            }
def abcs_schema(letters) -> dict:
    return [abc_schema(letter) for letter in letters]
def tematica_schema(theme) -> dict:
    return {"theme": theme[0]}

def tematiques_schema(tematiques) -> list:
    return [tematica_schema(theme) for theme in tematiques]

def paraula_random_schema(word) -> dict:
    return {"word": word}
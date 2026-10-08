
def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError("Неверное количество полей")
    city, temp, date = parts
    if not city:
        raise ValueError("Пустой город")
    if not date:
        raise ValueError("Пустая дата")
    try:
        temperature = float(temp)
    except ValueError:
        raise ValueError("Температура должна быть числом")
    return {
        "city": city,
        "temperature": temperature,
        "date": date,
    }

def read_valid(lines: list[str]) -> list[dict]:
    records = []
    for line in lines:
        if not line:
            continue
        try:
            record = parse_record(line)
        except ValueError:
            continue
        records.append(record)
    return records
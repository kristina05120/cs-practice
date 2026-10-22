"""Функции обработки журнала метеонаблюдений.
Модуль не читает stdin и ничего не печатает — только чистые функции.
"""
def parse_record(line: str) -> dict:
    """Разбирает строку «город;температура;дата» в словарь.
    Негодная строка — ValueError.
    """
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError(f"ожидалось 3 поля, получено {len(parts)}: {line!r}")
    city, temp_raw, date = (p.strip() for p in parts)
    if not city:
        raise ValueError(f"пустой город: {line!r}")
    if not date:
        raise ValueError(f"пустая дата: {line!r}")
    try:
        temperature = float(temp_raw.replace(",", "."))
    except ValueError:
        raise ValueError(f"температура не число: {temp_raw!r}") from None
    return {"city": city, "temperature": temperature, "date": date}
def read_valid(lines: list[str]) -> list[dict]:
    #Разбирает строки журнала, пропуская пустые и негодные.
    records = []
    for line in lines:
        if line.strip() == "":
            continue
        try:
            records.append(parse_record(line))
        except ValueError:
            continue
    return records
def average_by_city(records: list[dict]) -> dict:
    """Средняя температура по каждому городу, округлённая до десятых."""
    total = {}
    count = {}
    for record in records:
        city = record["city"]
        total[city] = total.get(city, 0.0) + record["temperature"]
        count[city] = count.get(city, 0) + 1
    return {city: round(total[city] / count[city], 1) for city in total}
def warmest_city(records: list[dict]) -> str:
    """Город с наибольшей средней температурой. При равенстве — первый по алфавиту."""
    averages = average_by_city(records)
    if not averages:
        return ""
    return min(averages, key=lambda city: (-averages[city], city))
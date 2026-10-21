"""Статистика по журналу сервиса: разбор строк, подсчёт уровней, отчёт."""
LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}
def parse_event(line: str) -> dict:
    """Строка журнала 'время уровень сообщение' -> словарь.
    Негодная строка -> ValueError.
    """
    text = line.rstrip("\n")
    if not text.strip():
        raise ValueError("пустая строка")
    parts = text.split(maxsplit=2)
    if len(parts) != 3:
        raise ValueError(f"ожидались три части, получено {len(parts)}")
    time, level, message = parts
    if level not in LEVELS:
        raise ValueError(f"незнакомый уровень: {level!r}")
    return {"time": time, "level": level, "message": message}
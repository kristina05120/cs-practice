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


def count_levels(lines) -> dict:
    """Сколько строк каждого уровня; негодные — под ключом BROKEN.

    lines — любая последовательность строк (список или открытый файл).
    """
    counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1
        else:
            level = event["level"]
            counts[level] = counts.get(level, 0) + 1
    return counts


def top_errors(lines, n: int) -> list:
    """n самых частых сообщений уровня ERROR: пары [сообщение, счёт].
    При равенстве частот — по алфавиту.
    """
    freq = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            continue
        if event["level"] == "ERROR":
            msg = event["message"]
            freq[msg] = freq.get(msg, 0) + 1
    ordered = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
    return [[msg, cnt] for msg, cnt in ordered[:n]]
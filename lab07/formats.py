import json

def csv_to_records(text: str) -> list[dict]:
    if not text.strip():
        return []
    lines = text.strip().splitlines()
    if not lines:
        return []
    headers = [h.strip() for h in lines[0].split(",")]
    records = []
    for line in lines[1:]:
        if not line.strip():
            continue
        values = [v.strip() for v in line.split(",")]
        records.append(dict(zip(headers, values)))
    return records
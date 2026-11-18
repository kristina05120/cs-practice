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


def parse_settings(lines: list[str]) -> dict:
    result = {}
    current_list_key = None

    def convert(value: str):
        if value in ("true", "yes"):
            return True
        if value in ("false", "no"):
            return False

        try:
            return int(value)
        except ValueError:
            pass
        try:
            return float(value)
        except ValueError:
            pass
        return value

    for raw in lines:
        line = raw.split("#")[0].strip()
        if not line:
            continue

        if line.startswith("- "):
            if current_list_key is not None:
                result[current_list_key].append(convert(line[2:].strip()))
            continue

        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip()

            if value == "":
                result[key] = []
                current_list_key = key
            else:
                result[key] = convert(value)
                current_list_key = None

    return result

def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    result = []
    for row in rows:
        k = row.get(key)
        merged = {}
        if k is not None and k in extra:
            merged.update(extra[k])
        merged.update(row)
        result.append(merged)
    return result

def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)
from pathlib import PurePosixPath
def count_by_extension(paths: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for path in paths:
        name = PurePosixPath(path).name
        if "." in name and (not name.startswith(".") or "." in name[1:]):
            ext = name.rsplit(".", 1)[1].lower()
        else:
            ext = ""
        counts[ext] = counts.get(ext, 0) + 1
    return counts
def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    max_depth = max(p.count("/") for p in paths)
    return min(p for p in paths if p.count("/") == max_depth)
def human_size(n_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    if n_bytes < 1024:
        return f"{n_bytes} Б"
    size = float(n_bytes)
    idx = 0
    while size >= 1024 and idx < len(units) - 1:
        size /= 1024
        idx += 1
    return f"{size:.1f} {units[idx]}"
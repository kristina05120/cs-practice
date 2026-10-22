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

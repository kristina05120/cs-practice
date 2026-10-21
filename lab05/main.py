"""Читает журнал построчно, печатает сводку и пишет report.txt."""
from logstats import count_levels, top_errors, format_report
def main():
    path = input().strip()
    # Первый проход: сводка по уровням.
    with open(path, encoding="utf-8") as log:
        counts = count_levels(log)
    total = sum(counts.values())
    errors = counts.get("ERROR", 0)
    broken = counts.get("BROKEN", 0)
    print(total)
    print(errors)
    print(broken)
    # Второй проход: частые сообщения ERROR.
    with open(path, encoding="utf-8") as log:
        top = top_errors(log, 3)
    report = format_report(counts, top)
    with open("report.txt", "w", encoding="utf-8") as out:
        out.write(report)
if __name__ == "__main__":
    main()
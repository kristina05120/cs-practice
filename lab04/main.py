"""Программа: читает журнал, вызывает функции из stats.py, печатает отчёт."""
import sys
from stats import average_by_city, read_valid, warmest_city
def main() -> None:
    lines = sys.stdin.read().splitlines()
    records = read_valid(lines)
    valid_count = len(records)
    # Пропущенные из-за ошибок = непустые строки, не ставшие записями.
    non_empty = sum(1 for line in lines if line.strip() != "")
    skipped = non_empty - valid_count
    averages = average_by_city(records)
    if records:
        best = warmest_city(records)
        best_avg = averages[best]
    else:
        best_avg = 0.0
    print(valid_count)
    print(skipped)
    print(f"{best_avg:.1f}")
if __name__ == "__main__":
    main()
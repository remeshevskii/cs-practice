import sys
from stats import average_by_city, read_valid, warmest_city

def main():
    lines = sys.stdin.read().splitlines()
    valid_records = read_valid(lines)
    skipped_count = len(lines) - len(valid_records)
    best_city = warmest_city(valid_records)
    
    if best_city:
        averages = average_by_city(valid_records)
        best_temp = averages[best_city]
    else:
        best_temp = 0.0

    print(len(valid_records))     # Сколько записей разобрано
    print(skipped_count)          # Сколько строк пропущено из-за ошибок
    print(f"{best_temp:.1f}")     # Средняя температура 

if __name__ == "__main__":
    main()

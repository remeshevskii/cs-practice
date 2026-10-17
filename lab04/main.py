import sys
from stats import average_by_city, read_valid, warmest_city

def main():
    # Читаем входные данные до конца
    lines = sys.stdin.read().splitlines()
    
    # 1. Получаем список валидных записей
    valid_records = read_valid(lines)
    
    # 2. Считаем количество пропущенных строк
    # Общее количество строк минус количество валидных записей (пустые строки тоже считаются пропущенными)
    skipped_count = len(lines) - len(valid_records)
    
    # 3. Находим самый теплый город и его среднюю температуру
    best_city = warmest_city(valid_records)
    
    if best_city:
        averages = average_by_city(valid_records)
        best_temp = averages[best_city]
    else:
        best_temp = 0.0

    # Выводим результат в требуемом порядке
    print(len(valid_records))     # Сколько записей разобрано
    print(skipped_count)          # Сколько строк пропущено из-за ошибок
    print(f"{best_temp:.1f}")     # Средняя температура (с одним знаком после точки)

if __name__ == "__main__":
    main()
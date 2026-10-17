def parse_record(line: str) -> dict:
    """
    Разбирает строку формата «город;температура;дата» в словарь.
    Вызывает ValueError, если строка некорректна.
    """
    parts = line.split(";")
    
    if len(parts) != 3:
        raise ValueError("Неверное количество полей в строке")
        
    city, temp_str, date = parts
    
    if not city.strip() or not date.strip():
        raise ValueError("Город или дата не могут быть пустыми")
        
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError(f"Температура должна быть числом, получено: {temp_str}")
        
    return {
        "city": city.strip(),
        "temp": temp,
        "date": date.strip()
    }


def read_valid(lines: list):
    """
    Разбирает строки журнала, пропуская пустые и негодные.
    """
    valid_records = []
    for line in lines:
        if not line.strip():
            continue
            
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            continue
            
    return valid_records


def average_by_city(records: list):
    """
    Вычисляет среднюю температуру по каждому городу, округленную до десятых.
    """
    city_stats = {}
    
    for record in records:
        city = record["city"]
        temp = record["temp"]
        
        if city not in city_stats:
            city_stats[city] = {"sum": 0.0, "count": 0}
            
        city_stats[city]["sum"] += temp
        city_stats[city]["count"] += 1
        
    averages = {}
    for city, data in city_stats.items():
        averages[city] = round(data["sum"] / data["count"], 1)
    return averages


def warmest_city(records: list):
    """
    Находит город с наибольшей средней температурой.
    При равенстве выбирает первый по алфавиту.
    """
    if not records:
        return ""
        
    averages = average_by_city(records)
    
    best_city = None
    max_temp = float('-inf')
    for city in sorted(averages.keys()):
        temp = averages[city]
        
        if temp > max_temp:
            max_temp = temp
            best_city = city
            
    return best_city

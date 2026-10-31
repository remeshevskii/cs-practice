def parse_record(line: str) -> dict:
    parts = line.split(";")
    
    if len(parts) != 3:
        raise ValueError("Неверное количество полей в строке")
        
    city, temp_str, date = parts
    
    city = city.strip()
    temp_str = temp_str.strip()
    date = date.strip()
    
    # Проверка на пустые значения
    if not city or not date:
        raise ValueError("Город или дата не могут быть пустыми")
        
    temp_str = temp_str.replace(",", ".")
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError(f"Температура должна быть числом, получено: {temp_str}")
        
    return {
        "city": city,
        "temp": temp,
        "date": date
    }


def read_valid(lines: list[str]) -> tuple[list[dict], int]:
    valid_records = []
    error_count = 0
    
    for line in lines:
        if not line.strip():
            continue
            
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            error_count += 1
            
    return valid_records, error_count


def average_by_city(records: list[dict]) -> dict:
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


def warmest_city(records: list[dict]) -> str:
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
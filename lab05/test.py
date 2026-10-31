def parse_event(line: str) -> dict:
    parts = line.strip().split(" ", 2)
    if len(parts) != 3:
        raise ValueError("Неверный формат строки")
    
    time_str, level, message = parts
    valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR"}
    
    if level not in valid_levels:
        raise ValueError(f"Неизвестный уровень: {level}")
        
    return {"time": time_str, "level": level, "message": message}

w = parse_event(" 2026-03-01T09:12:30 W")
print(w)

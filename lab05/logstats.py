def parse_event(line: str) -> dict:
    parts = line.strip().split(maxsplit = 2)
    if len(parts) != 3:
        raise ValueError("Неверный формат строки")
    
    time_str, level, message = parts
    valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR"}
    
    if level not in valid_levels:
        raise ValueError(f"Неизвестный уровень: {level}")
        
    return {"time": time_str, "level": level, "message": message}


def count_levels(lines) -> dict:
    counts = {}
    for line in lines:
        if not line.strip():
            continue
            
        try:
            event = parse_event(line)
            level = event["level"]
            counts[level] = counts.get(level, 0) + 1
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1
            
    return counts


def top_errors(lines, n: int) -> list:
    error_counts = {}
    
    for line in lines:
        if not line.strip():
            continue
            
        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                msg = event["message"]
                error_counts[msg] = error_counts.get(msg, 0) + 1
        except ValueError:
            pass 
            
    sorted_errors = sorted(error_counts.items(), key=lambda x: (-x[1], x[0]))
    
    top_n = [[msg, count] for msg, count in sorted_errors[:n]]
    return top_n


def format_report(counts: dict, errors: list) -> str:
    lines = ["Отчёт по журналу", ""]
    
    for level in sorted(counts.keys()):
        lines.append(f"{level}: {counts[level]}")
        
    lines.append("")
    lines.append("Частые ошибки:")
    
    if not errors:
        lines.append("- (нет ошибок)")
    else:
        for err in errors:
            msg, count = err
            lines.append(f"- {msg} — {count}")
            
    return "\n".join(lines) + "\n"

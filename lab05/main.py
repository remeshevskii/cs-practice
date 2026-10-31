import logstats

def main():
    filename = input().strip()
    
    total_lines = 0
    error_lines = 0
    broken_lines = 0
    
    try:
        with open(filename, encoding="utf-8") as f:
            for line in f:
                total_lines += 1
                
                try:
                    event = logstats.parse_event(line)
                    if event["level"] == "ERROR":
                        error_lines += 1
                except ValueError:
                    broken_lines += 1
                    
        print(total_lines)
        print(error_lines)
        print(broken_lines)
        
        with open(filename, encoding="utf-8") as f:
            counts = logstats.count_levels(f)
            
        with open(filename, encoding="utf-8") as f:
            errors = logstats.top_errors(f, 3)
            
        report_text = logstats.format_report(counts, errors)
        with open("report.txt", "w", encoding="utf-8") as f:
            f.write(report_text)
            
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
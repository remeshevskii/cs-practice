import sys
from stats import average_by_city, read_valid, warmest_city, parse_record

def main():
    lines = sys.stdin.read().splitlines()

    valid_records = read_valid(lines)
    
    non_empty_lines = [line for line in lines if line.strip()]
    error_count = len(non_empty_lines) - len(valid_records)
    
    best_city = warmest_city(valid_records)
    
    if best_city:
        averages = average_by_city(valid_records)
        best_temp = averages[best_city]
    else:
        best_temp = 0.0

    print(len(valid_records))
    print(error_count)
    print(f"{best_temp:.1f}")

if __name__ == "__main__":
    main()
import sys
from stats import average_by_city, read_valid, warmest_city

def main():
    lines = sys.stdin.read().splitlines()
    
    valid_records, error_count = read_valid(lines)
    
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
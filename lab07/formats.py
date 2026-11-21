import json
import csv
import io


def csv_to_records(text: str) -> list[dict]:
    f = io.StringIO(text.strip())
    reader = csv.reader(f, skipinitialspace=True)
    try:
        headers = [h.strip() for h in next(reader)]
    except StopIteration:
        return []

    records = []
    for row in reader:
        if not row:
            continue
        cleaned_row = [val.strip() for val in row]
        record = dict(zip(headers, cleaned_row))
        records.append(record)
    return records


def _cast_value(val_str: str):
    val_str = val_str.strip()
    if not val_str:
        return ""

    if val_str in ('true', 'yes'):
        return True
    if val_str in ('false', 'no'):
        return False

    if (val_str.startswith('"') and val_str.endswith('"')) or \
       (val_str.startswith("'") and val_str.endswith("'")):
        val_str = val_str[1:-1].strip()

    numeric_str = "".join(val_str.split())

    try:
        return int(numeric_str)
    except ValueError:
        pass

    val_for_float = numeric_str.replace(',', '.')
    try:
        return float(val_for_float)
    except ValueError:
        pass

    return val_str


def parse_settings(lines: list[str]) -> dict:
    if isinstance(lines, str):
        lines = lines.splitlines()

    result = {}
    current_key = None

    for line in lines:
        line = line.replace('\t', ' ')

        if ' #' in line:
            line = line.split(' #')[0]
        elif line.strip().startswith('#'):
            continue

        line = line.strip()
        if not line:
            continue

        if line.startswith('- '):
            if current_key is not None:
                if not isinstance(result.get(current_key), list):
                    result[current_key] = []
                val_str = line[2:].strip()

                if (val_str.startswith('"') and val_str.endswith('"')) or \
                   (val_str.startswith("'") and val_str.endswith("'")):
                    val_str = val_str[1:-1].strip()

                result[current_key].append(_cast_value(val_str))
            continue

        if ':' in line:
            key, val = line.split(':', 1)
            key = key.strip()
            val = val.strip()

            current_key = key

            if not val:
                result[key] = []
            else:
                if (val.startswith('"') and val.endswith('"')) or \
                   (val.startswith("'") and val.endswith("'")):
                    val = val[1:-1].strip()

                result[key] = _cast_value(val)

    return result


def merge_by_key(rows: list[dict], extra: dict, key: str = 'id') -> list[dict]:
    merged_rows = []
    for row in rows:
        new_row = row.copy()
        row_key_val = row.get(key)

        if row_key_val in extra:
            extra_data = extra[row_key_val]
            for k, v in extra_data.items():
                if k not in new_row:
                    new_row[k] = v

        merged_rows.append(new_row)

    return merged_rows


def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)
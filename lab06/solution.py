def count_by_extension(paths: list[str]) -> dict[str, int]:
	counts = {}
	
	for path in paths:
		filename = path.split('/')[-1]
		ext = filename.rsplit('.', 1)[-1].lower() if '.' in filename else ''
		counts[ext] = counts.get(ext, 0) + 1
		
	return counts 

def deepest_path(paths: list[str]) -> str:
	if not paths:
		return ''
	sorted_paths = sorted(paths)
	
	return max(sorted_paths, key = lambda p: p.count('/'))

def human_size(n_bytes: int) -> str:
	units = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
	size = float(n_bytes)
	unt_index = 0
	
	while size >= 1024 and unit_index < len(units) - 1:
		size = size / 1024
		unit_index += 1
		
	if unit_index == 0:
		return f'{int(size)} {units[unit_index]}'
	else:
		return f'{size:.1f} {units[unit_index]}'


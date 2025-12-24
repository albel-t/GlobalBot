
def read_file_to_dict(filename):
    """Упрощенная версия для файлов без сложных случаев"""
    result = {}
    
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    current_key = None
    value_lines = []
    
    for line in lines:
        line = line.rstrip('\n')
        
        if line.startswith('-(') and ')-' in line:
            if current_key is not None:
                result[current_key] = '\n'.join(value_lines).strip()
            
            key_start = line.find('-(') + 2
            key_end = line.find(')-')
            current_key = line[key_start:key_end].strip()
            value_lines = [line[key_end + 2:].lstrip()]
        elif current_key is not None:
            value_lines.append(line)
    
    if current_key is not None:
        result[current_key] = '\n'.join(value_lines).strip()
    
    return result
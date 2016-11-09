def find_separator(string):
    for index, item in enumerate(string):
        if item==',':
            return ','
        elif item=='|':
            return '|'
        elif item==';':
            return ';'
    
    return None
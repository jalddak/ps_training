def solution(new_id):
    new_id = new_id.lower()
    temp_id = new_id
    new_id = ''
    for letter in temp_id:
        if letter.islower():
            new_id += letter
        elif letter.isdigit():
            new_id += letter
        elif letter in ['-', '_', '.']:
            new_id += letter
            
    while new_id.count('..') != 0:
        new_id = new_id.replace('..', '.')
    
    while len(new_id) != 0:
        if new_id[0] == '.':
            new_id = new_id[1:]
        elif new_id[-1] == '.':
            new_id = new_id[:-1]
        else:
            break
    
    if len(new_id) == 0:
        new_id = 'a'
        
    if len(new_id) >= 16:
        new_id = new_id[0:15]
    
    while len(new_id) != 0:
        if new_id[0] == '.':
            new_id = new_id[1:]
        elif new_id[-1] == '.':
            new_id = new_id[:-1]
        else:
            break
    while len(new_id) <= 2:
        new_id += new_id[-1]
        
                
    return new_id
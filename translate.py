def translate(text):
    rus_eng = { 
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'д': 'd',
        'е': 'e',
        'ё': 'e',
        'ж': 'Zh',
        'з': 'z',
        'и': 'i',
        'й': 'j',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'u',
        'ф': 'f',
        'х': 'h',
        'ц': 'Ts',
        'ч': 'Ch',
        'ш': 'Sh',
        'щ': 'Shch',
        'ъ': 'ъ',
        'ы': 'y',
        'ь': 'ь',
        'э': 'e',
        'ю': 'Yu',
        'я': 'Ya',
        ' ': ' ',  #это пробел
        '0': '0',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
    }
    count_word = ''
    len_text = len(text)
    if 0 < len_text:
        if text[0] == ' ':
            return 'необходимо что-то ввести: /translate привет => privet'
        for letter in text:
            if letter not in rus_eng:
                return 'К сожалению введен не допустимый символ: {}'.format(letter)
            count_word += rus_eng[letter]
    else:
        return 'необходимо что-то ввести: /translate привет => privet'
    return count_word
    
    


     
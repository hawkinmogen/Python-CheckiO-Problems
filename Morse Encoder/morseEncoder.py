# Link to my solution on CheckiO:
# https://py.checkio.org/mission/morse-encoder/publications/hawkinmogen/python-3/first/share/0bd2185dc16dce3ee128e13c75b95528/

MORSE = {'a': '.-',    'b': '-...',  'c': '-.-.',
         'd': '-..',   'e': '.',     'f': '..-.',
         'g': '--.',   'h': '....',  'i': '..',
         'j': '.---',  'k': '-.-',   'l': '.-..',
         'm': '--',    'n': '-.',    'o': '---',
         'p': '.--.',  'q': '--.-',  'r': '.-.',
         's': '...',   't': '-',     'u': '..-',
         'v': '...-',  'w': '.--',   'x': '-..-',
         'y': '-.--',  'z': '--..',  '0': '-----',
         '1': '.----', '2': '..---', '3': '...--',
         '4': '....-', '5': '.....', '6': '-....',
         '7': '--...', '8': '---..', '9': '----.'
        }
#Uses the 'MORSE' dictionary to append the morse-code equivalent for each alpha-numeric character to 'result'
def morse_encoder(text):
    text=text.lower()
    result=""
    for x in text:
        if x==' ':
            result+='  '
        else:
            result+=MORSE[x]+' '
    if result[-1]==' ':
        result=result[0:-1]
        
    return result

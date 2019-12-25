##this is an easy encryption，particularly made for store account/password/username
##the reason is that we store these information in a .txt, kind of not that safe.
##so we design simply encrytion, namely shifting the alphabet ASCII code by k position.
## so we can shift information when store, and shift it back when we load information

def k_shift_encrypt( mystring, k = 2):
    
    def upper_shift(character, k):
        # A:65 Z:90
        index = ord(character)
        shift_index = index + k
        while shift_index > 90:
            shift_index -= 26
        while shift_index < 65:
            shift_index += 26
        return chr(shift_index)

    def lower_shift(character,k):
        # a:97 z:122
        index = ord(character)
        shift_index = index + k
        while shift_index > 122:
            shift_index -= 26
        while shift_index < 97:
            shift_index += 26
        return chr(shift_index)
    def number_shift(character,k):
        # 0:48 9:57
        index= ord(character)
        shift_index = index + k
        while shift_index > 57:
            shift_index -= 10
        while shift_index < 48:
            shift_index += 10
        return chr(shift_index)
    
    def k_shift(character,k):
        if character.isupper() == True:
            return upper_shift(character,k)
        elif character.islower() == True:
            return lower_shift(character,k)
        elif character.isdigit() == True:
            return number_shift(character,k)
        else:
            return character

    shift_string=''
    for character in mystring:
        shift_string += k_shift(character,k)
    return shift_string


def k_shift_decrypt( mystring, k = 2):

    def upper_shift(character, k):
        # A:65 Z:90
        index = ord(character)
        shift_index = index - k
        while shift_index > 90:
            shift_index -= 26
        while shift_index < 65:
            shift_index += 26
        return chr(shift_index)
    
    def lower_shift(character,k):
        # a:97 z:122
        index = ord(character)
        shift_index = index - k
        while shift_index > 122:
            shift_index -= 26
        while shift_index < 97:
            shift_index += 26
        return chr(shift_index)
    
    def number_shift(character,k):
        # 0:48 9:57
        index= ord(character)
        shift_index = index - k
        while shift_index > 57:
            shift_index -= 10
        while shift_index < 48:
            shift_index += 10
        return chr(shift_index)
    
    def k_shift(character,k):
        if character.isupper() == True:
            return upper_shift(character,k)
        elif character.islower() == True:
            return lower_shift(character,k)
        elif character.isdigit() == True:
            return number_shift(character,k)
        else:
            return character

    shift_string=''
    for character in mystring:
        shift_string += k_shift(character,k)
    return shift_string
            
print(k_shift_decrypt('Lcuqp@paw.gfw Lam112327 lam'))

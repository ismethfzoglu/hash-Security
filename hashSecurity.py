import string 

def private_password(usnm, psw):

    temp = max(usnm, psw, key=len)

    private_pass = ''
    for i in range(len(temp)):
        if i % 2 == 0:
            private_pass += usnm[i] if i < len(usnm) else ''
        elif i % 2 != 0:
            private_pass += psw[i] if i < len(psw) else ''

    return private_pass
 

def deviate(any_password):
    #list of ascii printable characters
    #plain ascii list 
    ascii_printable = list(string.printable.strip())
    # Shuffling the ascii printables 
    length = len(ascii_printable)
    size = length // 40
    remainder = length % 40
    divided_lists = []
    start = 0
    for i in range(40):
        end = start + size + (1 if i < remainder else 0)
        divided_lists.append(ascii_printable[start:end])
        start = end 
    indices = [0,29, 26, 39, 23, 36, 2, 21, 4, 35, 19,37, 6, 17, 8, 15, 27, 10, 
               33, 13, 12, 11 ,34 ,31 , 25, 38, 14, 9,30 , 16, 7, 32, 18, 5, 20,
                3, 22, 1, 24,28
               ]
    shuffle_ascii = sum([divided_lists[i] for i in indices], [])
    
    deviated_password = ""
    range_aspr = int(len(shuffle_ascii))
    #apply mod according to the value of ascii printable letters
    for char in any_password:
        ascii_order =int(ord(char))
        deviated_char = ascii_order % range_aspr
        deviated_password += shuffle_ascii[deviated_char]
        
    return deviated_password


def pass_shuff(psw):
    length = len(psw)
    if length <= 1:
        return psw
    
    mid = length // 2
    left = mid - 1
    right = length-1

    shuffled_psw = []
    
    for i in range(length):
        if i % 2 == 0:
            if left >= 0:
                shuffled_psw.append(psw[left]) 
                left -= 1
            else:
                shuffled_psw.append(psw[right])
                right -= 1 
        else:
            if right != left:
                shuffled_psw.append(psw[right])
                right -= 1
            else:
                shuffled_psw.append(psw[left])
                left -= 1

    return ''.join(shuffled_psw)
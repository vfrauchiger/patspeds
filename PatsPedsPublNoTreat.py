




def treat_publno(no):
    """
    This function takes publication number US pre-grant publication or a patent number and return a tuple containing 
    a treated publication (normal format) and the type (application or patent)
    """
    # make number a string
    number = str(no)

    # treat CC
    if number[:2].upper() == 'US':
        number = number[2:]
    elif number[0].isdigit():
        pass
    else: 
        return "This is not an US Number", "unknown"

    # treat KD
    kd =''
    if number[-2].isalpha():
        kd = number[-2:]
        number= number[:-2]
    else:
        pass

    # remove whitespace
    number = number.strip()

    # remove undesired characters with in number
    number = number.replace('/', '').replace(' ', '')
    
    # make decision between application and patent
    if len(number) == 7:
        print('{} is a patent'.format(number))
        tosearch = "patentNumber"
    elif len(number) == 8:
        print('{} is a young patent'.format(number))
        tosearch = "patentNumber"
    elif len(number) == 10:
        print('{} is a short format publication'.format(number))
        number = number[:4]+'0'+number[4:]
        number = 'US'+ number +"A1"
        tosearch = "appEarlyPubNumber"
    elif len(number) == 11:
        print('{} is a USPTO format publication'.format(number))
        tosearch = "appEarlyPubNumber"
        number = 'US'+ number +"A1"


    return number, tosearch




if __name__ == "__main__":
    no = input("Supply number: ")
    print(treat_publno(no))
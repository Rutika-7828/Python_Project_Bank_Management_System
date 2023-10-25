def validName(name):
    l = name.split()
    if len(l) == 3:
        if (l[0].isalpha() and l[1].isalpha() and l[2].isalpha()):
            return True

    return False


def validNumber(number):
    if (len(number) == 10 and number.isdigit()):
        return True
    return False


def validPan(number):
    if (len(number) == 10):
        first = number[0:5]
        second = number[5:9]
        third = number[9]

        if (first.isalpha() and first.isupper() and second.isdigit() and third.isalpha() and third.isupper()):
            return True
    return False
    '''
    import re
    exp = '^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
    if(re.match(exp, number)):
        return True
    return False
    '''


def validAdhar(number):
    if (len(number) == 12 and number.isdigit()):
        return True
    return False


def validIFSC(number):
    first = number[0:4]
    second = number[5:10]

    if (first.isalpha() and number[4] == '0' and second.isdigit()):
        return True
    return False


from datetime import datetime


def validDOB(str):
    day, mon, yr = map(int, str.split('-'))
    if 1 <= day <= 31 and 1 <= mon <= 12 and 1930 <= yr <= datetime.now().year:
        if (mon in (1, 3, 5, 6, 8, 10, 12)):
            if (day <= 31):
                return True
            return False
        elif (mon == 2):
            if ((day <= 28 and yr % 4 == 1) or (day <= 29 and yr % 4 == 0)):
                return True
            return False
        else:
            if (day <= 30):
                return True
            return False
        return True
    return False

def validGender(g):
    gender = ('male', 'female', 'transgender')
    if g.lower() in gender:
        return True
    return False


def validState(state):
    st = {'Maharashtra', 'MP', 'Bihar', 'Haryana'}
    if state.title() in st:
        return True
    return False


def validCity(state, city):
    st = {'Maharashtra': {'Pune', 'Mumbai', 'Nashik', 'Nagpur'}, 'MP': {'Indore', 'Ujjain'}, 'Haryana': {'Gurugram', 'Panipat'}}
    if city.title() in st[state.title()]:
        return True
    return False


def validAccountType(acc):
    acc_Type = ('saving', 'salary', 'current')
    if acc.lower() in acc_Type:
        return True
    return False


def age(str):
    day, mon, yr = map(int, str.split('-'))
    year = datetime.now().year - yr
    if (mon, day) > (datetime.now().month, datetime.now().day):
        return year - 1
    return year


print(age('28-10-2000'))


def validAccountNumber(number):
    if (number.isdigit()):
        return True
    return False



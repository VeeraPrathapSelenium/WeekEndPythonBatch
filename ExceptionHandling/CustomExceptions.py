class Error(Exception):
    """Base class for exception"""
    pass

class InvalidAge(Error):
    """When the user age is ;ess than 18 years"""
    pass

class TooHighAge(Error):
    """ Age is too much >60 years"""
    pass


age=int(input("Please enter Age"))
print(age)

try:
    if age<=18:
        raise InvalidAge
    elif age>=65:
        raise  TooHighAge
    else:
        print("You are elegible to get bank loan")
except InvalidAge:
    print("You Age is less than or equal to 18 years , you are not eligible to get loan")
except TooHighAge:
    print("You Age is retired age, unfortunately you are not eleigible to get loan")
except:
    print("UnKnown Error")

##Implemented https://pypi.org/project/passwordmeter/
##Simple password checker that gives a rating 0 to 1 with 1 being a strong password

import passwordmeter

def checkPasswords(password):
    strength, improvements = passwordmeter.test(password)
    return password, strength, improvements

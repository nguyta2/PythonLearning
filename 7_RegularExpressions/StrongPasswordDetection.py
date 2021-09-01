import re

passWord = input('Enter your password:')

def atLeastOneUpperCase(inPassWord):
    if(re.search('[A-Z]', inPassWord)):
        return True
    else:
        return False

def atLeastOneLowerCase(inPassWord):
    if(re.search('[a-z]', inPassWord)):
        return True
    else:
        return False

def atLeastOneDigit(inPassWord):
    if(re.search('\d', inPassWord)):
        return True
    else:
        return False

if(len(passWord) >= 8 and atLeastOneUpperCase(passWord) and atLeastOneLowerCase(passWord)
and atLeastOneDigit(passWord)):
    print('This password is STRONG')
else:
    print('This password is NOT STRONG')

# if mo.group() == passWordRegex:
#     print('The password is STRONG')
# else:
#     print('The password is not STRONG', 'You need to change it')

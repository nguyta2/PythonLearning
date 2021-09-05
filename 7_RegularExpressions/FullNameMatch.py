import re

names = {'Haruto Watanabe', 'Alice Watanabe', 'RoboCop Watanabe', 'Haruto watanabe', 'haruto Watanabe', 'Mr. Watanabe', 'Watanabe'}

nameRegex = re.compile(r'^[A-Z]' + r'[A-Za-z]+' + r' Watanabe')

for name in names:
    if nameRegex.findall(name):
        print(nameRegex.findall(name))

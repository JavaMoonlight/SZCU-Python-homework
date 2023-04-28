import re

# phoneNumRegex = re.compile(r'(\(\d{3}\))?(\d{3}-)?(\d{3}-\d{4})')
phoneNumRegex = re.compile(r'(\(\d{3}\)|(\d{3}-))?\d{3}-\d{4}')
phone = input('Please enter your telephone number ：')
mo = phoneNumRegex.search('My number is '+phone)
print('Phone number found: ',mo.group())
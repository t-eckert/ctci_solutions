'''
This problem was posed by Imran Ghory: https://imranontech.com/2007/01/24/using-fizzbuzz-to-find-developers-who-grok-coding/
My writeup on the problem is at: https://www.thomaseckert.org/05-wcftf
'''

# Head
mod_dict = {
    3 : 'Fizz',
    5 : 'Buzz'
}

# Functions
def check_remainder(number):
    keys = list(mod_dict.keys())
    out = ''
    for i in range(len(mod_dict)):
        if number%keys[i] == 0:
            out = out +mod_dict[keys[i]]
    if out == '':
        return number
    else:
        return out
        
# Control
for i in range(1,101):
    print(check_remainder(i))

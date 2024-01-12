a=10

try:
    print(b) #risky code
except:
    print('error')
else:
    print('No error')
finally:
    print('always')
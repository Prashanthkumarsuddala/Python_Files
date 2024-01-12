def person(**data):
    for k,v in data.items():
        if k == 'firstname' or 'lastname':
            print(k,':',v)
        elif k == 'age':
            print(k, ' :',v)
        else:
            print(k,':',v)
person(firstname= 'Prashanth',lastname='Kumar', age= 20,mobilenum=9440350065)

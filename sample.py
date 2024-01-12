def notes(amount):
    fivehundred=amount//500
    amount -=fivehundred*500
    twohundred= amount//200
    amount -=twohundred*200
    hundred= amount//100
    amount -= hundred*100
    fifty=amount//50
    amount -=fifty*50
    twenty= amount//20
    amount -=twenty*20
    ten=amount//10
    amount -=ten*10
    five = amount//5
    amount -=five*5
    one= amount//1
    amount -=one*1
    return fivehundred,fifty, ten,five,one,twohundred,hundred,twenty

if __name__ =="__main__":
    amount=int(input('Enter the Amount: '))
    fivehundred,twohundred,hundred, fifty,twenty, ten, five, one =notes(amount)
    print('The entered amount is: ',amount)
    print('500:',fivehundred)
    print('200:',twohundred)
    print('100:',hundred)
    print('50:',fifty)
    print('20',twenty)
    print('10:',ten)
    print('5:',five)
    print('1:',one)

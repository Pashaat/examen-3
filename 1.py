def karta(nom):
    if len(str(nom)) != 16:
        print('Номер карты состоит из 16 цифр, введите номер правильно')
    else:
        print('*' * len(str(nom[:-4])) + str(nom[-4:]))

karta('1234567890123456')

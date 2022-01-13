def palindrome(slovo):
    slovo = slovo.replace(' ','').lower()
    return 'Палиндром' if slovo == slovo[::-1] else 'Не палиндром'
print(palindrome('atrt'))


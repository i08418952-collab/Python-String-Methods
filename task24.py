email = input('email: ')
natija = not email.startswith('@') and email.endswith('.com')
print(natija)
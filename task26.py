username = input('username: ')
clean = username.replace('-', '')
natija = clean.isalnum()
print(natija)
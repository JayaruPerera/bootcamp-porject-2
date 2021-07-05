import hashlib
word = str(input("Enter your word to convert to hash = "))    #taking a input from the user
result = hashlib.md5(word.encode())                           #encoding the hash
print(result.hexdigest())                                     #conver it to a hexadigit


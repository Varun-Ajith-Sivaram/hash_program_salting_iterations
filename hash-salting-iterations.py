import random
import hashlib

# characters to be chosen for salting is stored in list 'salt_list'
salt_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
             "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
             "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Str = input("Enter the string to be hashed: ")      # getting the string from user
print("Actual String: " + Str)

# number of characters to be inserted to the string for salting is stored in variable 'no_of_saltchars'
# here, number of characters is chosen at random b/w numbers 1 and 10
no_of_saltchars = random.randint(1, 10)

Strlength = len(Str)
salted_string = Str

for i in range(no_of_saltchars):
    # character to be inserted to string is chosen at random from 'salt_list' and stored in variable 'salt_char'
    salt_char = str(random.choice(salt_list))

    # position where the character is inserted is stored in variable 'saltchar_pos'
    saltchar_pos = random.randint(0, Strlength)

    salted_string = salted_string[0:saltchar_pos] + salt_char + salted_string[saltchar_pos:]
    Strlength = len(salted_string)

print("String after salting: " + salted_string)

# number of times the salted string must be iterated using MD5 algorithm is chosen at random
# b/w numbers 1 and 10, and stored in variable 'No_of_iterations'
No_of_iterations = random.randint(1, 10)

hash_salt = salted_string

for i in range(No_of_iterations):
    byte_val = hash_salt.encode()       # encoding the string to bytes
    hmd5 = hashlib.md5(byte_val)
    hash_string = hmd5.hexdigest()
    hash_salt = hash_string

print(f"Salted string after {No_of_iterations} iterations: {hash_salt}")

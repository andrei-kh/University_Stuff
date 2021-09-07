string = "JUNIOR"

new_string = ""
for c in string:
    new_string += chr(ord(c) ^ 13)

print("crypto{" + new_string + "}")

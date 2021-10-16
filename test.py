import string

bla = "gergh    terter    tert    zezer               gdfcf"

new_string = bla[:-1]
print(new_string)
print(string.capwords(bla))

strng ="fsdrmne32"
for x in strng:
    if x.isdigit():
        print(x + " digit found")
        if int(x) == 3:
            print("drei gefunden")
    else:
        print(x + " is a char")
    pass
    
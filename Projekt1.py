ODDELOVAC = "=" * 80
print(ODDELOVAC)
print("""Welcome in program "Text analysator"
A program for your text analysis that will make your work easier.""")
print(ODDELOVAC)

# 1. Vyžádání od uživatele přihlašovací jméno a heslo.
user = input("Your username: ").lower()
heslo = input("Your password: ")
print(ODDELOVAC)

# 2. + 3. Zjištění, jestli zadané údaje odpovídají někomu z registrovaných uživatelů.
registr_user = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
if registr_user.get(user) == heslo:
    print("Welcome to the app,", user)
else:
    print("This app is only for registration users.")
    print("The program will be terminated for you.")
    exit()
print("We have 3 texts to be analyzed.")
print(ODDELOVAC)

# 4. Výběr analyzovaného textu.
choose_text = int(input("Enter a number btw. 1 and 3 to select: "))
if choose_text < 1 or choose_text > 3:
    print("The text, which be analyzed, have number between 1 and 3.")
    print("The program will be terminated for you")
    exit()
print(ODDELOVAC)
# pomocné proměnné
tword = []
uword = []
lword = []
nums = []
sum_nums = []
text1 = ('''Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley.''')
text2 = ('''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''')
text3 = ('''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.''')

# 5. Pro vybraný text spočítá následující statistiky:
# a) počet slov
if choose_text == 1:
    words1 = len(text1.split(" "))
    print("There are", words1, "words in the selected text.")
    for word in text1.split(" "):
        if word.istitle():
            tword.append(1)
        if word.isupper() and word.isalpha():
            uword.append(1)
        if word.islower():
            lword.append(1)
        if word.isnumeric():
            nums.append(1)
            sum_nums.append(int(word))
elif choose_text == 2:
    words2 = len(text2.split(" "))
    print("There are", words2, "words in the selected text.")
    for word in text2.split(" "):
        if word.istitle():
            tword.append(1)
        if word.isupper() and word.isalpha():
            uword.append(1)
        if word.islower():
            lword.append(1)
        if word.isnumeric():
            nums.append(1)
            sum_nums.append(int(word))
elif choose_text == 3:
    words3 = len(text3.split(" "))
    print("There are", words3, "words in the selected text.")
    for word in text3.split(" "):
        if word.istitle():
            tword.append(1)
        if word.isupper() and word.isalpha():
            uword.append(1)
        if word.islower():
            lword.append(1)
        if word.isnumeric():
            nums.append(1)
            sum_nums.append(int(word))
print("There are", sum(tword), "titlecase words.")
print("There are", sum(uword), "uppercase words.")
print("There are", sum(lword), "lowercase words.")
print("There are", sum(nums), "numeric strings.")
print("The sum of all the numbers", sum(sum_nums))
print(ODDELOVAC)
print("LEN|  OCCURENCES        | NR.")
print(ODDELOVAC)
data = {}
symbol = "*"
if choose_text == 1:
    for word in text1.split(" "):
        if len(word) not in data:
            data[len(word)] = 1
        else:
            data[len(word)] += 1
if choose_text == 2:
    for word in text2.split(" "):
        if len(word) not in data:
            data[len(word)] = 1
        else:
            data[len(word)] += 1
if choose_text == 3:
    for word in text3.split(" "):
        if len(word) not in data:
            data[len(word)] = 1
        else:
            data[len(word)] += 1
for key, value in sorted(data.items()):
    if key >= 10:
        print(key, "|", value * symbol, (17 - value) * " ",  "|", value)
    else:
        print("", key, "|", value * symbol, (17 - value) * " ",  "|", value)

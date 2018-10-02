# NOTE: GO TO THE NUMBER FIRST DAWG

# DEFINITIONS
# Note: Runes and Letters ordering is significant and the decimal value of their index (starting at 0) corresponds to
#        the key released by Cicada 3301 in 2013.
RUNES = ["ᚠ", "ᚢ", "ᚦ", "ᚩ", "ᚱ", "ᚳ", "ᚷ", "ᚹ", "ᚻ", "ᚾ", "ᛁ", "ᛄ", "ᛇ", "ᛈ", "ᛉ", "ᛋ", "ᛏ", "ᛒ", "ᛖ", "ᛗ", "ᛚ", "ᛝ",
         "ᛟ", "ᛞ", "ᚪ", "ᚫ", "ᚣ", "ᛡ", "ᛠ"]
LETTERS = ["F", "V(U)", "TH", "O", "R", "C(K)", "G", "W", "H", "N", "I", "J", "EO", "P", "X", "S(Z)", "T", "B", "E",
           "M", "L", "NG(ING)", "OE", "D", "A", "AE", "Y", "IA(IO)", "EA"]

MODULO = len(RUNES)


# VARIABLES
test = input("Enter encrypted text: ")

running_string = ""
output = []


# DIRECT TRANSLATION
for x in test:  # iterate through entire test input
    if (x == '/') or (x == '.'):       # test for line break
        output.append(running_string)  # append to output list
        running_string = ""            # reset translated string
    elif x == '-':
        running_string += " "
    else:
        running_string += LETTERS[RUNES.index(x)]  # translate directly from rune to letter, add to string

# If translated string still has length, append it
if len(running_string):
    output.append(running_string)

# Display results
print("\nDirect Rune to Latin Alphabet Letter(s) Translation:")
print(output)

# Clear output and string
output[:] = []
running_string = ""


# ATBASH CIPHER
for x in test:  # iterate through entire test input
    if (x == '/') or (x == '.'):       # test for line break
        output.append(running_string)  # append to output list
        running_string = ""            # reset translated string
    elif x == '-':
        running_string += " "
    else:
        running_string += LETTERS[28 - RUNES.index(x)]  # translate rune to letter using atbash cipher

# If translated string still has length, append it
if len(running_string):
    output.append(running_string)

print("\nAtbash Cipher Translation:")
print(output)

shift = input("\n\nEnter shift: ")
big_string = ""
new_string = ""

# Shift
for y in output:
    big_string += " " + y

for x in big_string:
    if (x == ' ') or (x == '(') or (x == ')'):
        new_string += x
    else:
        new_string += LETTERS[(LETTERS.index(x) + int(shift)) % MODULO]

print("\nShifted Atbash Cipher")
print(new_string)

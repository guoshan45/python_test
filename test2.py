# Generate a string with N opening brackets ("[") and N closing brackets
# ("]"), in some arbitrary order. Determine whether the generated string
# is balanced; that is, whether it consists entirely of pairs of
# opening/closing brackets (in that order), none of which mis-nest.

string1 = "[]"
string2 = "]["
string3 = "[][]"
string4 = "][]["
string5 = "[[][]]"
string6 = "[]][[]"


def bracket_balanced(string):
    flag = 0
    for i in range(len(string)):
        if string[i] == "[" and flag >= 0:
            flag = flag + 1
        elif string[i] == "]" and flag >= 0:
            flag = flag - 1
        if flag < 0:
            return ("NOT OK")

    if flag == 0:
        return ("OK")
    else:
        return ("NOT OK")

print(bracket_balanced(string1))
print(bracket_balanced(string2))
print(bracket_balanced(string3))
print(bracket_balanced(string4))
print(bracket_balanced(string5))
print(bracket_balanced(string6))

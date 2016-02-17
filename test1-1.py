# Write a function char_freq() that takes a string and builds a frequency
# listing of the characters contained in it. Represent the frequency
# listing as a Python dictionary. Try it with something like
# char_freq("abbabcbdbabdbdbabababcbcbab").


def char_freq(str):
    frequency = {}
    print(str)
    for i in str:
        if i in frequency:
            frequency[i] = int(frequency.get(i)) + 1
        else:
            frequency[i] = 1
    return frequency
print(char_freq("abbabcbdbabdbdbabababcbcbab"))

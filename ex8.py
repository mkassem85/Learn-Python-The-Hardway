#base formatter
formatter = "{} {} {} {}"
#use the base formatter to do different printing
print(formatter.format(1, 2, 3, 4)) # print numbers
print(formatter.format("one", "two", "three", "four")) #print numbers as strings
print(formatter.format(True, False, False, True)) #print boolean
#print the formatter itself
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about a fear"
))

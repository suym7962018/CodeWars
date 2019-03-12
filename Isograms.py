#An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
#Implement a function that determines whether a string that contains only letters is an isogram. 
#Assume the empty string is an isogram. Ignore letter case.
def is_isogram(string):
    #your code here
    string = str.lower(string)
    n = len(string)
    i = 0
    while i != n:
        if string[i] in string[i + 1 : ]:
            return False
        i += 1
    return True
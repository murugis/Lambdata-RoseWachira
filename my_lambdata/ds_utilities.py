def enlarge(n):
    """
    Param n is a number
    Function will enlarge the number
    """
    return n * 100

# this code breaks our ability to import enlarge from other files, if left in the global scope:
#
# print("HELLO")
y = int(input("Please choose a number"))
print(y, enlarge(y))
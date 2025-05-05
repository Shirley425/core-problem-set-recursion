# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num):
    if num < 0:
        raise ValueError
    if num == 0:
        return 1
    return num * factorial(num-1)


# reverse
def reverse(text):
    if len(text) <= 1:
        return text
    return reverse(text[1:]) + text[0]


# bunny
def bunny(count):
    if count == 0:
        return 0
    return 2 + bunny(count-1)


# is_nested_parens
def is_nested_parens(parens):
    if not parens:
        return True
    if parens[0] + parens[-1] != "()":
        return False
    return is_nested_parens(parens[1:-1])
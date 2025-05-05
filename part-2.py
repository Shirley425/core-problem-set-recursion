# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not array:
        return False
    elif array[0] == query:
        return True
    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(n1, n2):
    if n1 == 0 and n2 == 0:
        return 1
    def helper(a, b):
        if a == 0 or b == 0:
            return 0
        if a % 10 == b % 10:
            return 1 + helper(a // 10, b // 10)
        else:
            return helper(a // 10, b // 10)
    return helper(n1, n2)


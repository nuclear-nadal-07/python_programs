from pip._vendor.distlib.compat import raw_input


def checkPalindrome(number):
    temp = int(number)
    reverse = 0
    while temp > 0:
        remainder = int(temp % 10)
        reverse = (reverse * 10) + remainder
        temp = int(temp / 10)
    if reverse == int(number):
        return True
    else:
        return False


input = int(raw_input("Enter the number "))

#print the number if it is palindrome
#else iterate in indremental and decremental order to find the nearest palindrome
if checkPalindrome(input):
    print("{} is a palindrome".format(input))
else:
    forward_count = 0
    reverse_count = 0
    temp = int(input)

    # Loop till finding the palindrome number in incremental order
    # and store the count in forward_count variable
    while not checkPalindrome(temp):
        forward_count = forward_count + 1
        temp = temp + 1

    temp = int(input)
    # Loop till finding the palindrome number in decremental order
    # and store the count in reverse_count variable

    while not checkPalindrome(temp):
        reverse_count = reverse_count + 1
        temp = temp - 1

    # Determining the nearest palindrome number
    # by comparing the forward_count and reverse_count

    if forward_count < reverse_count:
        print(input + forward_count)
    elif forward_count == reverse_count:
        print(input - reverse_count)
        print(input + forward_count)
    else:
        print(input - reverse_count)

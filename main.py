# Check if a word is an anagrams
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


# def find_anagrams(word):
# [assignment] Add your code here
#   return True

# code on anagram
# str1 = "Race"
# str2 = "Care"

print("Welcome to Anagram finder")
is_running = True

while is_running:

    str1 = input("Enter first string:")
    str2 = input("Enter second string:")

    # convert both the strings into lowercase
    str1 = str1.lower()
    str2 = str2.lower()

# check if length is same
    if(len(str1) == len(str2)):

        # sort the strings
        sorted_str1 = sorted(str1)
        sorted_str2 = sorted(str2)

    # if sorted char arrays are same
        if(sorted_str1 == sorted_str2):
            print(str1 + " and " + str2 + " are anagram.")
        else:
            print(str1 + " and " + str2 + " are not anagram.")

    else:
        print(str1 + " and " + str2 + " are not anagram.")

    choice = input("Would you like to run another calculation. [y,n] :")
    if choice == "y":
        pass

    if choice == "n":
        is_running = False
    # This is the same thing as a break.

print("Thanks for using the Anagram finder, bye bye...")

#For this assignment use the words.txt file.
#Read in all the words. Count how many are palindromes, or words that are spelled the same forwads and backwards.
#For example, wow is a paldindrome.
#A different file wile be used for grading.
#Correct answer for this file: 

wordsTxt = open("words.txt")

wordsList = wordsTxt.read().splitlines()

wordsReverse = []

palindromeCount = 0

for x in wordsList:
    wordsReverse.append(x[::-1])

for x in wordsReverse:
    for y in wordsList:
        if x == y:
            palindromeCount += 1

print(f"The number of palindromes in the list is {palindromeCount}")
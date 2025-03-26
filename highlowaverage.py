#For this assignment use the numbers.txt file.
#A different numbers.txt will be used for grading.
#Read in all the numbers. Display the following information:
#How many numbers in the file
#Total of all the number
#Average
#Highest number
#Lowest number
#Correct answers for the included file:

numbersTxt = open("numbers.txt")

numbersList = numbersTxt.read().splitlines()

numbersTxt.close()

numbers = [int(x) for x in numbersList]

# was so happy to find splitlines, the \n was killing me

print(f"The amount of numbers in the file is {len(numbers)}")
print(f"The sum of the numbers in the file is {sum(numbers)}")
print(f"The average of the numbers is {sum(numbers)/len(numbers)}")
print(f"The highest number in the list is {max(numbers)}")
print(f"The lowest number in the list is {min(numbers)}")
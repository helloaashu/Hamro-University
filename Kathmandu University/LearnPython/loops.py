"""Showcase different loop constructs."""

numbers = [1, 2, 3, 4, 5]
print("For loop results: ")
for number in numbers:
    print(number * number, end=" ")
print("\n")

print("While loop countdown: ")
count = 3
while count > 0:
    print(count)
    count -= 1
print("Blast off!\n")

print("List comprehension example: ")
squares = [n * n for n in numbers if n % 2 == 1]
print("Odd squares:", squares)

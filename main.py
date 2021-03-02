
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


input_string = input("write here").split()
first_letters = []
for i in range(len(input_string)):
    first_letters.append(input_string[i][0])
print(first_letters)
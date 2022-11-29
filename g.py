#create an empty list
goals = []

#append the goals
n = int(input("How many goals do you want?"))
for i in range(5):
    new = input("Add a new goal to the list: ")
    goals.append(new)

print(goals)
#edit an item
i = input('which goal do you want to chage? ')
# convert i from string to the integer
i = int(i)
goal[i] = input('Enter a new goal: ')

print(goals)

#delete an item
i = int(input('Which goal do you want to delete? '))
del goals[i-1]
print(goals)
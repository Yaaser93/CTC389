#Muhammad Mahmood
#Lab 6

students = ["mike","john","sarah","lily","jake"]

print("1. Add student to list")
print("2. Modify student name")
print("3. Remove student")

choice = int(input("Choose one of the above options using the option number. "))

if choice == 1:
    name = str(input("Input the new student's name. "))
    students.append(name)
    for i in students:
        print(i)

if choice == 2:
    print("mike, 0")
    print("john, 1")
    print("sarah, 2")
    print("lily, 3")
    print("jake, 4")
    change = int(input("Select the index number of the student you want to modify. "))
    if change == 0:
        students.pop(0)
        newname1 = str(input("Input the new name. "))
        students.insert(0, newname1)
        for i in students:
            print(i)
    if change == 1:
        students.pop(1)
        newname2 = str(input("Input the new name. "))
        students.insert(1, newname2)
        for i in students:
            print(i)
    if change == 2:
        students.pop(2)
        newname3 = str(input("Input the new name. "))
        students.insert(2, newname3)
        for i in students:
            print(i)
    if change == 3:
        students.pop(3)
        newname4 = str(input("Input the new name. "))
        students.insert(3, newname4)
        for i in students:
            print(i)
    if change == 4:
        students.pop(4)
        newname5 = str(input("Input the new name. "))
        students.insert(4, newname5)
        for i in students:
            print(i)

if choice == 3:
    print("mike, 0")
    print("john, 1")
    print("sarah, 2")
    print("lily, 3")
    print("jake, 4")
    remove = int(input("Select the index number of the student you want to remove. "))
    if remove == 0:
        students.pop(0)
        for i in students:
            print(i)
    if remove == 1:
        students.pop(1)
        for i in students:
            print(i)
    if remove == 2:
        students.pop(2)
        for i in students:
            print(i)
    if remove == 3:
        students.pop(3)
        for i in students:
            print(i)
    if remove == 4:
        students.pop(4)
        for i in students:
            print(i)


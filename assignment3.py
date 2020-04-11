print("user defined programs")
print("Press 1 for assigning the elements to different list")
print("Press 2 for accessing elements from tuple")
print("Press 3 for updating a Dictionary")
ch=int(input("enter your choice = "))

if ch==1:                                            #program to assign data in different lists
    print("\nassigning user defined list")
    print("press 1 for int tpye list")
    print("press 2 for string type list")
    print("press 3 for float type list")
    x = int(input("enter your choice:"))

    if x == 1:
        print("\nUser defined lists of int type  ")
        list = []                                                # initially make a empty list
        n = int(input("enter the number of elements:"))            # user defined number
        for i in range(0, n):
            element = int(input())                             # defined for values of element
            list.append(element)                                 # adding new element at last
        print("input :", end=" ")
        print("list", list)

    elif x == 2:
        print("\nuser defined lists of string type")
        list = []
        n = int(input("enter the number of elements:"))
        for i in range(0, n):
            element = str(input())                                #Data type is string
            list.append(element)
        print("input :", end=" ")
        print("list", list)

    elif x == 3:
        print("\nuser defined lists of float type")
        list = []
        n = int(input("enter the number of elements:"))
        for i in range(0, n):
            element = float(input())                                 #Data type is float
            list.append(element)
        print("input :", end=" ")
        print("list", list)

    else:
        print("invalid choice")


elif ch==2:                                                        #program to access the elements from tuple
    print("\naccesing elements from tuple")
    num = (12, 24, 25, 67, 69, 30)
    print(num)
    print("press a to fetch single element through index number:")      #fetch element from index
    print("press b to fetch elements within a range:")                    #fetch elements using range
    print("press c to fetch elements from a given point:")             #fetch elements from a particular point
    x = str(input("enter the choice:"))
    if x == 'a':
        i = int(input("enter the index value (less than 5 or 5):"))
        print(num[i])

    elif x == 'b':
        i = int(input("enter the starting point of range:"))
        j = int(int(input("enter the ending point of range(less than 5 or 5):")))
        print(num[i:j])

    elif x == 'c':
        i = int(input("enter the given point :"))
        print(num[i:])

    else:
        print("invalid choice")


elif ch==3:                                       #program to create/remove elements from dictionary using lists
    print("\nuser defined dictonary")
    keys = []
    k = int(input("enter the number of keys:"))
    for i in range(1, k + 1):
        print("enter the key no.", i, "=", end=" ")
        ele = input()
        keys.append(ele)

    values = []
    j = int(input("enter the number of values:"))
    for j in range(1, j + 1):
        print("enter the value no.", j, "=", end=" ")
        ele = input()
        values.append(ele)

    dictionary = dict(zip(keys, values))                     #zip func. is used to combined the two lists
    print("dictionary =", dictionary)

    x = (input("enter the key  whose value you want delete:"))
    dictionary.pop(x)
    print("updated dictionary =", dictionary)

else:
    print("sorry wrong choice")

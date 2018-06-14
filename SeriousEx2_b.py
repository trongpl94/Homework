choic = input("Welcome to our shop, what do u want?(C, R, U, D)").upper()
item = ['T-Shirt','Sweater']
if choic =="R":
    print("Our Items: ",*item)
    choic = input("Welcome to our shop, what do u want?(C, R, U, D)").upper()
if choic =="C":
    new_item = input("Enter new Item: ")
    item.append(new_item)
    print("Our Item",*item)
    choic = input("Welcome to our shop, what do u want?(C, R, U, D)").upper()
if choic =="U":
     update_posi = int(input("Update Position: "))
     if update_posi < 0:
        print("Nothing was update!")
        choic = input("Welcome to our shop, what do u want?(C, R, U, D)").upper()
     else:
         if update_posi > len(item):
             new_item2 = input("New Items?")
             item.append(new_item2)
             print("We having updated in last position!")
             print("Our Items:", *item)
             choic = input("Welcome to our shop, what do u want?(C, R, U, D)").upper()
         else:
             del(item[update_posi-1])
             new_item2 = input("New Items?")
             item.insert(update_posi-1,new_item2)
             print("Our Items:",*item)
             choic = input("Welcome to our shop, what do u want?(C, R, U, D)").upper()
     choic = input("Welcome to our shop, what do u want?(C, R, U, D)").upper()
if choic =="D":
    del_position = int(input("Delete position, if u enter 0, nothing will be delete: "))
    if del_position < 0:
        print("Nothing was delete!")
        choic = input("Welcome to our shop, what do u want?(C, R, U, D)").upper()
    else:
        if del_position > len(item):
            print("We don't have ",del_position,"items")
            choic = input("Welcome to our shop, what do u want?(C, R, U, D)").upper()
        else:
         del(item[del_position-1])
         print("Our Items:",*item)
         choic = input("Welcome to our shop, what do u want?(C, R, U, D)").upper()





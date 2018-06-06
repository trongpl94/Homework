sheep_list = [5,7,300,90,24,50,75]
print("Hello Mother F****, my name is Long and these are my ship sizs:")
print(sheep_list)
max_size = sheep_list[0]
month = 0
for i in range(len(sheep_list)):
    if sheep_list[i] > max_size:
        max_size = sheep_list[i]
print("Now my biggest sheep has size",max_size,"let's shear it!","\n")
defult_size = 8
location = sheep_list.index(max_size)
sheep_list[location] = 8
print("After shearing, here is my flock: ", sheep_list, "\n")
for j in range(len(sheep_list)):
    sheep_list[j] += 50
    sheep_list_nextmonth = sheep_list
for month in range(0,int(input("How many months do u want to feed the Sheeps: ?"))):
    month += 1
    print("MONTH:", month, sep="")
    print("Hello Mother F**** again, one month has passed, these are my flock:","\n")
    print(sheep_list_nextmonth,"\n")
    max_size_next = sheep_list_nextmonth[0]
    for a in range(len(sheep_list_nextmonth)):
        if sheep_list_nextmonth[a] > max_size_next:
            max_size_next = sheep_list_nextmonth[a]
    print("Now my biggest sheep has size", max_size_next, "let's shear it!", "\n")
    defult_size_next = 8
    location_next = sheep_list_nextmonth.index(max_size_next)
    sheep_list_nextmonth[location_next] = 8
    print("After shearing, here is my flock: ", sheep_list_nextmonth, "\n")
    for k in range(len(sheep_list_nextmonth)):
        sheep_list_nextmonth[k] += 50





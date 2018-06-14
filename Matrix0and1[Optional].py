n = int(input("Enter ur N:"))
for a in range(0, n):
 if a % 2 == 0:
  for j in range(0, n):
        if j % 2 == 0:
            print(1, end=" ")
        if j % 2 == 1:
            print(0,end=" ")
  print("\t")
 if a % 2 == 1:
  for i in range(0, n):
        if i % 2 == 1:
            print(1, end=" ")
        if i % 2 == 0:
            print(0, end=" ")
  print("\t")

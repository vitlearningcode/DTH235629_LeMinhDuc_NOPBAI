print("* * * *")
print("*     *")
print("*     *")
print("* * * *")

print("\n")

width = 5
height = 4


for i in range(height):

  if i == 0 or i == height - 1:
    print("* " * width)
  else:
    print("* " + "  " * (width - 2) + "*")
from random import randint

# Build Array with no repeats
list = []
for i in range(10):
   int = randint(1,30)
   while int in list:
      int = randint(1,30)
   list.append(int)

print "Partition Element is: " + str(list[0])
print list
print "Show solution?"

raw_input()

boundary = 0

for i in range(1,10):
   if list[i] < list[0]:
      temp = list[i]
      list[i] = list[boundary + 1]
      list[boundary + 1] = temp
      boundary += 1
temp = list[0]
list[0] = list[boundary]
list[boundary] = temp

print list

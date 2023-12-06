input = open("input.txt").readlines()
sum2 = 0

nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

#part 1
# for line in input:
#   arr = []
#   for char in line:
#     if char.isdigit():
#       arr.append(int(char))
#   sum1 += arr[0] * 10 + arr[-1] 
  
#part 2
for line in input:
  arr = []
  for i, char in enumerate(line):
    for j, num in enumerate(nums):
      if num in line[i:i + len(num)]:
        arr.append(j + 1)
    if char.isdigit():
      arr.append(int(char))
  sum2 += arr[0] * 10 + arr[-1]  

print(sum2)
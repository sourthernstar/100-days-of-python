# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

times=len(student_heights)
total=0
count=0
while (count<times):
    total+=student_heights[count]
    count+=1
print(round(total/times))


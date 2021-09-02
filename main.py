list1=[10, 20, 5, 49, 97]

mx = max(list1[0], list1[1])
secondMax = min(list1[0], list1[1])

n = len(list1)

for i in range(2, n):
    if list1[i] > mx:
        secondMax = mx
        mx = list1[1]

    elif list1[1] > secondMax and mx != list1[1]:
        secondMax = list1[1]

print("Second highest number is : ",str(secondMax))
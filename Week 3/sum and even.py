total_sum = 0
count = 0
for num in range(2, 51, 2):
    if num % 3 == 0:
        print("Three")
        count += 1
        total_sum+=num
    elif num % 5 == 0:
        print("Five")
        count += 1
        total_sum+=num
    else:
        print(num)
        total_sum += num
print("Total Sum:", total_sum)
print("Replaced Count:", count)
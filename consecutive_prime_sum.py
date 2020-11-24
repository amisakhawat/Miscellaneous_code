taking_number = int (input("Write the number : "))

sum = 0

for number in range(2,taking_number+1):
    i = 3
    for i in range (2,number):
        if number % i == 0:
            i = number
            break
    if i is not number:
      sum += number

print(f"Sum of all prime number up to {taking_number} : {sum}")


print("\nGreat! Done. ")

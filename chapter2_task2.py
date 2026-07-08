age = int(input("Enter your age " ))
is_birthday = input("Is today your birthday? (yes/no): ")

if is_birthday == "yes":
    price = 0
elif age < 18 or age > 60:
    price = 100
else: 
    price =200


print(f"your price is: ${price}")


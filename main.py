from calculator import add, subtract, multiply, divide, power
from user import User
from utils import greet


print(greet("Sanjeet"))

print("\n----- Calculator -----")
print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))
print("Power:", power(2, 3))

print("\n----- User Details -----")
user = User("Sanjeet Kumar", "sanjeet@example.com")
user.display_user()




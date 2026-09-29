"""
PREDICT THE OUTPUT
Topics: lists, tuples, f-strings (formatted print), type conversions, if-elif-else

Directions:
  1. Do NOT run this file yet.
  2. Read each section and write down exactly what you think it will print.
  3. Run the file and compare your predictions to the real output.
  4. For any line you missed, figure out WHY before moving on.
"""

# ------------------------------------------------------------
# Section 1: Lists
# ------------------------------------------------------------
import string


print("--- Section 1: Lists ---")
bikes = ['trek', 'cannondale', 'redline', 'specialized']
print(bikes[0].title())
print(bikes[-1])
print(len(bikes))

bikes.append('giant')
bikes.insert(1, 'schwinn')
print(bikes)

popped = bikes.pop()
print(f"I sold my {popped.title()}.")

bikes.remove('redline')
print(bikes)
print(bikes[0:3])

# ------------------------------------------------------------
# Section 2: Sorting and list math
# ------------------------------------------------------------
print("\n--- Section 2: Sorting ---")
scores = [88, 72, 95, 60, 72]
print(sorted(scores))
print(scores)          # was the original list changed?
scores.sort(reverse=True)
print(scores)
print(min(scores), max(scores), sum(scores))

squares = [n ** 2 for n in range(1, 6)]
print(squares)

# ------------------------------------------------------------
# Section 3: Tuples
# ------------------------------------------------------------
print("\n--- Section 3: Tuples ---")
dimensions = (200, 50)
print(dimensions[0])
print(f"Width: {dimensions[0]}, Height: {dimensions[1]}")


# ------------------------------------------------------------
# Section 4: Type conversions
# ------------------------------------------------------------
print("\n--- Section 4: Type Conversions ---")
age = "17"
print(age + "1")
print(int(age) + 1)
print(str(5) * 3)
print(float(7.9))
print(float(3))


# ------------------------------------------------------------
# Section 5: f-strings
# ------------------------------------------------------------
print("\n--- Section 5: f-strings ---")
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

price = 19.5
qty = 3
print(f"Total: ${price * qty:.2f}")
print(f"{qty} items x ${price} = ${price * qty}")
print(f"{'left':<8}|{'right':>8}|")


# ------------------------------------------------------------
# Section 6: if-elif-else
# ------------------------------------------------------------
print("\n--- Section 6: if-elif-else ---")
age = 12
if age < 4:
    cost = 0
elif age < 18:
    cost = 25
elif age < 65:
    cost = 40
else:
    cost = 20
print(f"Your admission cost is ${cost}.")

# Order matters! Which branch runs?
temp = 85
if temp > 60:
    print("Warm")
elif temp > 80:
    print("Hot")
else:
    print("Cold")

# Several independent if statements (not elif)
toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in toppings:
    print("Adding mushrooms.")
if 'pepperoni' in toppings:
    print("Adding pepperoni.")
if 'extra cheese' in toppings:
    print("Adding extra cheese.")

# Empty list check
orders = []
if orders:
    print("We have orders!")
else:
    print("No orders yet.")

# ------------------------------------------------------------
# Section 7: Putting it all together
# ------------------------------------------------------------
print("\n--- Section 7: Challenge ---")
raw_grades = ["91", "78", "85", "64", "100"]
grades = [int(g) for g in raw_grades]
average = sum(grades) / len(grades)

if average >= 90:
    letter = 'A'
elif average >= 80:
    letter = 'B'
elif average >= 70:
    letter = 'C'
else:
    letter = 'F'

print(f"Grades: {grades}")
print(f"Average: {average:.1f} -> {letter}")

student = ("Maria", letter)
name, final = student          # tuple unpacking
print(f"{name} earned a(n) {final}.")
print(raw_grades[0] + raw_grades[1])
print(grades[0] + grades[1])

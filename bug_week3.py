# bug_week3.py
# Follow the SAME structured debugging process from Weeks 1 and 2.
# Verify your code against the master test case (what the output should look like)
# ============================================================

# --- OUR LIST OF PLANETS ---
# This line is correct — no bug here.
planets = ["mercury", "venus", "earth", "mars", "jupiter", "saturn"]


print("--- All Planets ---")
for planet in planets:                   
    print(planet.title())                   # BUG 1  
print("  (part of our solar system)")   # <-- should this be inside or outside?

# Inner solar system planets are Mercury, Venus, Earth, and Mars.  The outer solar system planets are Jupiter, Saturn, Uranus, and Neptune.
print("\n--- Counting Planets (inner solar system) ---")
for number in range(0, 4):              # BUG 2
     print(planets[number].title() + " is an inner solar system planet.")

# ============================================================
# BUG 3
# BUG HINT: Read about numerical list functions or google "Python list built-in functions"
#           You can a total list of built-in functions here: https://www.w3schools.com/python/python_ref_functions.asp
#           min(), max(), and sum() are built-in functions.
#           What is the correct syntax for calling a function?
#           Compare how you call a function vs. a list method (e.g. insert or append).
# ============================================================
scores = [88, 95, 70, 100, 83]
print("\n--- Test Score Stats ---")
print("Lowest: " + str(min(scores)))
print("Highest: " + str(max(scores)))
print("Total points: " + str(sum(scores)))

# ============================================================
# BUG 4
# BUG HINT:   
# If you see a code pattern you don't recognize, google it!  
# If you don't know the name of it, google "what is this python code called" and copy/paste the code into the search bar.  
# You will find a name for it, and then you can google that name to learn more about it.
# ============================================================
print("\n--- Squared Numbers ---")
squares = [number**2 for number in range(1, 6)]
for square in squares:
    print(square)


"""
@author : code8080.in

Using break statement: The loop breaks when i becomes 4.
Using continue statement: The loop skips the iteration when i is 3.
Using else clause with for loop: The else block runs after the loop completes.
Using else clause with for loop and break: The else block does not run because the loop was terminated by a break.
Using else clause with while loop: Similar to the for loop, the else block runs after the loop completes.
Using else clause with while loop and break: The else block does not run because the loop was terminated by a break.
"""

# Using break statement
print("Using break statement:")
for i in range(1, 6):
    if i == 4:
        print("Breaking the loop at i =", i)
        break
    print("i =", i)

# Using continue statement
print("\nUsing continue statement:")
for i in range(1, 6):
    if i == 3:
        print("Skipping the loop iteration at i =", i)
        continue
    print("i =", i)

# Using else clause with for loop
print("\nUsing else clause with for loop:")
for i in range(1, 4):
    print("i =", i)
else:
    print("This will run after the for loop completes.")

# Using else clause with for loop and break
print("\nUsing else clause with for loop and break:")
for i in range(1, 6):
    if i == 4:
        print("Breaking the loop at i =", i)
        break
    print("i =", i)
else:
    print("This will not run because the loop was terminated by a break.")

# Using else clause with while loop
print("\nUsing else clause with while loop:")
count = 1
while count < 4:
    print("count =", count)
    count += 1
else:
    print("This will run after the while loop completes.")

# Using else clause with while loop and break
print("\nUsing else clause with while loop and break:")
count = 1
while count < 6:
    if count == 4:
        print("Breaking the loop at count =", count)
        break
    print("count =", count)
    count += 1
else:
    print("This will not run because the loop was terminated by a break.")

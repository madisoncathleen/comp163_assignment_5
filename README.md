# comp163_assignment_5

# YURRRRR back at it again with the assignments
# lemme read the dang doc hollup
# OKAY OKAY OKAAAAAY! OH KAY OH KAY OH KAY CODE IS OUT AND CODE IS OUT AND OO CODEY CODEY CODEY CODEY CODEY
#CHATGPT was used for bug fixing and minor help in the 3rd part.

print("=== Challenge 1: Collatz Conjecture ===")
output1 = ""
step_count = 0
current_number = int(input("Enter starting number: "))
if current_number >= 0:
        print(f"Sequence: {round(current_number)}", end=" ") # adding the first number to visual representation
        while current_number != 1: # using a while loop cuz idk how many times its gonna run
            step_count += 1
            if current_number % 2 == 0: # if even number
                current_number /= 2
            else: # if odd number 
                current_number *= 3
                current_number += 1
            print(f"{round(current_number)}", end=" ") # adding sequence to visual representation
if current_number == 1:
    print(output1)
    print(f"Steps: {step_count}")


#---------------------------------------------------------------------------------------------------------------

print()
print("=== Challenge 2: Prime Number Checker ===")
current_number = int(input("Enter a number: ")) # grabbing input yes yes
found_divisor = True
if current_number > 0:
    for meow in range (2,current_number): # checking every number 2 through the number (for loop because I DO know how many times)
        if current_number % meow == 0: # yippee! making sure it aint disvisible 
               found_divisor = False
               break
        
        
        else:
               found_divisor = True
else:
    found_divisor = False

print(f"Testing divisors from 2 to {current_number - 1}...")
if found_divisor:
    print(f"{current_number} is prime!")
else:
    print(f"{current_number} is not prime (divisible by 3)")
print()

#---------------------------------------------------------------------------------------------------------------

print("=== Challenge 3: Multiplication Table ===")
print("Multiplication Table:")

print("   ", end="")   # empty space in the cornerrrrr
for col in range(1, 11):
    print(f"{col:4}",end="")   # printing the col numbaas
print()

# Print rows
for row in range(1, 11): # (for loop because i do know how many times i want it to run
    print(f"{row:2} ", end="")   # row numbersss
    for col in range(1, 11):
        product = row * col
        print(f"{product:4}", end="")   # printing the stuff yes yes
    print()   # movin to next line



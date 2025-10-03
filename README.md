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

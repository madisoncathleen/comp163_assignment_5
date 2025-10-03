# YURRRRR back at it again with the assignments
# lemme read the dang doc hollup
# OKAY OKAY OKAAAAAY! OH KAY OH KAY OH KAY CODE IS OUT AND CODE IS OUT AND OO CODEY CODEY CODEY CODEY CODEY

print("=== Challenge 1: Collatz Conjecture ===")
output1 = ""
step_count = 0
current_number = int(input("Enter starting number: "))
if current_number >=0:
        output1 += str(round(current_number))
        output1 += " "
        while current_number != 1:
            step_count += 1
            if current_number % 2 == 0:
                current_number /= 2
            elif current_number % 2 != 0:
                current_number *= 3
                current_number += 1
            output1 += str(round(current_number))
            output1 += " "

print(f"Sequence: {output1}")
print(f"Steps: {step_count}")

print()
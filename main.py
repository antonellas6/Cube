# Antonella Sanchez
# 11/9/2023
#CUBES / CUBES / CUBES sequence: 1, 8, 27, 64, 125
# Give number N(Limit) as static input and store in a variable
given_number = int(input("Enter a number between 1 to 5: "))
counter = 1

# loop until counter is less or equal to the given number
# using the given number in a while loop

while counter <= given_number:
    # inside the loop multiply the counter with itself 3 times
    # and store it another variable
    # n*n*n == cubed == n*3
    cube = counter ** 3
    # print the cube variable separated with spaces
    print(cube, end=" ")
    #increment counter by 1
    counter += 1
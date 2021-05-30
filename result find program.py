
# Find your result of exam

marks= int(input("Enter your makrs :"))

if marks >= 80 and marks <= 100:
    print("You got A+")
elif marks >= 70 and marks <= 79:
    print("You got A-")
elif marks >= 60 and marks <= 69:
    print("you got A")
elif marks >= 50 and marks <= 59:
    print("You got B")
elif marks >= 40 and marks <= 49:
    print("You got B-")
elif marks >= 30 and marks <= 39:
    print("You got C")
elif marks >= 0 and marks <= 29:
    print("Sorry! you got F")
else :
    print ("Your number is not in 1 to 100. Please try again.")

    

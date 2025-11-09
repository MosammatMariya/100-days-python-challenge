print("Welcome to the Tip Calculator")
bill=float(input("What was the total Bill?\n"))
tip=int(input("How much tip you want to give? 10%, 12% or 15%\n"))
people=int(input("How many people to split the bill?\n"))
tip2=bill*tip
result=(bill+tip2)/people
result=round(result,2)
print("Each person should pay: " + str(result))

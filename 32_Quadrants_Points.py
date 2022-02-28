# X  is positive integer as well as Y is also positive a integer it signifies first quadrant.
# X  is negative integer but Y is positive integer it signifies second quadrant.
# X  is negative integer as well as Y is also negative integer it signifies third quadrant.
# X  is positive integer but Y is negative integer it signifies fourth quadrant.

# If ( x>0 and y>0 ) First Quadrant
# If ( x<0 and y>0 ) Second Quadrant
# If ( x<0 and y<0 ) Third Quadrant
# If ( x>0 and y>0 ) Fourth Quadrant
# If ( x=0 and y=0 ) Origin
# If ( x!=0 and y=0 ) x-axis
# If ( x>0 and y>0 ) y-axis

x,y=map(int,input("Enter the values of x and y co-ordinate:").split(","))
if x>0 and y>0:
    print(f"{x} and {y} are in First Quadrant")
elif x<0 and y>0:
    print(f"{x} and {y} are in Second Quadrant")
elif x<0 and y<0:
    print(f"{x} and {y} are in Third Quadrant")
elif x>0 and y<0:
    print(f"{x} and {y} are in Fourth Quadrant")
elif x==0 and y==0:
    print(f"{x} and {y} are at Origin Axis")
elif x!=0 and y==0:
    print(f"{x} and {y} are on x-axis")
else:
    print(f"{x} and {y} are on y-axis")

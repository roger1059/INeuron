
# Problem 1
for i in range(2000,3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i,end=',')
print()
print("--------------------------------")
# Problem 2
f_name = input("First name: ")
l_name = input("Last name: ")
rf_name = f_name[::-1]
rl_name = l_name[::-1]
print(rf_name + " " + rl_name)
print()
print("--------------------------------")
# Problem 3
import math
diameter = 12
r = diameter/2
v = (4/3)*math.pi*r**3
print("Volume of Sphere:{}".format(v))

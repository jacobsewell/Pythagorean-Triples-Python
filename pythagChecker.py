'''
This program takes in 3 user input values and returns whether or not they are considered a pythagorean triple.
'''

#include math.h

print("Please enter a value for a");
a = int(input());

print("Please enter a value for b");
b = int(input());

print("Please enter a value for c");
c = int(input());


asq = a * a;

bsq = b * b;

csq = c * c;

if(asq + bsq == csq):
    print("The values you entered, " + str(a) + ", " + str(b) +", " + str(c) + " make up a pythagorean triple.");
else:
     print("The values you entered, " + str(a) + ", " + str(b) +", " + str(c) + " do not make up a pythagorean triple.");

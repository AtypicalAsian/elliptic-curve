12-Mar-2024
Nicolas Nguyen
CS401 - Prof. Duncan Buell
Denison University
___________________________________________________________________________

		            	Elliptic Curves

This project is designed to explore and demonstrate the mathematical properties
and cryptographic applications of elliptic curves. It involves implementing 
key operations on elliptic curves over finite fields, such as point 
addition, point doubling and point order count, which are foundational 
for elliptic curve cryptography (ECC).
___________________________________________________________________________

    Files                                Description
    ------------------    ----------------------------------------------   
    ecurve.py   	  Elliptic Curve Class Implementation with Jacobian 
			  coordinates
    main.py   	          Main program to run computation on elliptic curves
    curves.txt            Input parameters for elliptic curves (a, b, p)
    output.txt  	  File to write the results to
    zsampledata.txt   	  Sample output data provided by Dr. Buell

___________________________________________________________________________

                        ELLIPTIC CURVE CLASS FEATURES

1. Point Addition: Allows the addition of two distinct points on the elliptic 
		   curve in Jacobian coordinates

2. Point Doubling: Allows the same point to be added to itself

3. Find Points: Generate all points on the curve modulo a prime 

4. Invert Z-coordinate: Normalizes the point in Jacobian coordinates by converting 
		        Z to 1, which facilitates easier interpretations

5. Validate Coefficients: Checks if the provided coefficients (a and b in the equation 
			  y^2 = x^3 + ax + b) for the elliptic curve satisfy the 
			  non-singularity condition (4a^3 + 27b^2 ≠ 0 mod p). This validation 
			  ensures that the curve does not contain any singular points, making 
			  it suitable for cryptographic purposes

___________________________________________________________________________

                        USAGE & COMMANDS

To run the program with input from the curves.txt file, use the command:
	- python main.py curves.txt
The program will enumerate the list of points, power each point up to infinity, count
the order of each point and write the corresponding results to the file output.txt

Within main.py, I have hardcoded the line number where the selected curve is defined. To select a different line from the input, please adjust the specified line number in the script to correspond to the line of your chosen curve in the input file. This can be done by modifying the variable "line_number" in the main function in main.py.
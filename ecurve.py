"""
Nicolas Nguyen
March 10 2024
EC_class.py
This program implements the Elliptic Curve class using project Jacobian coordinates scheme
"""
class EllipticCurve:
    '''
    DOCSTRING
    '''
    def __init__(self, coeff_a, coeff_b, prime):
        self.coeff_a = coeff_a
        self.coeff_b = coeff_b
        self.prime = prime  # The prime defining the finite field
        if not self.valid_coefficients(coeff_a,coeff_b):
            raise Exception("Coefficients a and b must satisfy: 4a^3 + 27b^2 != 0 mod p")

    def scheme(self):
        '''
        This method displays the mathematical form of the elliptic curve
        '''
        res = "Elliptic Curve: x^3 + {}x + {} mod {}".format(self.coeff_a, self.coeff_b, self.prime)
        return res

    def point_add(self, point_p, point_q):
        '''
        This method performs point addition on two points on the curve
        INPUTS:
            point_p - the first point
            point_q - the second point
        RETURN:
            the result of p+q in Jacobian coordinates (X,Y,Z)
        '''
        x_coordinate_1,y_coordinate_1,z_coordinate_1 = point_p
        x_coordinate_2,y_coordinate_2,z_coordinate_2 = point_q
        z_coordinate_2 = z_coordinate_2+1-1
        x_coordinate_3 = ((y_coordinate_2*pow(z_coordinate_1,3) - y_coordinate_1)**2 - ((x_coordinate_2*pow(z_coordinate_1,2) - x_coordinate_1)**2)*(x_coordinate_1+x_coordinate_2*pow(z_coordinate_1,2))) % self.prime
        y_coordinate_3 = (((y_coordinate_2*pow(z_coordinate_1,3)-y_coordinate_1)*(x_coordinate_1*((x_coordinate_2*pow(z_coordinate_1,2)-x_coordinate_1)**2)-x_coordinate_3)) - (y_coordinate_1*((x_coordinate_2*pow(z_coordinate_1,2)-x_coordinate_1)**3))) % self.prime
        z_coordinate_3 = ((x_coordinate_2*pow(z_coordinate_1,2)-x_coordinate_1)*z_coordinate_1) % self.prime
        return (x_coordinate_3,y_coordinate_3,z_coordinate_3)

    def point_double(self,point_p):
        '''
        This method performs point doubling on a given point on the curve
        INPUTS:
            point_p - a point on the curve
        RETURN:
            the result of 2p in Jacobian coordinates (X,Y,Z)
        '''
        x_coordinate,y_coordinate,z_coordinate = point_p
        x_return = (((3*pow(x_coordinate,2))+(self.coeff_a*pow(z_coordinate,4)))**2 - (8*x_coordinate*pow(y_coordinate,2))) % self.prime
        y_return = ((((3*pow(x_coordinate,2)) + (self.coeff_a*pow(z_coordinate,4)))*(4*x_coordinate*pow(y_coordinate,2) - x_return)) - 8*pow(y_coordinate,4)) % self.prime
        z_return = 2*y_coordinate*z_coordinate % self.prime
        return (x_return,y_return,z_return)

    def is_quadratic_residue(self, val):
        '''
        Checks if an integer is a quadratic residue
        INPUTS:
            val - an integer
        RETURN:
            True if the integer is a quadratic residue. False otherwise
        '''
        # Euler's criterion for checking quadratic residue
        return pow(val, (self.prime - 1) // 2, self.prime) == 1

    def sqrt_mod_p(self, val):
        '''
        Takes a square root mod p of an integer
        INPUTS:
            val - an integer
        REURN:
            the square root of val mod p
        '''
        # Computes the square root of x mod p assuming p % 4 == 3
        #if not self.is_quadratic_residue(val):
        #    return None  # No solution
        return pow(val, (self.prime + 1) // 4, self.prime)

    def find_points(self):
        '''
        Generates all the points on the curve in Jacobian coordinates
        INPUTS:
            None
        RETURN:
            points - a list of all points on the curve (including the point at infinity)
            len(points) - number of points on the curve
        '''
        points = [(float('inf'),float('inf'),0)]
        for num in range(self.prime):
            rhs = (num**3 + self.coeff_a * num + self.coeff_b) % self.prime
            if self.is_quadratic_residue(rhs):
                sqrt_rhs = self.sqrt_mod_p(rhs)
                points.append((num, sqrt_rhs,1))
                y_neg = (-1*sqrt_rhs) % self.prime
                if y_neg != sqrt_rhs:  # Add the negation if it's different
                    points.append((num, y_neg,1))
        return points,len(points)

    def invert_z(self,point_p):
        '''
        This method normalizes a Jacobian point (inverting the z coordinate by making it 1)
        INPUTS:
            point_p - a point on the curve
        RETURN:
            A normalized point (Z=1)
        '''
        x_coordinate, y_coordinate, z_coordinate = point_p
        if z_coordinate == 0:
            return (x_coordinate,y_coordinate,z_coordinate)
        z_inv = pow(z_coordinate, self.prime-2, self.prime)
        z_inv_squared = z_inv**2 % self.prime
        x_norm = x_coordinate * z_inv_squared % self.prime
        y_norm = y_coordinate * z_inv_squared * z_inv % self.prime
        return (x_norm, y_norm, 1)

    def valid_coefficients(self,coeff_a,coeff_b):
        '''
        This method whether a given pair of coefficients a and b constitute
        valid parameters for defining an elliptic curve over a finite field modulo a prime number.
        In other words, does a and b satisfy 4a^3 + 27b^2 != 0 mod p
        INPUTS:
            coeff_a - coefficient a
            coeff_b - coefficient b
        RETURN:
            True if a and b are valid. False otherwise
        '''
        return ((4*pow(coeff_a,3) + 27*pow(coeff_b,2)) % self.prime) != 0

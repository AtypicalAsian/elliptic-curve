"""
Nicolas Nguyen
March 10 2024
main.py
Program to run script on EC Class
"""
import sys
from ecurve import EllipticCurve

def write_point_info(file, count, point, curve):
    '''
    Write point information to the output file
    INPUTS:
        file (file object): The output file to write information to
        count (int): The sequence number of the point in the processing order
        point (tuple): The point in the elliptic curve represented as a tuple
        curve (EllipticCurve object): The elliptic curve instance to which the point belongs
    RETURN:
        None: This function writes to a file and does not return any value
    '''
    file.write(f"PT {count}: {point}, Normalized: {curve.invert_z(point)}\n")

def process_points(file, points, curve, label="SOLUTION"):
    '''
    Process and write information for a list of points
    INPUTS:
        file (file object): The file to which the point information is written.
        points (list): A list of points on the elliptic curve to process.
        curve (EllipticCurve object): The elliptic curve instance that the points belong to.
        label (str, optional): A label used to mark the start of processing a new point.
                               Defaults to "SOLUTION".

    RETURN:
        None: This function writes to a file and does not return any value.

    '''
    for index, base in enumerate(points, start=1):
        count = 1
        curr_point = base
        # Write base point to output file
        file.write(f"{label} {curr_point} \n")
        write_point_info(file, count, curr_point, curve)

        # Double the first point
        curr_point = curve.point_double(curr_point)
        count += 1
        write_point_info(file, count, curr_point, curve)

        # From then on, we power up until we hit the identity (point at infinity)
        while curr_point[2] != 0:
            curr_point = curve.point_add(curr_point, base if label == "SOLUTION" else points[0])
            count += 1
            write_point_info(file, count, curr_point, curve)

        file.write(f"Done Point: {curr_point}\n")
        file.write(f"Point Order: {count}\n\n")



def main():
    '''
    Main Function
    '''
    #Read input from file (curve info)
    line_number = 2 #Line Number from input file

    with open(sys.argv[1], "r") as text_file:
        lines = text_file.readlines()
        text_input = lines[line_number-1].strip()
    params = text_input.split(" ")
    curve = EllipticCurve(int(params[0]),int(params[1]),int(params[2]))
    curve_info = curve.scheme()

    with open('output.txt', 'w') as file:
        file.write(f"{curve_info}\n")
        points_on_curve, no_points = curve.find_points()
        file.write(f"Points on Curve: {no_points}\n\n")

        # Process base point
        process_points(file, [points_on_curve[1]], curve, "BASE POINT")

        # Process all other points
        process_points(file, points_on_curve[2:], curve)

print("Program finished!")

if __name__ == "__main__":
    main()

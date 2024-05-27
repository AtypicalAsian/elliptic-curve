# Elliptic Curve Cryptography

An elliptic curve is a type of smooth, projective algebraic curve defined by a cubic equation of the form $y^2 = x^3 + ax + b$, where $a$ and $b$ are real numbers that satisfy the condition $4a^3 + 27b^2 \neq 0$ to ensure 
the curve is non-singular. The points on an elliptic curve, along with a defined addition operation, form an abelian group, 
which means adding two points on the curve results in another point on the curve. 

This group structure is leveraged in elliptic curve cryptography (ECC), a technique that provides strong security with smaller key sizes compared to 
traditional cryptographic methods like RSA. This results in faster computations and reduced storage and bandwidth requirements, making ECC highly efficient and secure. Elliptic curves are foundational in protocols such as 
Elliptic Curve Diffie-Hellman (ECDH) for secure key exchange and the Elliptic Curve Digital Signature Algorithm (ECDSA) for digital signatures. This project implements fundamental elliptic curve 
operations over finite fields, which includes point addition, point doubling, and point order count.

<br/>

| Operations | Description |
| --- | --- |
| Point Addition | Adds two distinct points on the elliptic curve in Jacobian coordinates |
| Point Doubling | Allows the same point to be added to itself |
| Find Points | Generate all points on the curve modulo a prime |
| Invert Z-coordinate | Normalizes the point in Jacobian coordinates by converting Z to 1, which facilitates easier interpretations |
| Validate Coefficients | Ensures that the curve does not contain any singular points |

<br/>

## Project Organization
---

    ├── README.md          <- The top-level README for developers using this project.
    ├── ecurve.py          <- Elliptic Curve Class Implementation with Jacobian coordinates
    ├── curves.txt         <- Input parameters for elliptic curves in the form (a, b, p)
    ├── main.py            <- Main program to run computation on curves
    ├── output.txt         <- Store program output
    ├── zsampledata.txt    <- Sample output data

## Dependencies

```bash
$ pip3 install -r requirements.txt
```

## Clone this Repository

```bash
$ git clone https://github.com/AtypicalAsian/elliptic-curve.git
```

## Usage
To run the program with input from the curves.txt file, use the command:
```bash
$ python main.py curves.txt
```
The program will enumerate the list of points, power each point up to infinity, count the order of each point and write the corresponding results to output.txt

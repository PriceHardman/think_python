# Exercise 11-8.
# Exponentiation of large integers is the basis of common algorithms for public-key en­
# cryption. Read the Wikipedia page on the RSA algorithm (http://en.wikipedia.org/wiki/
# RSA) and write functions to encode and decode messages.

import math
import numpy
import random
import fractions

# We need the ability to generate primes.
# For the sake of clarity (not efficiency), use the Sieve of Eratosthenes:

def random_prime(n, avoid=1):
    """Return a random prime number less than n, optionally avoiding avoid"""
    numbers = {}
    primes = []
    for i in range(2, n):
        numbers[i] = True
    p = 2
    while p ** 2 <= n:
        if numbers[p] == True:
            j = p ** 2
            while j <= n:
                numbers[j] = False
                j += p
        p += 1
    for i in numbers:
        if numbers[i] == True:
            primes.append(i)
    if avoid in primes:
        primes.remove(avoid)
    return primes[random.randint(0, len(primes) - 1)]

def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def gcd(a, b):
    """Find and return the greatest common divisor of a and b"""
    while b:
        a, b = b, b % a
    return a


def mod_inverse(a, b):
    """Find and return the modular inverse of a mod b."""
    p1, p2, q1, q2, mod = 1, 0, 0, 0, b
    while a != 0:
        q0, r0 = b // a, b % a
        p0 = (p2 - p1 * q2) % mod
        a, b, p2, p1, q2, q1 = r0, a, p1, p0, q1, q0
    return((p2 - p1 * q2) % mod)


def keygen():
    """Generate Public-Private keys for RSA"""
    p = random_prime(10000)   # random prime < 1000
    q = random_prime(10000, p)  # another prime < 1000, not p
    n = p * q  # since p and q are prime, phi(n)=phi(pq)=(p-1)(q-1)
    phi_n = (p - 1) * (q - 1)

    # Choose an integer e s.t. 1<e<phi(n) and gcd(e,phi(n))=1, i.e. e and
    # phi(n)
    e = random.randint(1, phi_n)
    while gcd(e, phi_n) != 1:
        e = random.randint(1, phi_n)

    # Determine the modular inverse of e mod phi(n), d = (e^(-1)) mod phi(n).
    d = mod_inverse(e, phi_n)

    return {"public": {"modulus": n, "public_exponent": e},
            "private": {"modulus": n, "private_exponent": d},
            "phi": phi_n, "p":p, "q":q}


def encrypt(message,public_exponent,modulus):
    """Given a message, modulus, and public key exponent, returns ciphertext"""
    return pow(message,public_exponent,modulus)  # message^public mod modulus

def decrypt(ciphertext,private_exponent,modulus):
    """Given encrypted ciphertext, modulus, and private key exponent,
       returns original message"""
    return pow(ciphertext,private_exponent,modulus) # cipher^private mod modulus

def validate(p,q,phi_n,public,private,modulus):
    print("\n\nValidation:")
    print("p prime:\tis_prime(p)=is_prime(%d)=%s" %(p,is_prime(p)))
    print("q prime:\tis_prime(q)=is_prime(%d)=%s" %(q,is_prime(q)))
    print("phi_n:\t\tphi_n(pq)=(p-1)(q-1)=(%d-1)(%d-1)=%d"%(p,q,(p-1)*(q-1)))
    print("e:\t\t\t1<e<phi_n <=> 1<%d<%d\t%s" % (public,phi_n,1 < public < phi_n))
    print("e:\t\t\tgcd(e,phi_n)=gcd(%d,%d)=%d==1\t%s" % (public,phi_n,gcd(public,phi_n),gcd(public,phi_n)==1))

# Alice generates public and private keys:
keys = keygen()

# Alice sends the public key to Bob:
public = keys["public"]
print("Public key sent by Alice by Bob:")
print("\tPublic Key:",public)

# Alice keeps the private key secret:
private = keys["private"]
print("Private key kept secret by Alice:")
print("\tPrivate Key:",private)

# Bob wants to send a message a Alice:
message = 8675309
print("Bob's message to Alice:")
print("\tMessage:",message)

ciphertext = encrypt(message,public["public_exponent"],public["modulus"])
print("Bob encrypts the message to Alice using the public key:")
print("\tEncrypted Message:",ciphertext)

# Alice decrypts Bob's message using the private key:
decrypted_message = decrypt(ciphertext,private["private_exponent"],private["modulus"])
print("Alice decrypts the message using the private key:")
print("\tDecrypted Message:",decrypted_message)


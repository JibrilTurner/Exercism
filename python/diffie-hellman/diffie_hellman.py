import random 

def private_key(p):
    return random.randrange(2,p)
    pass


def public_key(p, g, private):
    return pow(g, private, p )
    pass


def secret(p, public, private):
    return pow(public,private, p   )
    pass



# Alice's side
p = 3  # Prime number
g = 5   # Generator

# Alice generates her private key
alice_private = private_key(p)


# Alice computes her public key
alice_public = public_key(p, g, alice_private)

# Bob's side
# Bob generates his private key
bob_private = private_key(p)

# Bob computes his public key
bob_public = public_key(p, g, bob_private)

# Exchange of public keys between Alice and Bob

# Shared secret calculation on Alice's side
alice_secret = secret(p, bob_public, alice_private)

# Shared secret calculation on Bob's side
bob_secret = secret(p, alice_public, bob_private)

# The shared secret should be the same on both sides
print("Shared Secret: ", alice_secret)
print("Shared Secret: ", bob_secret)
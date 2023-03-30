---
year: 2023
month: 03
day: 30
---
# PicoCTF 2023 - SRA

> I just recently learnt about the SRA public key cryptosystem... or wait, was it supposed to be RSA? Hmmm, I should probably check...
> 
> 400 points - cryptography

This challenge was one of the ones that I found the most satisfying to solve during PicoCTF 2023. I
haven't done many cryptography challenges before, so please excuse any inefficiencies in my solution 😅.

## Overview

@TableOfContents{"stripEmojis":true,"depth":2}@

## What is RSA?

RSA is a relatively simple asymmetric encryption/decryption algorithm (the encryption key and
decryption key are different).

The [wikipedia page for RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) has a great
explanation of the maths behind RSA.

Applied to the context of this challenge, here's what we know:

```txt
p is a 128-bit prime (would usually be much larger)
q is a 128-bit prime (would also usually be much larger)

n = pq
e = 65537 (would usually be chosen based on some constraints)
φ(n) = (p - 1) * (q - 1)
d ≡ e^(-1) (mod φ(n))

ciphertext ≡ plaintext^e (mod n)
plaintext ≡ ciphertext^d (mod n)
```
Figure 1: *SRA overview*

## The code

The challenge essentially implements the algorithm outlined above to encrypt a randomly generated
sequence of 16 ascii letters and digits. It then prints out `d` (`anger`) and `ciphertext` (`envy`)
and gets us to enter the plaintext. If we get the plaintext correct, we get the flag.

```python
from Crypto.Util.number import getPrime, inverse, bytes_to_long
from string import ascii_letters, digits
from random import choice

pride = "".join(choice(ascii_letters + digits) for _ in range(16))
gluttony = getPrime(128) # p
greed = getPrime(128) #    q
lust = gluttony * greed #  n
sloth = 65537 #            e
envy = inverse(sloth, (gluttony - 1) * (greed - 1)) # d

anger = pow(bytes_to_long(pride.encode()), sloth, lust)

print(f"{anger = }")
print(f"{envy = }")

print("vainglory?")
vainglory = input("> ").strip()

if vainglory == pride:
    print("Conquered!")
    with open("/challenge/flag.txt") as f:
        print(f.read())
else:
    print("Hubris!")
```
Figure 2: *chal.py*

The most important question to answer is what we need to decrypt the ciphertext.

## What do we need?

Recall the last equation from Figure 1; We've got `ciphertext` and `d`, all we need is `n`. Can't be
too hard, right?

```txt
plaintext ≡ ciphertext^d (mod n)
```
Figure 3: *RSA decrypt*

## Maths time!

```txt
# Some useful information
n = pq
e = 65537 (would usually be chosen based on some constraints)
φ(n) = (p - 1) * (q - 1)

# Rearrange some modular arithmetic
d ≡ e^(-1) (mod φ(n))
ed ≡ 1 (mod φ(n))
ed - 1 ≡ 0 (mod φ(n))

# The `mod φ(n)` essentially means get the remainder dividing by φ(n)
# Thus, if the remainder is 0, `ed - 1` is a multiple of φ(n)
ed - 1 = φ(n) * k, where k is an integer

ed - 1 = (p - 1) * (q - 1) * k
```
Figure 4: *the maths*

With the final rearranged equation in mind, there's a pretty naïve solution that we can try. It
could be too slow, but it's always best to try it first and optimise later.

## The approach

The basis of this approach is that `p - 1` and `q - 1` will be divisors of `ed - 1`. Therefore, in
theory, we can just list all divisors of `ed - 1` and then find all of the divisors are 1 less than
a 128-bit prime. We can then take all of those possible values of `p - 1` and `q - 1`, add one to
them, and go through all combinations of possible values for `p` and `q`. For each combination we
can attempt to decrypt the ciphertext, and if the output is a string of ascii letters and digits,
we've probably found the correct value. If we get lucky, there weren't be too many divisors.

```python
from Crypto.Util.number import isPrime, long_to_bytes
from string import ascii_letters, digits
from itertools import combinations
from sympy import divisors
from math import log2

anger = int(input("anger = "))
envy = int(input("envy = "))
sloth = 65537

ds = divisors(envy * sloth - 1)
primes = [x + 1 for x in ds if isPrime(x + 1)]
correct_size_primes = [x for x in primes if log2(x) // 1 == 127]

valid_plaintexts = []
charset = ascii_letters + digits
for p, q in combinations(correct_size_primes, 2):
    try:
        s = long_to_bytes(pow(anger, envy, p * q)).decode("ascii")
        if all([c in charset for c in s]):
            valid_plaintexts.append(s)
    except Exception:
        continue

print(valid_plaintexts)
```
Figure 5: *exploit.py*

## Does it work?

The short answer; most of the time?

```txt
anger = 24398438998096796505136585754485122083423993128182088895588693010516281150000
envy = 79858385363514967732413083778555381826816038680345822674623719303400035174513
["HGWW0Lhmhzatb2Ul"]
```
Figure 6: *it works! (in 1 minute and 16 seconds)*

In practice, this approach is a bit hit and miss because the line `ds = divisors(envy * sloth - 1)`
can take an awfully long amount of time if you get unlucky and `ed - 1` ends up having an incredibly
large amount of possible divisors. It works around 30-50% of the time in my experience which is
certainly good enough for a CTF challenge solution 😅.

## Possible optimisations (for fun, no profit)

During the CTF I just moved on after solving the challenge, as you do, but afterwards I read 
[a clever 'writeup'](https://crypto.stackexchange.com/questions/105734/crack-rsa-with-e-and-d)
(answer on StackExchange) in which the hacker instead found the prime factors of `ed - 1` (much
faster than finding all possible divisors). They then took the log (base 2) of each factor and used
that to figure out which factors multiply together to make 128-bit numbers (if a prime is 128-bit,
subtracting 1 still gives you a 128-bit number because 2^127, the smallest 128-bit number, isn't
prime). The rest of the approach is the same, but in theory it should run much faster. I haven't
personally tried out this approach, but if you do I'd be interested to hear how much of an
improvement it gives.

## Conclusion

I've always wanted to get into cryptography challenges more (as a binary exploitation guy). And in
my opinion, this challenge was a great introduction to RSA challenges, and didn't require a
prohibitive amount of maths (although take that with a grain of salt coming from a guy doing a
bachelor of maths).

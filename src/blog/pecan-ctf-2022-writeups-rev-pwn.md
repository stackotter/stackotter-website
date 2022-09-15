---
year: 2022
month: 09 
day: 15
---
# PeCan CTF 2022 writeups (rev/pwn)

In this post I will be explaining my solutions for each of the 9 rev/pwn challenges from PeCan CTF
2022 (plus an additional misc challenge which I solved in a rev/pwn way). If my solution to a
challenge doesn't make sense to you, feel free to reach out to me on Discord (`@stackotter#3100`) or
Twitter ([`@stackotter`](https://twitter.com/stackotter)) and ask me for a better explanation.

Challenge file download links will be provided once the respective authors give their permission.

## Table of contents

@TableOfContents{"stripEmojis":false,"depth":1}@

## encoded (rev, 50 points, 30 solves)

My first instinct with reverse engineering challenges is always to take a quick look through all of
the strings present in the binary, especially when the challenge is a beginner challenge and/or
hints at some kind of encoding.

After running `strings ./encoded` I found a base64 encoded string (easy to identify if you've seen
base64 before) and sure enough decoding it gave the flag: `pecan{B@sically_I_Sh0uld_H1de_B3tt3r}`.
You've gotta appreciate the sneaky little pun in there, intended or not. Overall a pretty simple
beginner rev challenge.

## Thr34d1ng the n33dl3 (rev, 50 points, 23 solves)

You know it's getting serious once the challenge authors whip out leetspeak! (well not really, I
just wanted to say that).

Once again this challenge can be solved using `strings`. Here's an excerpt from the output of
`strings ./thym3` (the challenge executable is called `thym3`):

```txt
pecan{0bH
fu$c4t3_H
y0ur_$trH
1ng5}
```
Figure 1: *an excerpt from the output of `strings ./thym3`*

Removing the trailing `H`s and concatenating the lines gives us the flag:
`pecan{0bfu$c4t3_y0ur_$tr1ng5}`.

The reason that the flag is weirdly fragmented like this is more clear if we take a look at the
program in a decompiler (I used Ghidra).

```c
local_38 = 0x62307b6e61636570;
local_30 = 0x5f33743463247566;
local_28 = 0x7274245f72753079;
local_20 = 0x20207d35676e31;
```
Figure 2: *an excerpt from the decompiled `main` function*

These 4 extremely suspicious looking unused local variables declared at the start of the `main`
function hold the flag and the `strings` which we saw are from these integer values hardcoded into
`mov` instructions. The trailing `H`s that `strings` found are actually just the first byte of the
opcode of the instruction after each string.

Without needing to go into all that depth, it's easy to guess that the `H`s are garbage because they
don't fit into the flag's words, they suspiciously end each line (except the last which is shorter)
and the blocks are 9 characters as opposed to 8 which would be much more likely.

## among_us (rev, 50 points, 8 solves)

Again the first step in my solution was using `strings`. Scrolling through the output of `strings`
a massive block of base64 data immediately jumped out at me (not literally luckily) so I piped it
through the `base64` command-line tool (but CyberChef also works if you're more comfortable with a
GUI). The decoded output clearly started with the elf file header (looks like `.ELF` in CyberChef
because the first byte is `0x7f` which is non-printable), so I saved it to a file and ran the file
as an executable which printed out the flag: `pecan{Who_Got_Ejected?_N0t_mE}`.

## Printing machine (rev, 100 points, 36 solves)

This challenge came in the form of a single Python file. To solve the challenge you just read
through the Python to see where the flag might be generated. Because of the cryptic variable names
it may help to give the variables to more distinct names (e.g. a, b, c) using the rename function of
the your code editor if your editor has python support. The `FlagifyYourLifeWithOurNewAppFlagify`
function is a decoy, the real function we are interested in is the aptly named
`IfFightingIsSureToResultInVictoryThenYouMustFightTsunTzuSaidThat` function. Only the last two lines
of this function do anything of effect, so how suitable for them to print the flag for us! After
identifying how the flag is generated, I just ran the Python code in Figure 3 to get the flag:
`pecan{7cd68c67379055ce66d370da91201767}`.

```python
password ="fjdSDwEo91%i#fj"
content =md5 (password .encode ('utf-8')).hexdigest ()
print(f"{name}{{{content}}}" )
```
Figure 3: *the code that generates the flag*

## 0v3r_fl0w (rev, 150 points, 16 solves)

This challenge is just an extremely simple buffer overflow. Spam a bunch of characters and then hit
enter and it'll print the flag before it crashes (how philanthropic). The flag was
`pecan{kk_so_u_just_overflowed_the_buffer_:)_}`.

## broken_elf (rev, 150 points, 3 solves)

As you can see from the number of solves, this was quite an interesting challenge. We are given two
ELF executables, one corrupted and one working. The working ELF file is purely to serve as a
reference when fixing up the corrupted ELF file. My first steps were opening up the two ELFs in
split screen hex editors (I used Octets, a simple hex editor, but I probably should've used 010
editor for filetype-aware hex editing which decodes known fields), and then Googling the ELF file
format and opening [the Wikipedia result](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format).

The first difference between the two ELFs was at byte 7 where the broken ELF had a 4 and the working
one had a 0. Referring to the Wikipedia section on the ELF file header, I found that byte 7
signifies the OS application binary interface. Both ELFs were likely compiled for the same system so
I changed the broken ELF to have a 0 at byte 7 as well.

The next difference was at byte 0x18 where the broken ELF had zeroes and the working one had what
looked like an address. The Wikipedia page confirmed this suspicion, specifying that bytes 0x18 to
0x1b (inclusive) are the address of the program's entrypoint represented as a 32 bit integer.

To find the address of the broken ELFs entrypoint you can run `objdump -d ./broken_elf` and scroll
through the output to find the `_start` function and its corresponding address (`0x401070`). During
the competition I actually did this a much more convoluted way which involved looking at the working
ELF's entrypoint in GDB and then searching for the same sequence of instructions in the broken ELF
and then trying both possibilities that I found, but the `objdump` method (which I realised after
the event) is so much better so please kindly use that instead. The reason that the `objdump` method
works even though we haven't fixed the entry point yet is that `objdump` doesn't care what the entry
point is because it uses the debug symbols present in the binary to locate the functions and
probably doesn't even read the entry point.

Now we just replace bytes 0x16 to 0x1b of the broken ELF with `70 10 40 00` (the bytes are reversed
because the address is stored as a [little endian](https://en.wikipedia.org/wiki/Endianness)) And
voila, we have a working executable. Just run the fixed executable to get the flag:
`pecan{Th1ng$_ar3_n0t_br0k3n_4eva}` (for some reason in the output of the program the closing curly
bracket is missing).

Overall this was a very enjoyable challenge and really tested knowledge of file formats and
executables.

## C4lcul8t0r (rev, 200 points, 5 solves)

To solve this challenge my first instinct was to open the executable in Ghidra to see what it was up
to. In the `calc` function (effectively the main function of the program) I found the code that was
printing the flag. All it did was subtract `0x50` from each byte of the `flag` global and then print
out the result. I think the intended method was to reverse engineer the password and then type it
in, but given that the flag and password were encoded in exactly the same way, this method was
slightly more direct.

During the competition I just typed the bytes into a Python script manually by reading them out of
Ghidra, and then whipped up a one liner to decode the array of bytes. But afterwards I realised it
would've saved a bit of time to just use pwntools' great elf file reader (Figure 4).

```python
from pwn import *

elf = ELF("./C4lcul8t0r")
encoded = elf.string(elf.symbols["flag"])
print("".join([chr(byte - 0x50) for byte in encoded]))
```
Figure 4: *a Python script to solve the challenge using pwntools*

The flag that this produces is: `pecan{L33t-sp34k+m4th$=c0oO0ooO0o0L}`.

I completed this challenge much faster than broken ELF and I think that the points were quite a bit
too high, but I'm not complaining, free points! (and the number of solves says otherwise I guess)

## Birthday (rev, 300 points, 5 solves)

This challenge was actually quite interesting for me because I hadn't done any Windows pwn
challenges before. My first step was attempting to open it in Ghidra which didn't really work, all
of the C sharp bytecode was left undecoded. So next I Googled how to decompile C sharp executables
and I found a tool called
[Reflector](https://www.red-gate.com/products/dotnet-development/reflector/) which I promptly
installed on my friend's laptop. After a bit of browsing around and scratching my head at dot net's
strange programming model, I found the win function (called `ahha`) which essentially takes in some
input and XOR's each byte with `'A'` to get the flag. By searching for callers of the function using
Reflector's handy features, I found what the input to the function was and my teammate finished off
the challenge by writing a Python script to decode the flag (I got distracted helping a different
teammate debug their solution to another challenge).

I don't have a Windows computer at hand and I can't be bothered booting up one of mine so I'll leave
finding the flag as an exercise to the reader.

## Password_Prompt (rev, 360 points, 3 solves)

I'm surprised this challenge didn't get more solves as it was a relatively vanilla buffer overflow.
The aim of the challenge (as described helpfully by the program itself) was to overwrite the
contents of a char array to the value `Real_password`. By decompiling the program in Ghidra we can
see that the input buffer is 32 bytes long and the buffer to overwrite is located directly after the
input buffer. This means that we can enter 32 characters of garbage and then everything that we
enter after that will get written straight into the target buffer. See figure 5 for the exploit
script I used.

```python
from pwn import *

payload = b"a" * 32 + b"Real_password"

p = process("./password_prompt.out")
p.sendline(payload)
print(p.recvall())
```
Figure 5: *exploit script for `Password_Prompt`*

The flag was `pecan{Remember_to_protect_the_memory_allocation_in_your_work!}`.

## The Sassbot (misc, 400 points, 6 solves)

I'm incuding this challenge in my pwn/rev writeups because it was basically a pwn challenge (the way
I solved it at least). According to the challenge author, the intended method didn't require any
external tools, however reverse engineering and pwn are my natural habitat so I instantly opened the
binary in Ghidra to check it out. I found that both the password (in `main`) and the flag (in `flagf`)
were encoded within the executable in the same way as calculator (except with an offset of `0x55`
instead of `0x50` this time). Woohoo, we can trivially reuse the script from calculator to solve the
challenge :) (sorry challenge author).

```python
from pwn import *

elf = ELF("./sassbotv1.0.5.1")
encoded = elf.string(elf.symbols["flag"])
print("".join([chr(byte - 0x55) for byte in encoded]))
```
Figure 6: *exploit script for `The Sassbot`*

The flag was `pecan{G0od-guy$-d0nt-f1ni$h-l4st}`.

## Conclusion

Overall the rev/pwn challenges were quite easy compared to other CTFs and their points were weighted
very high, but I guess that's because the CTF was aimed at school age students and only a few of the
top teams are expected to have any expertise in the areas of pwn and rev. The challenges that I
enjoyed the most were broken elf (because it was a bit unconventional) and birthday (because it was
a completely new area of rev/pwn for me).

---
year: 2024
month: 04
day: 30
---
# Cryptography talk

Resources for a talk on the foundations of modern cryptography.

## Practice time 1

1. Decode `ZmxhZ3tub3RfYmFzZV82M30=`
2. Decrypt `uapv{rpthpg_hjrzh}`
3. Decrypt `Ao(mgHZs$UEb&NgDIYA20lCV]I/`
4. Decrypt `glnq{ttni_witsmaad}`
5. Decrypt `312d3522293e1e68760d2f2e261a3b23320b363d0832312627252429`

## Padding oracles

- [Animated explanation](https://dylanpindur.com/blog/padding-oracles-an-animated-primer/)
- [My padding oracle write-up from BSidesCTF 2023](https://stackotter.dev/blog/bsides-brisbane-2023-writeups-part-1#neo-crypto---300-points)
- [My PicoCTF SRA write-up](https://stackotter.dev/blog/picoctf-2023-sra-writeup)

## Mini CTF

### Existing challenges

- [hello_world (easy)](https://ctf.stackotter.dev/challenges#hello_world-1) (intro to encodings)
- [a_bootleg_riddler (medium)](https://ctf.stackotter.dev/challenges#a_bootleg_riddler-6) (can be mostly solved with pure CyberChef)
- [horses (medium)](https://ctf.stackotter.dev/challenges#horses-12) (covers block ciphers and frequency analysis)

### New challenges

- [frequently (easy)](https://ctf.stackotter.dev/challenges#frequently-33) (it's in the name)
- [onion (medium)](https://ctf.stackotter.dev/challenges#onion-32) (solvable with pure CyberChef)
- [ars (medium)](https://ctf.stackotter.dev/challenges#ars-30) (an RSA challenge)
- [delphi (hard)](https://ctf.stackotter.dev/challenges#delphi-31) (a CBC PKCS7 padding oracle)

Prizes for the first 3 solves of each new challenge.

Bonus prize for the fastest `ars` solution which doesn't make assumptions about the input numbers.

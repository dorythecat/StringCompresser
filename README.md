# StringCompresser
> A (very silly) experiment on how to compress and encode strings :3

I just really wanted to test how much I could compress a string, in
such a way that it can be:
- Reverted
- URL-safe
- As small as possible
- Maintains case and special characters
Let's see how far I can get with this! >:D

# Story
I want to leave a little bit of a diary of development of this, mainly
because I want to be able to look at this in future and say "Oh so this
is how I arrived at that, interesting!". With that said, here's the
different iterations I went through:

## 1st Iteration - Modulo 2048
Coming up with a basic idea was really hard for me, because there's not
really a good, apparent way of encoding a string into something that's
smaller, yet can still be represented as a string.

After some experimenting, I started by turning the string into a
hexadecimal number. There's functions in python for this, but a TL;DR of
what they do is, they take the string, character by character, convert it
to hexadecimal (00 to FF), and then join every character tail-to-head to
create a long hexadecimal number. This doubles the string's size, so it
originally didn't seem like a good idea. But then I remembered that I can
turn that hexadecimal number into a "normal", decimal integer. This number
is sadly even bigger, but we can work on it by using a trick: Division
remainders.

The idea is to divide this number by 2048, take the remainder, and store
that remainder, as a character. If we keep on doing this until we reach 0,
we can get a list of remainders, in the form of a string of characters,
each representing a number from 0 to 2047. This process is easy to inverse,
so we can easily get our number back. This all is very compact to write in
Python, and produces a string that is about 25% smaller than the original
(the reduction factor grows with the string).

If you're wondering why I chose 2048, it's not at random. First of all, it's
a power of 2, so it's easy to work with it in binary, and Python is great at
doing those optimizations. It's also a big value (the bigger the value, the
bigger the reduction, and the smaller the minimum string it affects), without
being too big (Whilst 65536 would theoretically be better, it would include
certain characters that are not URL-safe, and most of the time, not even
supported!). So it's basically the perfect compromise in this weird tug-of-war.

## 2nd Iteration - 65536 is the new 2048
After a bit of thinking and tinkering, I decided to retry using a high value as is
65536, or 2^16, which is the maximum value that can be represented by 2 bytes, and
thus, the maximum on the UTF-8 encoding scheme for a single character. I had thought
this would not really work. Turns out, I was wrong. The only actual problem was that,
previously, I had used 65535, which is 2^16 - 1, and thus, caused a few issues. But
65536 works perfectly fine, and in fact, reduces the size of strings to half their size!
(Technically it reduces by half only strings that have an even length, whilst it does 
slightly less for odd-length strings, though it's often negligible).
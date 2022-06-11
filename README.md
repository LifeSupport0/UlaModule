# UlaModule

## What is UlaModule?

UlaModule is a small, fast, dependency-less package for producing an Ulam spiral.

## What is an Ulam spiral?

An [Ulam Spiral](https://en.wikipedia.org/wiki/Ulam_spiral) is a type of spiral that consists of a grid of points labeled with positive integers.

![A rendition of the Ulam spiral, with the center colored in black and the primes colored in red. (Oops! this is alt text)](https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fprimorial-sieve.com%2FPic_sav%2FUlam%2520spiral%25201.JPG&f=1&nofb=1)  
(credit: primordial-sieve.com)

Note that the Ulam Spiral starts at 1. This isn't particularly convenient for indexing purposes, so this implementation will start with 0 as its start.

e.g.,  
0 -> (0,0),  
1 -> (1,0),  
2 -> (0,1),  
3 -> (1,1),  
and so on

The inverse function ((1,0) -> 1, etc) is also included in UlaModule.

Note that in order to translate this library's Ulam spiral into a traditional one, you need only increment by 1 after converting a 2d point into an integer. Eventually, I'm going to add a function that will do this automatically.

## How fast is UlaModule?

Both functions (int-to-point and point-to-int) is O(1).

## Why would I use UlaModule?

UlaModule isn't meant to be something big, significant, or immensely impactful for your project.  
It's intended for the programmer who wants to convert one number into two and vice versa (with no duplicates or missing numbers), but doesn't want to waste time thinking about how to do that.

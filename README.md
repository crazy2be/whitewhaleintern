
A small python program to scramble strings (but leave the first/last letters
intact). In theory, the resulting strings are still readable. Does not scramble
symbols or numbers, only alphabetic characters.

**To Run:**
`./gibgen.py "some string" "and some more"`
-or-
`cat a_file | ./gibgen.py`

Written in python3.

Supports Unicode ♙┶⍥⚕.

Works by first making a list of scrambleable letters, and a bunch of
(list, position) pairs for immovable ones (first, last, symbols, numbers).

Then, scrambles the eggs, and puts them in all the gaps.

The most difficult aspect was getting unicode support flawless. <may not be
flawless, unicode is complicated, I didn't test it as much as Unicode may
warrant>.

Bitwise Operations
------------------

A B		A & B
------------------
0 0 	0
1 0		0
0 1		0
1 1		1	

A B		A | B
------------------
0 0 	0
1 0		1
0 1		1
1 1		1	

    vv 
  1110101
& 0011000
------------------
  0011000


Every time you shift a number right you are dividing it by the base

Shifting

0010000
0001000
0000100
0000010

1. mask the number to get rid of values you dont want
2. shift the number until you isolate the bits you want

  vv
  10100010	MUL
& 11000000
-----------------
  10000000 >> 6
  ^^
  00000010
  		^^

>> right shift

<< left shift

ir = 0b10100010 # MUL
length = ((ir & 0b11000000) >> 6) + 1

pc += length


# NOT

Not operator is `~` (tilde)

```
a = 1

~a == 0

a = 0

~a == 1


```

# AND 

AND operator is `&` (ampersand)

```
a = 0
b = 0

a & b == 0

a = 1
b = 0

a & b == 0

a = 0
b = 1

a & b == 0

a = 1
b = 1

a & b == 1


```

# OR 

OR operator is `|` (ampersand)

```
a = 0
b = 0

a | b == 0

a = 1
b = 0

a | b == 1

a = 0
b = 1

a | b == 1

a = 1
b = 1

a | b == 1


```

# NAND

NOT AND

```
a = 0
b = 0

~(a & b) == 1

a = 0
b = 1

~(a & b) == 1

a = 1
b = 0

~(a & b) == 1

a = 1
b = 1

~(a & b) == 0


```


# NOR - neither A nor B

```
a = 0
b = 0

a NOR b == 1

a = 0
b = 1

a NOR b == 0

a = 1
b = 0

a NOR b == 0

a = 1
b = 1

a NOR b == 0


```

# XOR - exclusive OR
# only true if either one or other is true, not both

XOR operator is `^` (carrot)


```
a = 0
b = 0

a ^ b == 0

a = 1
b = 0

a ^ b == 1

a = 0
b = 1

a ^ b == 1

a = 1
b = 1

a ^ b == 0


```

## Multi-bit numbers

  11101011
& 10011101
----------
  10001001

  11011010
^ 11100011
----------
  00111001
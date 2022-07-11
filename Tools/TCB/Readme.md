# This file is used to convert multiplication to shift and addition.

## Flow 
* Num(DEC) -> Num(Bin)
* Find the range of the consecutive numbers
* Return Results

## Example
* N x 53 = N << 6 - N << 4 + N << 2 + N << 0
* $53 = 11 0101 = +0- 0+0+ = 2^6 - 2^4 + 2^2 + 2^0 $
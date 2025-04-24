"""A magic square is an N×N grid of numbers in which the entries in each row, column and main 
diagonal sum to the same number (equal to N(N^2+1)/2). Create a magic square for N=4, 5, 6, 7, 8"""

import numpy as np

def odd_magic_square(n):
    magic_square = np.zeros((n, n), dtype=int)
    i, j = 0, n // 2  # Start at the middle of the first row

    for num in range(1, n * n + 1):
        magic_square[i, j] = num
        new_i, new_j = (i - 1) % n, (j + 1) % n  # Move up-right

        if magic_square[new_i, new_j]:  # If occupied, move down
            i += 1
        else:
            i, j = new_i, new_j

    return magic_square

def double_even_magic_square(n):
    magic = np.arange(1, n * n + 1).reshape(n, n)
    mask=np.ones((n,n),dtype=bool)
    for i in range(n):
        for j in range (n):
            if((i%4==j%4) or (i%4+j%4==3)):
                mask[i,j]=False
    magic[mask]=(n*n+1)-magic[mask]
    return magic
   
def single_magic_square(n):
    half_n = n // 2
    sub_square = odd_magic_square(half_n)
    magic_square = np.zeros((n, n), dtype=int)

    # Assign each quadrant an offset
    add = [0, 2 * half_n * half_n, 3 * half_n * half_n, half_n * half_n]
    
    for i in range(n):
        for j in range(n):
            quadrant = (i // half_n) * 2 + (j // half_n)
            magic_square[i, j] = sub_square[i % half_n, j % half_n] + add[quadrant]

    # Swap columns in the leftmost upper and lower part
    k = (n - 2) // 4
    for i in range(half_n):
        for j in range(k):
            magic_square[i, j], magic_square[i + half_n, j] = (
                magic_square[i + half_n, j],
                magic_square[i, j],
            )

    # Swap columns in the rightmost part
    for i in range(half_n):
        for j in range(k + 1, half_n):
            magic_square[i, j + half_n], magic_square[i + half_n, j + half_n] = (
                magic_square[i + half_n, j + half_n],
                magic_square[i, j + half_n],
            )

    return magic_square

def generate_magic_square(n):
    """Generate a magic square for any given N."""
    if n % 2 == 1:
        return odd_magic_square(n)
    elif n % 4 == 0:
        return double_even_magic_square(n)
    else:
        return single_magic_square(n)


for N in [4, 5, 6, 7, 8, 10]:
    print(f"\nMagic Square for N = {N}:\n")
    print(generate_magic_square(N))

def pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            if j==1 or j==i or j==n:
                print(j, end=" ")
            else:
                print(" ",end=" ")
        print()

a=int(input('Enter the number: '))
pattern(a)

def print_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if j == 1 or j == i or i == n:
                print("*", end=" ")  # Print the first, last, and bottom row numbers
            else:
                print(" ", end=" ")  # Print blanks for other positions
        print()

# Example usage:
n = 5  # You can change the value of n to adjust the size of the triangle
print_triangle(n)

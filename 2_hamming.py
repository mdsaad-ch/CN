
h = [0] * 8

print("Enter 4 data bits: ", end="")
h[3], h[5], h[6], h[7] = map(int, input().split())

# Calculate parity bits
h[1] = h[3] ^ h[5] ^ h[7]
h[2] = h[3] ^ h[6] ^ h[7]
h[4] = h[5] ^ h[6] ^ h[7]

print("Transmitted Hamming code: ", end="")
for i in range(1, 8):
    print(h[i], end="")

# Introduce error
error = int(input("\nEnter bit position to introduce error (0 for none): "))

if 1 <= error <= 7:
    h[error] ^= 1

print("Received code: ", end="")
for i in range(1, 8):
    print(h[i], end="")

# Check parity bits
p1 = h[1] ^ h[3] ^ h[5] ^ h[7]
p2 = h[2] ^ h[3] ^ h[6] ^ h[7]
p4 = h[4] ^ h[5] ^ h[6] ^ h[7]

# Find error position
error = p1 + 2 * p2 + 4 * p4

if error:
    print("\nError detected at bit position:", error)
    h[error] ^= 1
    print("Corrected code: ", end="")
else:
    print("\nNo error detected.")
    print("Received code is: ", end="")

for i in range(1, 8):
    print(h[i], end="")

print()

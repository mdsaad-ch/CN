import math

prefix, subnets = map(int, input("Enter base prefix (e.g., 24) and number of subnets: ").split())

# Calculate borrowed bits and new prefix length
new_prefix = prefix + math.ceil(math.log2(subnets))
total_hosts = 1 << (32 - new_prefix)

# Generate the 32-bit subnet mask
mask = (0xFFFFFFFF << (32 - new_prefix)) & 0xFFFFFFFF

# Display subnet mask
print("Subnet Mask:",
      (mask >> 24) & 255, ".",
      (mask >> 16) & 255, ".",
      (mask >> 8) & 255, ".",
      mask & 255, sep="")

print("Usable hosts:", total_hosts - 2)
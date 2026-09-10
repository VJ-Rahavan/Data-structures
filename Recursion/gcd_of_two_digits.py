#gcd(12,18)

# gcd(12,18)
#     ↓
# gcd(18,12)
#     ↓
# gcd(12,6)
#     ↓
# gcd(6,0)
#     ↓
#     6


def gcd(a,b):
  if b == 0:
    return a

  return gcd(b, a % b)
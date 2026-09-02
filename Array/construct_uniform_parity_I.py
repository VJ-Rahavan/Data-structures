# 3875. Construct Uniform Parity Array I

#                 nums1
#                   │
#           ┌───────┴────────┐
#           │                │
#      Has an odd?       No odd?
#           │                │
#          YES               │
#           │                │
#  Pick any odd number    All are even
#           │                │
#           ↓                ↓
#  even - odd = odd       Keep as-is
#  odd → keep             ↓
#           │           all even
#           ↓
#       all odd
#           │
#           ↓
#        ALWAYS TRUE

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return True
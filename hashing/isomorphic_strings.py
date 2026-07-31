# Two strings are isomorphic if characters in s can be replaced to get t,
# with a one-to-one mapping (no two chars map to the same char, and each char maps to only one).
# I maintain two hash maps: s -> t and t -> s. For every pair of characters at the same index,
# I check both mappings are consistent. If either mapping conflicts, they're not isomorphic.
# Time: O(n), Space: O(k) where k is the alphabet size.

def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    map_st, map_ts = {}, {}

    for a, b in zip(s, t):
        if a in map_st and map_st[a] != b:
            return False
        if b in map_ts and map_ts[b] != a:
            return False
        map_st[a] = b
        map_ts[b] = a

    return True


print(is_isomorphic("egg", "add"))
print(is_isomorphic("foo", "bar"))
print(is_isomorphic("paper", "title"))

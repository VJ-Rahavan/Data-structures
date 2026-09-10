def countChar(s, ch, idx=0):
    if idx == len(s):
        return 0

    if s[idx] == ch:
        return 1 + countChar(s, ch, idx + 1)

    return countChar(s, ch, idx + 1)
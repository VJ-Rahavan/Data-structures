

def reverse(s, i=0, result=""):
    if i == len(s):
        return result

    return reverse(s, i + 1, s[i] + result)

print(reverse("Hello"))
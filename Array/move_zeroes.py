# I use two pointers. The "write" pointer tracks where the next non-zero element should go.
# As I scan with the "read" pointer, every non-zero value is swapped into the write position,
# and the write pointer advances. All zeros naturally end up at the end.
# Time: O(n), Space: O(1) — done in place.

def move_zeroes(arr):
    write = 0

    for read in range(len(arr)):
        if arr[read] != 0:
            arr[write], arr[read] = arr[read], arr[write]
            write += 1

    return arr


print(move_zeroes([0, 1, 0, 3, 12]))
print(move_zeroes([0, 0, 1]))

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:

            while (
                stack
                and asteroid < 0
                and stack[-1] > 0
                and stack[-1] < abs(asteroid)
            ):
                stack.pop()

            if not stack or asteroid > 0 or stack[-1] < 0:
                stack.append(asteroid)

            elif stack[-1] == abs(asteroid):
                stack.pop()

        return stack
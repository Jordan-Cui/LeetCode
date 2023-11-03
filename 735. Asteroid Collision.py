class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        for i in range(1, len(asteroids)):
            if not stack or stack[-1] < 0:
                stack.append(asteroids[i])
                continue
            if asteroids[i] > 0:
                stack.append(asteroids[i])
                continue
            while stack and stack[-1] > 0 and asteroids[i] * -1 > stack[-1]:
                stack.pop()
            if not stack or stack[-1] < 0:
                stack.append(asteroids[i])
            elif asteroids[i] * -1 < stack[-1]:
                continue
            else:
                stack.pop()
        return stack

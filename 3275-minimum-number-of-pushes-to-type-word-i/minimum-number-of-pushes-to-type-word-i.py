class Solution:
    def minimumPushes(self, word: str) -> int:
        quo = len(word) // 8
        rem = len(word) % 8

        ans = 0
        level = 1
        for i in range(quo) :
            ans += level * 8
            level += 1

        ans += rem*level

        return (ans)


        
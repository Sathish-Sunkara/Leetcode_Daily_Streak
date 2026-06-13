class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:

        # preprocessing the weights so that we find the character for sum weight in O(1) time
        # weightTOchar = defaultdict(list)
        # for i,w in enumerate(weights[::-1]) :
        #     weightTOchar[w].append(chr(25-i+97))

        ans = ""
        for word in words :
            sum = 0
            for ch in word :
                sum += weights[ord(ch) - 97]

            sum %= 26
            ans += chr(25-sum+97)
        return ans


        
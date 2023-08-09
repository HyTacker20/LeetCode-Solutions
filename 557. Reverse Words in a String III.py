class Solution:
    def reverseWords(self, s: str) -> str:
        res = ''
        for word in s.split(' '):
            word = list(word)
            for n in range(len(word) // 2):
                word[n], word[-(n + 1)] = word[-(n + 1)], word[n]
            word = ''.join(word)
            res += word + ' '

        return res.rstrip()

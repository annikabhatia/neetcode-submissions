class Solution:

    def encode(self, strs: List[str]) -> str:
        result = list()
        for i in range(len(strs)):
            result.append(str(len(strs[i])) + "#" + strs[i])
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            result.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return result
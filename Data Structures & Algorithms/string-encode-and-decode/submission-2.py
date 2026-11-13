class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded += i

        result = str(len(encoded)) + "#" + encoded + "#"

        for i in strs:
            result += str(len(i)) + ","

        return result

    def decode(self, s: str) -> List[str]:
        i = 0
        while s[i] != '#':
            i += 1
        lengths = s[:i]

        j = len(s) - 1
        while s[j] != '#':
            j -= 1
        
        payload = s[i + 1 : j]
        lengths = s[j + 1:].split(',')
        offset = 0
        ls = []
        for i in lengths:
            if i != "":
                ls.append(payload[offset : offset + int(i)])
                offset += int(i)

        return ls

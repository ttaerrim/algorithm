s = input()
alphabet = [0 for _ in range(26)]

for i in range(len(s)):
    idx = ord(s[i]) - 97
    alphabet[idx] += 1

print(' '.join(str(x) for x in alphabet))

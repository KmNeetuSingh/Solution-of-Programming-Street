def anagrams(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    if len(str1) != len(str2):
        return False
    count = [0] * 26  
    for char in str1:
        count[ord(char) - ord('a')] += 1
    for char in str2:
        count[ord(char) - ord('a')] -= 1
    return all(c == 0 for c in count)

print(anagrams("listening", "silent"))

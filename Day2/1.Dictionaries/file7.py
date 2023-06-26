# Word counter

def word_counter(string):
    count = {}
    for char in string:
        count[char] = string.count(char)
    return count


ans = word_counter('Ayaan')
print(ans)

def two_sum(nums, target):
    
    seen = {}
    for i, value in enumerate(nums):
        remaining = target - value
        if remaining in seen:
            return [seen[remaining], i]
        
        else:
            seen[value] = i

def roman_to_integer(s):
    
    dict = {'I':1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    total = 0

    for x in range(len(s)-1):
        if dict[s[x]] < dict[s[x+1]]:
            total -= dict[s[x]]
        else:
            total += dict[s[x]]

    total += dict[s[-1]]

    return total

def longest_prefix(strs):
    strs = sorted(strs)
    n = len(strs)
    s1, s2 = strs[0], strs[n-1]
    result = ''

    for i in range(len(s1)):
        if s1[i] == s2[i]:
            result += s1[i]
        else:
            return result

    return result

def valid_parenthesis(s):
    dict = {')':'(', '}':'{', ']':'['}
    stack = []

    for x in s:
        if x in dict.values():
            stack.append(x)
        elif stack and stack[-1] == dict[x]:
            stack.pop()
        else:
            return False

    return stack == []



if __name__ == "__main__":
    two_sum([2,7,11,15],9)
    roman_to_integer('VIII')
    longest_prefix(["flower","flow","flight"])
    print(valid_parenthesis('()'))
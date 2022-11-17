from collections import defaultdict, Counter
import string

incomes = [('Books', 1250.00),
           ('Books', 1300.00),
           ('Books', 1420.00),
           ('Tutorials', 560.00),
           ('Tutorials', 630.00),
           ('Tutorials', 750.00),
           ('Courses', 2500.00),
           ('Courses', 2430.00),
           ('Courses', 2750.00),]

def result_get(st):

    ans = Counter(st)
    return(dict(ans))
    # result = defaultdict(int)
    # position = defaultdict(list)

    # for x in st:
    #     result[x] += 1
    #     position[x] = st.index(x)
    
    # print(result)
    # print(position)


def new(incomes):

    total = defaultdict(float)

    for x , y in incomes:
        total[x] += y
    
    return (dict(total))

def prime(num):
    num = int(num)
    for i in range(2, num):
        if num % i == 0:
            return False

    return True

def palindrome(strs):
    for x in string.punctuation:
        strs = strs.replace(x, "").replace(" ","").lower()
    if strs[::-1] == strs:
        return (strs[::-1])
    


if __name__ == "__main__":
    result_get("iamritik")
    new(incomes)
    prime(11)
    palindrome("Hi! This is me.")
    
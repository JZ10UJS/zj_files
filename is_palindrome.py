'''
def is_palindrome(n):   # 我的写法
    n_str = str(n) 
    long = len(n_str)
    for i in range(long):
        if n_str[i] != n_str[long-1-i]:
            return False
    return True
'''

def is_palindrome(n):   # 别人的写法
    return str(n) == str(n)[::-1]

output = filter(is_palindrome, range(1,1000))
print(list(output))

#!/usr/bin/python
# coding: utf-8

"""

"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def twoSum(self, nums, target):
        """
        1. Two Sum
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, v in enumerate(nums):
            # i+1 是因为题目要求， not based on 0
            if target-v in d:
                return [d[target-v], i+1]
            else:
                d[v] = i+1
            
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode  2 -> 4 -> 9
        :type l2: ListNode  7 -> 8 -> 2 -> 1
        :rtype: ListNode    9 -> 2 -> 2 -> 2
        """
        tmp, l1.val = divmod(l1.val + l2.val, 10)
        r = l1

        while (l1.next and l2.next):
            tmp, l1.next.val = divmod(l1.next.val + l2.next.val + tmp, 10)
            l1 = l1.next
            l2 = l2.next
            
        # while 循环结束，必有一个节点.next 为None
        if l2.next:
            l1.next = l2.next
        while l1.next and tmp:
            tmp, l1.next.val = divmod(l1.next.val + tmp, 10)
            l1 = l1.next
        if tmp:
            l1.next = ListNode(1)
        return r

    def lengthOfLongestSubstring(self, s):
        """
        3. Longest Substring Without Repeating Characters My Submissions Question
        :type s: str
        :rtype: int
        """
        
        mydict = {}
        maxlen = 0
        start = 0
        
        for i, letter in enumerate(s):
            if letter not in mydict or mydict[letter] < start:
                # <start, 是忽略掉 重复字母之前的
                mydict[letter] = i
            else:
                length = i - start
                if maxlen < length:
                    maxlen = length
                start = mydict[letter] + 1 # start 改为 重复字母后一位 ‘abcbaf', 此时从c开始计算长度
                mydict[letter] = i
                
        return max(maxlen, len(s)-start) # len(s)-start 就是后面的字母没有重复的，导致上面else语句未执行

    def findMedianSortedArrays(self, nums1, nums2):
        """
        4. Median of Two Sorted Arrays
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = []
        i = 0
        j = 0
        while i<len(nums1) and j<len(nums2):
            if nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
                
        nums.extend(nums1[i:])
        nums.extend(nums2[j:])
        
        length = len(nums)
        if length % 2 == 0:
            return (nums[length/2-1]+nums[length/2])/2.0
        else:
            return nums[(length-1)/2]*1.0

    def longestPalindrome(self, s):
        """
        5 Longest Palindromic Substring
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length < 2:
            return s

        start = 0
        end = 0
        maxlen = 0
        i = 0

        while i < length:
            left, right = i, i
            while left >=0 and s[left] == s[i]:
                left -= 1
            while right < length and s[right] == s[i]:
                right += 1
            i = right

            while left >= 0 and right < length:
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    break

            if maxlen < right-left-1:
                maxlen = right-left-1
                start = left+1
                end = right

        return s[start:end]

    def convert(self, s, numRows):
        """
        6. ZigZag Conversion
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length = len(s)
        if length == 0: return ""
        if numRows == 1 or length <= numRows: return s

        string_list = [[] for i in range(numRows)]
        i = 0

        while i < length:
            for j in range(numRows-1):
                if i<length:
                    string_list[j].append(s[i])
                    i += 1
            for j in range(-1,-numRows,-1):
                if i<length:
                    string_list[j].append(s[i])
                    i += 1

        ans = []
        for i in string_list:
            ans.extend(i)

        return ''.join(ans)

    def myAtoi(self, str):
        """
        8. String to Integer (atoi)
        :type str: str
        :rtype: int
        """
        import re
        str = str.strip()
        if not str: return 0
        if str[0] not in '0123456789-+': return 0

        res = re.findall(r'^[\+|\-]?\d+', str)
        if res:
            ans = int(res[0])
            if ans > 2147483647:
                return 2147483647
            if ans < -2147483648:
                return -2147483648
            return ans
        else:
            return 0

    def reverse(self, x):
        """
        7. Reverse Integer
        :type x: int
        :rtype: int
        """
        if x>=0:
            a= int(str(x)[::-1])
        else:
            a= -int(str(-x)[::-1])
        if a > 2147483647 or a < -2147483647:
            return 0
        else:
            return a

    def maxArea(self, height):
        """
        11. Container With Most Water
        :type height: List[int]
        :rtype: int
        """
        area = 0
        i = 0
        j = len(height)-1
        while(i < j):
            if min(height[j],height[i])*(j-i) > area:
                area = min(height[j],height[i])*(j-i)
            if height[i] <= height[j]:
                i+=1
            else:
                j-=1
        return area

    def intToRoman(self, num):
        """
        12. Integer to Roman
        :type num: int
        :rtype: str
        """
        table = [
            ["","M",'MM','MMM'],
            ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'],
            ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'],
            ['','I','II','III','IV','V','VI','VII','VIII','IX']
            ]

        digit_list = []
        while num > 0:
            digit_list.insert(0, num%10)
            num /= 10

        string = ""
        for i in range(-1, -len(digit_list)-1, -1):
            string = table[i][digit_list[i]] + string

        return string

    def romanToInt(self, s):
        """
        13. Roman to Integer
        :type s: str
        :rtype: int
        """
        table = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        ans=0
        left=0
        for letter in s:
            if left < table[letter]:
                ans -= 2*left
            ans += table[letter]
            left = table[letter]

        return ans

    def longestCommonPrefix(self, strs):
        """
        14. Longest Common Prefix
        :type strs: List[str]
        :rtype: str
        """
        length = len(strs)
        if length == 0: return ''  # []
        if length == 1: return strs[0] and strs[0][0] or ''  # [""]

        minlen = min(map(lambda x: len(x), strs))
        i = 0
        done = False

        while not done and i < minlen:
            for j in range(length-1):
                if strs[j][i] != strs[j+1][i]:
                    done = True
                    break
            else:
                i += 1

        return strs[0][:i]
    



if __name__ == '__main__':
    test = Solution()
    print test.romanToInt('XIV')
        

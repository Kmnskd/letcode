class Solution:
    def removeDuplicates(self, nums) -> int:
        """
            给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
        不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
            输入：nums = [0,0,1,1,1,2,2,3,3,4]
            输出：5, nums = [0,1,2,3,4]
            解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。
        """
        left = 0
        for right in range(1, len(nums)):
            if nums[left] != nums[right]:
                left += 1
                yuanshi = nums[left]
                nums[left] = nums[right]
                nums[right] = yuanshi
        print(nums[:left + 1])
        return left + 1


    # 方法一
    def reverseString1(self, s):
        """
        编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。
        不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
        输入：s = ["h","e","l","l","o"]
        输出：["o","l","l","e","h"]
        """
        num = len(s) // 2
        end = len(s) - 1
        for i in range(num):
            # temp = s[i]
            # s[i] = s[end]
            # s[end] = temp
            s[i], s[end] = s[end], s[i]
            end -= 1
        print(s)
    # 方法二
    def reverseString2(self, s):
        start = 0
        end = len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        print(s)

    def rotate(self, nums, k):
        """
        给你一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
        输入: nums = [1,2,3,4,5,6,7], k = 3
        输出: [5,6,7,1,2,3,4]
        解释:
        向右轮转 1 步: [7,1,2,3,4,5,6]
        向右轮转 2 步: [6,7,1,2,3,4,5]
        向右轮转 3 步: [5,6,7,1,2,3,4]

        """
        length = len(nums)
        new_list = nums[length - k:]
        hf = nums[:length - k]
        ne = new_list + hf
        print(ne)

    def encrypt(self, jiami_char, jiemi_char):
        """
        字符串加密（python版）
        https://blog.csdn.net/qq_41051690/article/details/100123739
        """
        # jiami
        mystr = ""
        for i in jiami_char:
            if 65 <= ord(i) < 90:
                i = chr(ord(i) + 1).lower()
                mystr += i
            elif 97 <= ord(i) < 122:
                i = chr(ord(i) + 1).upper()
                mystr += i
            elif ord(i) == 90:
                i = "a"
                mystr += i
            elif ord(i) == 122:
                i = "A"
                mystr += i
        print(mystr)

        # jiemi
        jiemistr = ""
        for i in jiemi_char:
            if 65 < ord(i) <= 90:
                i = chr(ord(i) - 1).lower()
                jiemistr += i
            elif 97 < ord(i) <= 122:
                i = chr(ord(i) - 1).upper()
                jiemistr += i
            elif ord(i) == 65:
                i = "z"
                jiemistr += i
            elif ord(i) == 97:
                i = "Z"
                jiemistr += i
        print(jiemistr)


so = Solution()
# so.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
# so.reverseString1(["h","e","l","l","o"])
# so.reverseString1(["h","e","l","l","o"])
# so.rotate([1, 2, 3, 4, 5, 6, 7], 3)
so.encrypt("dfdsafdsgz", "BCDEFGH")

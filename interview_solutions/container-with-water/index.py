class Solution:
    def maxarea_water_container(self, a: list[int]) -> int:
        l, r = 0, len(a)-1
        max_area = 0
        while l < r:
            max_area = max(max_area,min(a[l], a[r])*(r - l))

            if a[l] < a[r]:
                l+=1
            else:
                r-=1
        return max_area

s = Solution()
a = [1,8,6,2,5,7]
print(s.maxarea_water_container(a))


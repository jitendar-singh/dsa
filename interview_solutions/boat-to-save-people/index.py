class Solution:
    def boat_to_save(self, people: list[int],weight: int) -> int:

        l_pointer, h_pointer, boats = 0, len(people)-1, 0
        people.sort()

        while(l_pointer <= h_pointer):
            if people[l_pointer] + people[h_pointer] <= weight:
                boats+=1
                l_pointer+=1
                h_pointer-=1
            elif people[h_pointer] == weight:
                boats+=1
                h_pointer-=1
            elif l_pointer == h_pointer:
                boats+=1
                break
        return boats

bts = Solution()
people = [1,2,3,2]
weight = 3
answer = bts.boat_to_save(people, weight)
print(answer)

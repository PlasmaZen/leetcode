class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sList = s.split()
        sListLast = sList[-1]
        sListLastSplit = [x for x in sListLast]
        print()
        return len(sListLastSplit)
        
sol = Solution()
print(sol.lengthOfLastWord('fly me to the moon'))
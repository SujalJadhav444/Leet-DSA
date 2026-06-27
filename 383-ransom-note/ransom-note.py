class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count = {}
        for i in range(len(magazine)):
            if magazine[i] in count:
                count[magazine[i]] += 1
            else:
                count[magazine[i]] = 1
        for i in range(len(ransomNote)):
            if ransomNote[i] not in count or count[ransomNote[i]] == 0:
                return False
            count[ransomNote[i]] -= 1
        return True
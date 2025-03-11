class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
    
        def char_count(string):
            count = {}
            for char in string:
                count[char] = count.get(char, 0) + 1
            return count
        
        p_count = char_count(p)
        s_count = char_count(s[:len(p)])
        result = []
        
        if s_count == p_count:
            result.append(0)
        
        for i in range(len(p), len(s)):
            start_ind = i - len(p)
            
            s_count[s[start_ind]] -= 1
            if s_count[s[start_ind]] == 0:
                del s_count[s[start_ind]]
            
            s_count[s[i]] = s_count.get(s[i], 0) + 1
            
            if s_count == p_count:
                result.append(start_ind + 1)
        
        return result
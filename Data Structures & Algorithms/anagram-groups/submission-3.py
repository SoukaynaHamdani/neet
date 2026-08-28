class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         
        anagram_map = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            anagram_map[tuple(count)].append(word)
        return list(anagram_map.values())
        """
        class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        # 1. كندورو على الكلمات مباشرة (Pythonic way)
        for word in strs:
             
             
            sorted_word = tuple(sorted(word))

             
            if sorted_word in anagram_map:
                anagram_map[sorted_word].append(word)
            else:
                # 4. إلا ماكاينش، كنكرييو مصفوفة جديدة وكنحطو فيها الكلمة
                anagram_map[sorted_word] = [word]

        # 5. كنرجعو القيم (المجموعات) على شكل مصفوفة ديال المصفوفات
        return list(anagram_map.values())     
          """


 
         
       
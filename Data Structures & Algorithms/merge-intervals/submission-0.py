class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Time Complexity: O(N log N)
          - Sorting takes O(N log N) using Python's Timsort.
          - Single linear scan takes O(N). 

        Space Complexity: O(N)
          - Python's Timsort requires O(N) auxiliary space in the worst case.
          - The `output` list takes O(N) space in the worst case  
        """
        # Sort intervals by start time 
        intervals.sort(key=lambda i: i[0])
        
        # Initialize output with the first interval
        output = [intervals[0]]
          
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                # Overlapping intervals -> merge by extending the end bound in-place: O(1)
                output[-1][1] = max(lastEnd, end)
            else:
                # Non-overlapping -> append 
                output.append([start, end])

        return output
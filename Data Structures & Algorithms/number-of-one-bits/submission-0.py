class Solution:
    def hammingWeight(self, n: int) -> int:
        nmbr=bin(n)[2:]
        count= nmbr.count("1")
        return count

    #o(1) space and time but not the soltution you should came up with during interv
#88


# Time:  O(n)
# Space: O(1)


# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
# You may assume that nums1 has enough space (size that is greater or equal to m + n) 
# to hold additional elements from nums2. The number of elements initialized 
# in nums1 and nums2 are m and n respectively.


class sortSol():
    def mergeSortedArray(self,nums1,len1,nums2,len2):
        last1,last2,last=len1-1,len2-1,len1+len2-1
        while last1>=0 and last2>=0:
            if nums1[last1]>nums2[last2]:
                nums1[last],last1,last=nums1[last1],last1-1,last-1
            else:
                nums1[last],last2,last=nums2[last2],last2-1,last-1
        while last2>=0:
            nums1[last],last2,last=nums2[last2],last2-1,last-1

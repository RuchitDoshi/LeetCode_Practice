class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        new_list=[]
        i=0
        j=0
        while(i < m and j<n):
            if (nums1[i] <= nums2[j]):
                new_list.append(nums1[i])
                i+=1
            else : 
                new_list.append(nums2[j])
                j+=1

        if(i>=m):
            while (j<n):
                new_list.append(nums2[j])
                j+=1
        else:
            while(i<m):
                new_list.append(nums1[i])
                i+=1
        for i in range(len(nums1)):
            nums1[i]=new_list[i]

#Solution can be improved without using additional space
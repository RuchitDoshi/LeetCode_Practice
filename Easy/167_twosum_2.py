class Solution:
    def twoSum(self, numbers, target):
        result=[]
        l=len(numbers)
        for i in range(l-1):
            new_list=numbers[i+1:]
            if target-numbers[i] in new_list:
                result.append(i+1)
                result.append(new_list.index(target-numbers[i])+2+i)
                break
        
        return result
        
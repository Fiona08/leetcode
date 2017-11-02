#75


# Given an array with n objects colored red, white or blue, 
# sort them so that objects of the same color are adjacent, 
# with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent 
# the color red, white, and blue respectively.


class sortSol():   
    def sortColors1(self,colors):
        count=[0]*3
        for color in colors:
            count[color]+=1
        sort_color=[]
        for color in range(len(count)):
            sort_color+=[color]*count[color]
        return sort_color
    
    # Time:  O(n)
    # Space: O(1)
    def sortColors2(self,colors):
        #in place    
        left,cur, right=0,0,len(colors)-1
        while cur<=right:
            if colors[cur]>1:
                colors[cur],colors[right],right=colors[right],colors[cur],right-1
            elif colors[cur]<1:
                colors[cur],colors[left],left,cur=colors[left],colors[cur],left+1,cur+1
            else:
                cur+=1

class Solution(object):
    def flipAndInvertImage(self, A):
    
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        #Horizontal Flip
        n,temp,k=0,0,1
        
        for row in A:
            
            
            row.reverse()
          
            
            # for i in range(len(row)):
            #     n=len(row)
            #     temp = row[i]
            #     row[i]=row[n-k]
            #     row[n-k] = temp
            #     k=k+1
                
                       
         #Inverted Image
        
        for row in A:
            for i in range(len(row)):
                if row[i]==1:
                    row[i]=0
                    
                else:
                    row[i]=1
                    
        
        return A
        

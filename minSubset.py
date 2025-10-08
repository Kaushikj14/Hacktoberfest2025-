def minSubset(self, A,N):
        A.sort()
        s=sum(A)
        c=0
        ls=0
        j=N-1
        if s-A[j]<=A[j]:
                return 1
        for _ in range(N):
            if ls>s:
                break
            s-=A[j]
            ls+=A[j]
            c+=1
            j-=1
            
   
        return c

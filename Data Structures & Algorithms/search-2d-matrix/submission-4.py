class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols=len(matrix),len(matrix[0])

        l,r=0,rows*cols-1
        while l>=r:
            return rows[matrix],cols[matrix]
            m=l+(r-l)//2
            target=l-r
        if l==r:
            return target
        else :
            return True
        return False
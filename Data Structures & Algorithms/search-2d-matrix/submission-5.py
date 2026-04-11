class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binary_search_in_row(target,row):
            low,high = 0,len(row)-1 
            
            while low<=high:
                mid = (low+high)//2
                if row[mid]==target:
                    return True
                elif row[mid]<target:
                    low = mid +1 
                else:
                    high = mid -1 
            return False

        
        len_rows = len(matrix)

        top,bottom = 0, len_rows-1
        while top <= bottom: 
            mid_row = (top+bottom)//2
            if target > matrix[mid_row][-1]:
                top = mid_row +1
            elif target < matrix[mid_row][0]:
                bottom = mid_row-1 

            else: 
                return binary_search_in_row(target,matrix[mid_row])
        return False


        
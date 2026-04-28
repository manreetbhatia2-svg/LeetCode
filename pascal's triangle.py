# pascal's triangle 
class Solution(object):
    def generate(self, numRows):
        out_list = []

        for i in range(numRows):
            rows = [1]*(i+1)
            out_list.append(rows)
            for j in range(1,i):
                out_list[i][j] = out_list[i-1][j-1] + out_list[i-1][j]
        print(out_list)

my_list = Solution()
(my_list.generate(5))



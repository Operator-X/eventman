class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = []
        
        for i in range(numRows):
            row = [1] * (i + 1)  # Start each row with 1s
            for j in range(1, i):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]  # Calculate the inner elements
            result.append(row)
        
        return result

# Example usage
sol = Solution()
numRows = int(input())
print(sol.generate(numRows))
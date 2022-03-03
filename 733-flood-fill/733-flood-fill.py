class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def solve(row, col, i, j, newColor, image, source):
            if i < 0 or i >= row or j < 0 or j >= col or image[i][j] != source:
                return
            image[i][j] = newColor
            solve(row, col, i, j-1, newColor, image, source)
            solve(row, col, i, j+1, newColor, image, source)
            solve(row, col, i-1, j, newColor, image, source)
            solve(row, col, i+1, j, newColor, image, source)
        row = len(image)
        col = len(image[0])
        source = image[sr][sc]
        if source == newColor:
            return image
        solve(row, col, sr, sc, newColor, image, source)
        return image
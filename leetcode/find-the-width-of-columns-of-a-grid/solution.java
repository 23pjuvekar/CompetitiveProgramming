class Solution {
    public int[] findColumnWidth(int[][] grid) {

        int[] res = new int[grid[0].length];


        // Go be cols so second index
        for (int c = 0; c < grid[0].length; c++) {
            int max = 0;
            for (int r = 0; r < grid.length; r++) {
                int temp = 0;
                if (grid[r][c] < 0) {
                    temp = 1 + (String.valueOf(-1 * grid[r][c])).length();
                } else {
                    temp = (String.valueOf(grid[r][c])).length();
                }
                if (max < temp) {
                    max = temp;
                }
            }
            res[c] = max;
        }

        return res;
        
    }
}

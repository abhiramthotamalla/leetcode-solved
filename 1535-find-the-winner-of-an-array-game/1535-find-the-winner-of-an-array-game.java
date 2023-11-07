class Solution {
    public int getWinner(int[] arr, int k) {
        int winner = arr[0];
        int c = 0;
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > winner) {
                c = 1;
                winner = arr[i];
            } else {
                c++;
            }
            if (c == k) {
                return winner;
            }
        }
        return winner;
    
    }
}
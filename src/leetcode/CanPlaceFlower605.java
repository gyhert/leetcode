package leetcode;

public class CanPlaceFlower605 {
    public static void main(String[] arg) {
        int[] flower = [0, 0, 1, 0, 1, 0, 0, 0, 0, 1];
        int t = 4;
        return canPlaceFlowers(flower, t);
    }

    public boolean canPlaceFlowers(int[] flowerbed, int n){
        int count = 0;
        for(int i = 0; i < flowerbed.length && count < n; i++){
            if(flowerbed[i] == 0){
                int next = (i == flowerbed.length - 1) ? 0 : flowerbed[i+1];
                int prev = (i == 0) ? 0 : flowerbed[i-1];
                if(next == 0 && prev == 0) {
                    flowerbed[i] = 1;
                    count++;
                }
            }
        }
        return count == n;
    }
}

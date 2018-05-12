package leetcode;

public class PaintFence276 {
    public int numways(int n, int k){
        if(n == 0) return 0;
        if(n == 1) return k;
        int same = 0, diff = k, total = k;
        for(int i = 2; i<= n; i++){
            same = diff;
            diff = (k - 1)*total;
            total = same + diff;
        }
        return total;
    }
    public static void main(String [] args){
        int n = 4;
        int k = 3;
        PaintFence276 t = new PaintFence276();
        System.out.println("total ways: " + t.numways(n,k));
    }
}

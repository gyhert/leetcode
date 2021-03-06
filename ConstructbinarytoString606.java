package leetcode;

public class ConstructbinarytoString606 {
    public String tree2str(Treenode t){
        if(t == null){
            return "";
        }
        if(t.left == null && t.right == null){
            return t.val + "";
        }
        //after that if left == null, then right will not null, and vs
        if(t.left == null){
            return t.val + "()" + "(" + tree2str(t.right) + ")";
        }
        if(t.right == null){
            return t.val + "(" + tree2str(t.left) + ")";
        }
        if(t.right == null){
            return t.val + "(" + tree2str(t.left) + ")" + "(" + tree2str(t.right) + ")";
        }
    }
}

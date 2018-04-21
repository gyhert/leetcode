package leetcode;

/**
 * Project Name: leetcode
 * package Name: leetcode
 *
 */
public class CountUnivalueSubstring {
    /**
     * given a binary tree, count the number of uni-value subtrees.
     */
    int res;
    public int CountUnivalueSubstring(TreeNode root){
        res = 0;
        helper(root);
        return res;
    }
    public boolean helper(TreeNode root){
        if(root == null) return true;
        /**
         * postorder traversal
         */
        boolean left = helper(root.left);
        boolean right = helper(root.right);

        if(left && right){
            if(root.left != null && root.val != root.left.val){
                return false;
            }
            if(root.right != null && root.val != root.right.val){
                return false;
            }
            res++;
            return true;
        }
    }
}

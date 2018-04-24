package leetcode;

public class LowestCommenAncester236 {
    public static TreeNode lowestCommenAncestor(Treenode root, TreeNode p, TreeNode q) {
        if(root == null || root == p) return root;
        TreeNode left = lowestCommenAncestor(root.left, p, q);
        TreeNode right = lowestCommenAncestor(root.right, p, q);
        if(root.left != null && root.right != null){
            return root;
        }
        return left == null? right: left;
    }
}

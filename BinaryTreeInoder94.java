package leetcode;
import java.util.LinkedList;
import java.util.List;
import MutableTreeNode;
public class BinaryTreeInoder94 {
    public list<Integer> inorderTraversal(TreeNode root) {
        linkedList<Integer> res = new LinkedList<Integer>();
        if(root == null) {
            return res;
        }
        DFS(root, res);
        return res;

    }
    public void DFS (TreeNode node, LinkedList<Integer> list) {
        if(node == null) return;
        DFS(node.left, list);
        list.add(node.val);
        DFS(node.right, list);
    }
    /**
    public static void main(String [] args){
        System.out.println("hellow world!!");
    }
}
     */

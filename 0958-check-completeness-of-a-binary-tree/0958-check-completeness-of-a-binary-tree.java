/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isCompleteTree(TreeNode root) {
        Queue<TreeNode> qu = new LinkedList<>();
        qu.offer(root);
        boolean past = false;
        while(!qu.isEmpty()){
            TreeNode curr=qu.poll();
        if(curr == null){
            past = true;
        }else{
            if(past == true){
                return false;
            }
            qu.offer(curr.left);
            qu.offer(curr.right);

        }
    }
    return true;
    }
}
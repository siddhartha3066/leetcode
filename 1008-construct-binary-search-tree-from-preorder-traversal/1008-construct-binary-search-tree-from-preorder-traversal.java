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
    public TreeNode construct(int start,int end,int[] nodes){
        if (start>end)
          return null;
        TreeNode root = new TreeNode(nodes[start]);
        int i = start+1;
        while(i<nodes.length && nodes[i]<nodes[start])
         i++;
        root.left = construct(start+1,i-1,nodes);
        root.right = construct(i,end,nodes);
        return root;
    }
    public TreeNode bstFromPreorder(int[] preorder) {
       return construct(0,preorder.length-1,preorder); 
    }
}
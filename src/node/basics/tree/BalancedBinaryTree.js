'use strict';
// Generated By lexicon-dsa CLI tool.
// Author: Saptak Sengupta(deeps.sengupta@gmail.com)
// Github: https://github.com/saptaksengupta/

// If in a tree, the absollute difference between left and 
// right subtree is greater than one then it is called as unbalanced binary tree.

function Tree(value) {
    this.value = value;
    this.left = null;
    this.right = null;
}

function isBalancedTree(root) {
    return getMaxHightOfTree(root) !== -1;
}

function getMaxHightOfTree(root) {
    if (root == null) {
        return 0;
    }

    var left = getMaxHightOfTree(root.left);
    if(left === -1) return -1;
    var right = getMaxHightOfTree(root.right);
    if (right == -1) return -1;

    if (Math.abs(left - right) > 1) return -1;
    return 1 + Math.max(left, right);
}



function main() {
    var tree = new Tree(1);
    tree.left = new Tree(2);
    tree.right = new Tree(3);
    tree.left.left = new Tree(4);
    tree.left.right = new Tree(5);
    tree.right.left = new Tree(6);
    tree.right.right = new Tree(7);
    tree.right.left.left = new Tree(8);
    tree.right.left.right = new Tree(9);
    console.log(isBalancedTree(tree));
}

main();

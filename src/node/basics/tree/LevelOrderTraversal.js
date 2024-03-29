'use strict';
// Generated By lexicon-dsa CLI tool.
// Author: Saptak Sengupta(deeps.sengupta@gmail.com)
// Github: https://github.com/saptaksengupta/


function Tree(value) {
    this.value = value;
    this.left = null;
    this.right = null;
}

function LevelOrderTraversal(root) {
    var queue = new Array();
    queue.push(root);

    while(queue.length > 0) {
        var root = queue.shift();
        console.log(root.value);

        if (root.left) {
            queue.push(root.left);
        }

        if (root.right) {
            queue.push(root.right);
        }
    }
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
    console.log(LevelOrderTraversal(tree));
}

main();


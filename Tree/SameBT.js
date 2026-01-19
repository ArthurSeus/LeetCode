// Definition for a binary tree node.
class TreeNode {
  constructor(val = 0, left = null, right = null) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}

class Solution {
  /**
   * @param {TreeNode} p
   * @param {TreeNode} q
   * @return {boolean}
   */
  isSameTree(p, q) {
    const arr1 = [];
    const arr2 = [];

    const traverseTree = (node, arr) => {
      if (!node) {
        return;
      }
      arr.push(node.val)
      const left = traverseTree(node.left, arr)
      const right = traverseTree(node.right, arr)
    }

    traverseTree(p, arr1);
    traverseTree(q, arr2);

    if (arr1.length !== arr2.length) {
      return false;
    }

    var i = 0
    while (i < arr1.length && i < arr2.length) {
      if (arr1.at(i) != arr2.at(i)) {
        return false;
      } 
      i++
    }

    return true;
  }
}

/* ---------- helpers para teste local ---------- */

function buildTree(arr) {
  if (!arr.length || arr[0] === null) return null;

  const root = new TreeNode(arr[0]);
  const queue = [root];
  let i = 1;

  while (queue.length && i < arr.length) {
    const node = queue.shift();

    if (arr[i] !== null) {
      node.left = new TreeNode(arr[i]);
      queue.push(node.left);
    }
    i++;

    if (i < arr.length && arr[i] !== null) {
      node.right = new TreeNode(arr[i]);
      queue.push(node.right);
    }
    i++;
  }

  return root;
}

function runTests() {
  const s = new Solution();

  // Example 1
  let p = buildTree([1, 2, 3]);
  let q = buildTree([1, 2, 3]);
  console.log(s.isSameTree(p, q)); // true

  // Example 2
  p = buildTree([1, 2]);
  q = buildTree([1, null, 2]);
  console.log(s.isSameTree(p, q)); // false

  // Example 3
  p = buildTree([1, 2, 1]);
  q = buildTree([1, 1, 2]);
  console.log(s.isSameTree(p, q)); // false
}

runTests();

// Definition for singly-linked list.
class ListNode {
  constructor(val = 0, next = null) {
    this.val = val;
    this.next = next;
  }
}

class Solution {
  /**
   * @param {ListNode} head
   * @param {number} n
   * @return {ListNode}
   */
  removeNthFromEnd(head, n) {
    let curr = head;
    let size = 0;
    while (curr) {
        size ++;
        curr = curr.next;
    }

    curr = head;
    let prev;
    let i = 0
    while (i < size - n) {
        i ++;
        prev = curr;
        curr = curr.next;
    }

    if (!prev) {
        return curr.next
    }
    prev.next = curr.next

    return head;
  }
}

/* ---------- helpers for local testing ---------- */

function buildList(arr) {
  if (arr.length === 0) return null;
  const head = new ListNode(arr[0]);
  let curr = head;
  for (let i = 1; i < arr.length; i++) {
    curr.next = new ListNode(arr[i]);
    curr = curr.next;
  }
  return head;
}

function listToArray(head) {
  const res = [];
  while (head) {
    res.push(head.val);
    head = head.next;
  }
  return res;
}

function runTests() {
  const s = new Solution();

  // Example 1
  let head = buildList([1, 2, 3, 4]);
  head = s.removeNthFromEnd(head, 2);
  console.log("Output:", listToArray(head)); // expected [1,2,4]

  console.log("-".repeat(40));

  // Example 2
  head = buildList([5]);
  head = s.removeNthFromEnd(head, 1);
  console.log("Output:", listToArray(head)); // expected []

  console.log("-".repeat(40));

  // Example 3
  head = buildList([1, 2]);
  head = s.removeNthFromEnd(head, 2);
  console.log("Output:", listToArray(head)); // expected [2]
}

runTests();

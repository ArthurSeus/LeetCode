class LRUCache {
    map;
  /**
   * @param {number} capacity
   */
  constructor(capacity) {
    this.capacity = capacity;
    this.cache = new Map();
  }

  /**
   * @param {number} key
   * @return {number}
   */
  get(key) {
    if (!this.cache.has(key)) {
        return -1
    }

    const value = this.cache.get(key);
    this.cache.delete(key);
    this.cache.set(key, value)
    return value
  }

  /**
   * @param {number} key
   * @param {number} value
   * @return {void}
   */
  put(key, value) {
    if (this.capacity < 1) {
        return;
    }

    if (this.cache.size === this.capacity && !this.cache.has(key)) {
        this.cache.delete(this.cache.keys().next().value);
    }

    if (this.cache.has(key)) {
        this.cache.delete(key)
    }
    this.cache.set(key, value)
  }
}

/* ---------- helpers para teste local ---------- */

function runTests() {
  const cache = new LRUCache(2);

  console.log(cache.put(1, 10)); // null
  console.log(cache.get(1));     // 10
  console.log(cache.put(2, 20)); // null
  console.log(cache.put(3, 30)); // null (evict 1)
  console.log(cache.get(2));     // 20
  console.log(cache.get(1));     // -1
}

function runTests2() {
  const cache = new LRUCache(2);

  console.log(cache.put(1, 1)); // null
  console.log(cache.put(2, 2)); // null
  console.log(cache.get(1));    // 1
  console.log(cache.put(3, 3)); // null (evict 2)
  console.log(cache.get(2));    // -1
  console.log(cache.put(4, 4)); // null (evict 1)
  console.log(cache.get(1));    // -1
  console.log(cache.get(3));    // 3
  console.log(cache.get(4));    // 4
}

function runTests3() {
  const cache = new LRUCache(2);

  console.log(cache.get(2));    // -1
  console.log(cache.put(2, 6)); // null
  console.log(cache.get(1));    // -1
  console.log(cache.put(1, 5)); // null
  console.log(cache.put(1, 2)); // null (update value)
  console.log(cache.get(1));    // 2
  console.log(cache.get(2));    // 6
}

runTests3();

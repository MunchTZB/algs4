/*
 * @Author: zhenbang.tang 
 * @Date: 2018-05-29 19:44:50 
 * @Last Modified by:   zhenbang.tang 
 * @Last Modified time: 2018-05-29 19:44:50 
 * 链表
 */

class Node {
  constructor() {
    this.item = null;
    this.next = null;
  }
}

class Stack {
  constructor() {
    this.N = 0;
    this.first = new Node();
  }

  [Symbol.iterator]() {
    let compass = null;
    return {
      next: () => {
        if (!compass) {
          compass = this.first;
        } else {
          compass = compass.next;
        }

        return {
          value: compass.item,
          done: !compass.next
        }
      }
    }
  }

  get isEmpty() {
    return this.N === 0;
  }

  get size() {
    return this.N;
  }

  push(ele) {
    const oldFirst = this.first;
    this.first = new Node();
    this.first.item = ele;
    this.first.next = oldFirst;
    this.N += 1;
  }

  pop() {
    const item = this.first.item;
    this.first = this.first.next;
    this.N -= 1;
    return item;
  }
}

const stack = new Stack();
stack.push(1);
stack.push(3);
stack.push(5);
console.log(...stack);
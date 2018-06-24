/*
 * @Author: zhenbang.tang 
 * @Date: 2018-05-29 19:44:25 
 * @Last Modified by:   zhenbang.tang 
 * @Last Modified time: 2018-05-29 19:44:25 
 * 队列
 */

const Bag = require('./Bag');

class Queue extends Bag {
  constructor() {
    super();
  }

  enqueue(ele) {
    this.add(ele);
  }

  dequeue() {
    return this.content.shift();
  }
}

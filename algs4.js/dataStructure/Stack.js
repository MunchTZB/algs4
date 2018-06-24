/*
 * @Author: zhenbang.tang 
 * @Date: 2018-05-29 19:44:33 
 * @Last Modified by:   zhenbang.tang 
 * @Last Modified time: 2018-05-29 19:44:33 
 * 堆栈
 */

const Bag = require('./Bag');

class Stack extends Bag {
  constructor() {
    super();
  }

  push(ele) {
    this.add(ele);
  }

  pop() {
    return this.content.pop();
  }
}
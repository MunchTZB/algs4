/*
 * @Author: zhenbang.tang 
 * @Date: 2018-05-29 19:45:01 
 * @Last Modified by:   zhenbang.tang 
 * @Last Modified time: 2018-05-29 19:45:01 
 * 背包
 */

class Bag {
  constructor() {
    this.content = [];
  }

  [Symbol.iterator]() {
    let index = 0;

    return {
      next:() => {
        let value = {
          value: this.content[index],
          done: index > this.content.length - 1
        }
        index ++;
        return value;
      }
    }
  }

  toString() {
    return this.content.reduce((str, item) => {
      return str.toString() + item.toString();
    })
  }

  add(ele) {
    this.content.push(ele);
  }

  get isEmpty() {
    return this.size == 0
  }

  get size() {
    return this.content.length
  }
}

module.exports = Bag;
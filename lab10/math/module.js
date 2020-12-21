
class Operation {
    /**
 * Assigns values to x and y.
 * @constructor
 * @param {number} x - The first number.
 * @param {number} y - The the second number.
 * 
 * @classdesc Represents an operation.
 */
    constructor(x, y){
        this.x = x;
        this.y = y;
    }
    /**
   * Returns sum of x and y
   * @method
   */
    sum() {
        return this.x + this.y;
    }


}
module.exports = Operation;
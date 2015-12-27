/**
 * @param {number} n
 * @return {number}
 */
var trailingZeroes = function(n) {
    var _5s = 0;
    while(n > 1) {
        n = Math.floor(n/5);
        _5s += n;
    }
    return _5s;
};

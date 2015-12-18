/**
 * @param {number[]} digits
 * @return {number[]}
 */

/*
var plusOne = function(digits) {
    var i = digits.length - 1;
    digits[i] += 1;
    var carry = 0;
    if(digits[i] >= 10) {
        digits[i] -= 10;
        carry = 1;
    }
    while(carry) {
        i -= 1;
        if(i < 0) {
            digits.unshift(1);
            return digits;
        }
        digits[i] += carry;
        carry = 0
        if(digits[i] >= 10) {
            digits[i] -= 10;
            carry = 1;
        }
    }
    return digits;
};
*/
var plusOne = function(digits) {
    var i = digits.length;
    var carry = 1;
    while(carry) {
        i -= 1;
        if(i < 0) {
            digits.unshift(1);
            return digits;
        }
        digits[i] += carry;
        carry = 0
        if(digits[i] >= 10) {
            digits[i] -= 10;
            carry = 1;
        }
    }
    return digits;
};

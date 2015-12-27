/**
 * @param {number} n
 * @return {number}
 */

/*
var factorNumber = function(n) {
    if(n === 1) return 1;
    var ans = 0;
    for(var i = 2; i <= Math.sqrt(n); i++) {
        if(n % i === 0) {
            if(i * i === n) {
                ans += 1;
            } else {
                ans += 2;
            }
        }
    }
    return ans;
};

var bulbSwitch = function(n) {
    var on = 0;
    for(var i = 1; i <= n; i++) {
        if(factorNumber(i) % 2 !== 0) {
            on ++;
        }
    }
    return on;
};

*/

var bulbSwitch = function(n) {
    return Math.floor(Math.sqrt(n));
};

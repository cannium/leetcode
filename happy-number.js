/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    var seen = {};
    var inner = function(n) {
        var s = n.toString();
        var next = 0;
        for(var i = 0; i < s.length; i++) {
            next += Number(s[i]) * Number(s[i])
        }
        if(seen[next]) {
            return false;
        }
        if(next === 1) {
            return true;
        }
        seen[next] = true;
        return inner(next);
    }
    return inner(n)
};

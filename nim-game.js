/**
 * @param {number} n
 * @return {boolean}
 */

/*
var canWinNim = function(n) {
    var dp = Array(n+1);
    dp[1] = true;
    dp[2] = true;
    dp[3] = true;
    for(var i=4; i <=n; i++) {
        dp[i] = dp[i-1] === false || dp[i-2] === false || dp[i-3] === false;
    }
    return dp[n]
};
*/

var canWinNim = function(n) {
    return (n % 4 !== 0)
}

/*
for(var j=1; j< 100; j++){
    console.log(canWinNim(j))
}
*/

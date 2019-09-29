class Solution(object):
    def dietPlanPerformance(self, calories, k, lower, upper):
        """
        :type calories: List[int]
        :type k: int
        :type lower: int
        :type upper: int
        :rtype: int
        """
        T = 0
        score = 0
        for i in range(k):
            T += calories[i]
        if T < lower:
            score -= 1
        if T > upper:
            score += 1
        for i in range(k, len(calories)):
            T = T + calories[i] - calories[i-k]
            if T < lower:
                score -= 1
            if T > upper:
                score += 1
        return score
from typing import List
import collections

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # 정렬 수행(앞에서부터 기록하기 위해서)
        logs.sort(key = lambda log: log[0])

        # years
        years = collections.defaultdict(int)

        # birth, death year 기록
        for birth, death in logs:
            for year in range(birth, death):
                years[year] += 1

        # find maximum population
        max_pop = max(years.values())

        for key, value in years.items():
            if value == max_pop:
                return key

    """
    https://leetcode.com/problems/maximum-population-year/discuss/1199494/Python-sorting-max-overlapping-segments-algorithm
    """
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        dates = []

        for birth, death in logs:
            dates.append((birth, 1))
            dates.append((death, -1))

        # 정렬 수행
        dates.sort()

        population = max_population = max_year = 0
        for year, change in dates:
            population += change
            if population > max_population:
                max_population = population
                max_year = year

        return max_year
        
logs = [[1950,1961],[1960,1971],[1970,1981]]
solution = Solution()
print(solution.maximumPopulation(logs))
# https://leetcode.com/problems/course-schedule/description/?envType=problem-list-v2&envId=topological-sort
from collections import defaultdict
from typing import List


class DFS:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_to_prerequisites = defaultdict(list)
        for prerequisite in prerequisites:
            course_to_prerequisites[prerequisite[0]].append(prerequisite[1])

        visited = set()
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False

            if course in visited:
                return True

            visiting.add(course)
            visited.add(course)

            for prerequisite in course_to_prerequisites[course]:
                if not dfs(prerequisite):
                    return False

            visiting.remove(course)
            return True

        for prerequisite in prerequisites:
            if not dfs(prerequisite[0]):
                return False
        return True


class Kahn:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisite_to_course = defaultdict(list)
        in_degree = defaultdict(int)

        for prerequisite in prerequisites:
            prerequisite_to_course[prerequisite[1]].append(prerequisite[0])
            in_degree[prerequisite[0]] += 1

        queue = []
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)

        while queue:
            prerequisite = queue.pop()
            for course in prerequisite_to_course[prerequisite]:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    queue.append(course)

        for degree in in_degree.values():
            if degree > 0:
                return False

        return True


if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1, 0]]
    # print(DFS().canFinish(numCourses, prerequisites))  # Output: True
    print(Kahn().canFinish(numCourses, prerequisites))  # Output: True


    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    # print(DFS().canFinish(numCourses, prerequisites))  # Output: False
    print(Kahn().canFinish(numCourses, prerequisites))  # Output: False

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        res = []
        visited = set()
        seen = set()

        def dfs(course):
            if course in seen:#cycle
                return False
            if course in visited: #current node/course is already validated.
                return True
            
            seen.add(course)
            for neighbor in graph[course]:
                if not dfs(neighbor): #if dfs false IE cycle,
                    return False
            
            seen.remove(course)
            visited.add(course) 
            res.append(course)
            return True

        for courseNum in range(numCourses):
            if not dfs(courseNum):
                return []
        return res
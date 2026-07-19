class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #can finish = do prerequisites form a cycle or not?
        #adjacency list

        adjList = defaultdict(list)
        for prereq in prerequisites:
            adjList[prereq[0]].append(prereq[1])
        
        inProgress = set()

        def dfs(course):
            if course in inProgress: #cycle
                return False 
            if not adjList[course]: #empty therefore True
                return True
            inProgress.add(course)
            for prereq in adjList[course]:
                if not dfs(prereq):
                    return False
            inProgress.remove(course) #this course is completely valid
            adjList[course] = [] # in the future, if any course goes into our validated course, return True (caught in the if not prereq[course])
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
        

            

        
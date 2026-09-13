class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.courseGraph = {}
        for i in range(numCourses):
            self.courseGraph[i] = []
        
        for prereq in prerequisites:
            a, b = prereq
            self.courseGraph[a].append(b)
        
        self.completed = set()
        self.completing = set()

        for course in self.courseGraph:
            if not self.detectCycle(course):
                return False
        
        return len(self.completed) == numCourses
        
    def detectCycle(self, course):
        if course in self.completed:
            return True
        
        if course in self.completing:
            return False
        
        self.completing.add(course)
        for prereq in self.courseGraph[course]:
            if not self.detectCycle(prereq):
                return False
        
        self.completed.add(course)
        self.completing.remove(course)
        return True

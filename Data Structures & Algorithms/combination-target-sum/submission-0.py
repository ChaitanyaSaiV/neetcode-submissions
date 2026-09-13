class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        # Define the recursive backtracking function
        def backtrack(current_combination, remaining_target, start_index):
            # Base Case 1: Found a combination
            if remaining_target == 0:
                # Append a copy of the combination
                result.append(list(current_combination))
                return

            # Base Case 2: Went over the target
            if remaining_target < 0:
                return

            # Recursive step: Explore candidates
            for i in range(start_index, len(candidates)):
                candidate = candidates[i]
                
                # 1. Choose (add to current combination)
                current_combination.append(candidate)
                
                # 2. Explore (make recursive call)
                # We pass 'i' (not 'i + 1') because we can reuse the same element
                backtrack(current_combination, remaining_target - candidate, i)
                
                # 3. Unchoose (backtrack - remove the element)
                current_combination.pop()

        # Start the backtracking process
        backtrack([], target, 0)
        return result
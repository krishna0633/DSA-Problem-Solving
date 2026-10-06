class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]  # Initialize with first triplet
        
        for i in range(n - 2):
            # Skip duplicate i values (optional optimization)
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                # Update closest if this sum is closer to target
                if abs(total - target) < abs(closest - target):
                    closest = total
                
                # If exact match, return immediately
                if total == target:
                    return target
                
                if total < target:
                    left += 1
                else:
                    right -= 1
        
        return closest
class Solution:
        def triangleType(self, nums: List[int]) -> str:
        #Check the triangle inequality condition
            if not (nums[0] + nums[1] > nums[2] and nums[0] + nums[2] > nums[1] and nums[2] + nums[1] > nums[0]):
                return "none"  
                # addition of 2 sides must be > the other side,if not- return "none"

            #Check if all sides are equal (equilateral)
            if nums[0] == nums[1] == nums[2]:
                return "equilateral"  # If all sides are equal, return "equilateral"
            elif nums[0] != nums[1] and nums[0] != nums[2] and nums[1] != nums[2]:
                return "scalene"  # If no two sides are equal, return "scalene"

            #If not equilateral or scalene, it is isosceles
            return "isosceles"  # Return "isosceles" as the default option
import unittest
from code import Solution  

class TestMathOperations(unittest.TestCase):
    def test_minElement(self):
        solution = Solution()  
        
        # Test cases
        
        # Small arrays
        self.assertEqual(solution.minElement([10, 12, 13, 14]), 1)  
        self.assertEqual(solution.minElement([1, 2, 3, 4]), 1)
        self.assertEqual(solution.minElement([9, 8, 7]), 7)
        self.assertEqual(solution.minElement([21, 22, 23]), 3)
        
        # Larger arrays
        self.assertEqual(solution.minElement([100, 200, 300, 400]), 1)
        self.assertEqual(solution.minElement([123, 456, 789, 987]), 12)
        self.assertEqual(solution.minElement([99, 999, 9999]), 9)
        self.assertEqual(solution.minElement([1234, 2345, 3456, 4567]), 10)
        
        # Single element
        self.assertEqual(solution.minElement([1]), 1)
        self.assertEqual(solution.minElement([9999]), 36)
        self.assertEqual(solution.minElement([7]), 7)
        
        # All identical numbers
        self.assertEqual(solution.minElement([5, 5, 5]), 5)
        self.assertEqual(solution.minElement([11, 11, 11]), 2)
        self.assertEqual(solution.minElement([1000, 1000, 1000]), 1)
        
        # All zeros (not applicable due to constraints)
        
        # Mixed numbers
        self.assertEqual(solution.minElement([45, 56, 78]), 9)
        self.assertEqual(solution.minElement([101, 202, 303]), 2)
        self.assertEqual(solution.minElement([1001, 2002, 3003]), 4)
        
        # Edge cases
        self.assertEqual(solution.minElement([5]), 5)  # Minimum input size
        
        # Large numbers within constraints
        self.assertEqual(solution.minElement([9999]), 36)
        self.assertEqual(solution.minElement([10000]), 1)
        self.assertEqual(solution.minElement([1234, 9999]), 10)
        
        # Negative numbers (if handling them)
        # Note: According to the constraints, negative numbers should not be included.
        
        # Mixed positive numbers
        self.assertEqual(solution.minElement([12, 23, 34]), 3)
        self.assertEqual(solution.minElement([45, 56, 78]), 9)
        
        # Arrays with maximum size
        self.assertEqual(solution.minElement([i + 1 for i in range(100)]), 1)  # [1, 2, ..., 100]
        self.assertEqual(solution.minElement([10000 for _ in range(100)]), 1)  # All elements are 10000
        
        # Special patterns
        self.assertEqual(solution.minElement([121, 212, 321]), 4)
        self.assertEqual(solution.minElement([909, 808, 707]), 14)
        
        # Numbers with alternating digits
        self.assertEqual(solution.minElement([1212, 3434]), 6)
        self.assertEqual(solution.minElement([5656, 7878]), 21)

        # Numbers where sum of digits are minimal
        self.assertEqual(solution.minElement([1001, 2000, 3000]), 4)
        self.assertEqual(solution.minElement([100, 200, 300]), 1)
        
        # Prime numbers within constraints
        self.assertEqual(solution.minElement([2, 3, 5, 7]), 2)
        self.assertEqual(solution.minElement([11, 13, 17, 19]), 2)

if __name__ == "__main__":
    unittest.main()

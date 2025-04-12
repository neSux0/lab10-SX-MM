from calculator import *
from unittest import TestCase

class TestCalculator(TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
    #     fill in code
        self.assertEqual(add(10,4),14)
        self.assertEqual(add(0,0),0)
        self.assertEqual(add(-5,-5),-10)
        self.assertEqual(add(0.5,0.3),0.8)

    def test_subtract(self): # 3 assertions
    #     fill in code
        self.assertEqual(sub(10, 4), 6)
        self.assertEqual(sub(0, 0), 0)
        self.assertEqual(sub(-5, -5), 0)
        self.assertEqual(sub(0.5, 0.32), 0.18)  # checks if it returns a float number
    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(7, 3), 21)
        self.assertEqual(mul(-9, 2), -18)
        self.assertEqual(mul(-5, -6), 30)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(10, 5), 2)
        self.assertEqual(div(-9, 3), -3)
        self.assertEqual(div(-8, -2), 4)
        self.assertAlmostEqual(div(10, 3), 3.33)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion #???
        with self.assertRaises(ValueError):
            div(5, 0)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(2,8),3)
        self.assertEqual(log(10,100),2)


    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0,5) #error when a== 0
        with self.assertRaises(ValueError):
            log(-5,5) #error when a == negative number
        with self.assertRaises(ValueError):
            log(1,1)  #error when b == 1
        with self.assertRaises(ValueError):
            log(1,-5) #error when b == negative number
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError): #error when a == 0
            log(0, 10)
        with self.assertRaises(ValueError): #error when a <= 0
            log(-4, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4), 5)
        self.assertEqual(hypotenuse(-6, 8), 10)
        self.assertEqual(hypotenuse(-5, -12), 13)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertEqual(square_root(16), 4)
        self.assertEqual(square_root(64), 8)

# Do not touch this
if __name__ == "__main__":
    unittest.main()
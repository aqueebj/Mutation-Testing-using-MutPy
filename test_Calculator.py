# import required libraries
import math
from unittest import TestCase

import numpy
from Calculator_2 import GCD, LCM, Ceil, Cos, Factorial, Floor, Log, Roots, Sin, Sqrt, Tan, comb, fmod, perm
# from Calculator_2 import Sci_Calculator
import mock
import builtins
# define a class
class CalculatorTest(TestCase):
    pi=3.14
    def test_GCD(self):
        self.assertEqual(GCD(18,6),6)
    def test_Fact(self):
        self.assertEqual(Factorial(5),120)
    def testFact2(self):
        self.assertEqual(Factorial(0),1)
    def testFloor(self):
        self.assertEqual(Floor(2.5),2)

    def testFloor1(self):
        self.assertEqual(Floor(2),2)

    def testFloor2(self):
        self.assertEqual(Floor(-2.5),-3)

    def testFloor3(self):
        self.assertEqual(Floor(0),0)
    def testCeil(self):
        self.assertEqual(Ceil(2.3),3)

    def testCeil1(self):
        self.assertEqual(Ceil(2),2)

    def testCeil2(self):
        self.assertEqual(Ceil(-2.3),-2)

    def testCeil3(self):
        self.assertEqual(Ceil(0),0)
    def test_comb(self):
        self.assertEqual(comb(6,2),15)
    def test_combEqual(self):
        self.assertEqual(comb(5,5),1)
    def testPerm(self):
        self.assertEqual(perm(5,2),20)
    def testPerm1(self):
        self.assertEqual(perm(5,5),120)
    def testSqrt(self):
        self.assertEqual(Sqrt(4),2)

    def testSqrt1(self):
        self.assertEqual(Sqrt(0),0)
    def testSin(self):
        self.assertAlmostEqual(round(Sin(self.pi/2)),1)

    def testCos(self):
        self.assertAlmostEqual(round(Cos(0)),1) 

    def testTan(self):
        self.assertAlmostEqual(round(Tan(self.pi/4)),1) 
    def test_lcm(self):
        with mock.patch.object(builtins, 'input', lambda _: '6 8 12'):
            self.assertEqual(LCM(self),24)
    def test_fmod(self):
        self.assertEqual(fmod(5,5),0.0)
    def test_Roots(self):
        with mock.patch.object(builtins, 'input', lambda _: '3 1 -2'):
            res = [-1.0,1.5]
            numpy.testing.assert_array_almost_equal(Roots(self),res)
    def test_log(self):
        self.assertEqual(Log(math.e),1)
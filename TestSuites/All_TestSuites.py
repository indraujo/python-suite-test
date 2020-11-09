import unittest
import sys
import os
print(os.path.join(os.path.dirname(__file__),".."))
for x in sys.path:
    print(x)

sys.path.append(os.path.join(os.path.dirname(__file__),".."))

from Package1.TC_LoginTest import LoginTest
from Package1.TC_SignupTest import SignupTest

from Package2.TC_PaymentTest import PaymentTest
from Package2.TC_PaymentReturnsTest import PaymentReturnsTest

# get all test from LoginTest,SignUpTest,PaymentTest and paymentReturntest
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

# creating test suites
sanityTestSuite = unittest.TestSuite([tc1,tc2]) #sanity test suite
functionalTestSuite = unittest.TestSuite([tc3,tc4]) #functional test suite
masterTestSuite = unittest.TestSuite([tc1,tc2,tc3,tc4]) #master test suite

unittest.TextTestRunner(verbosity=2).run(masterTestSuite)


import sys, Ice
import Demo

class PrinterI(Demo.Printer):
    def printString(self, s, current=None):
        print(s)

    def printUpperCase(self, s, current=None):
        print(s.upper())

    def printReverse(self, s, current=None):
        print(s[::-1])

class CalculatorI(Demo.Calculator):
    def add(self, a, b, current=None):
        return a + b

    def multiply(self, a, b, current=None):
        return a * b

communicator = Ice.initialize(sys.argv)

adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 11000")
adapter.add(PrinterI(), communicator.stringToIdentity("SimplePrinter"))
adapter.add(CalculatorI(), communicator.stringToIdentity("SimpleCalculator"))
adapter.activate()

communicator.waitForShutdown()

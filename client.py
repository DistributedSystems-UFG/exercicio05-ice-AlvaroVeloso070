import sys, Ice
import Demo

with Ice.initialize(sys.argv) as communicator:
    base = communicator.stringToProxy("SimplePrinter:default -p 11000")
    printer = Demo.PrinterPrx.checkedCast(base)
    if not printer:
        raise RuntimeError("Invalid proxy")

    printer.printString("Hello World!")
    printer.printUpperCase("hello uppercase")
    printer.printReverse("hello reverse")

    calcBase = communicator.stringToProxy("SimpleCalculator:default -p 11000")
    calculator = Demo.CalculatorPrx.checkedCast(calcBase)
    if not calculator:
        raise RuntimeError("Invalid proxy")

    print(f"10 + 5 = {calculator.add(10, 5)}")
    print(f"10 * 5 = {calculator.multiply(10, 5)}")

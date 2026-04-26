module Demo
{
    interface Printer
    {
        void printString(string s);
        void printUpperCase(string s);
        void printReverse(string s);
    }

    interface Calculator
    {
        int add(int a, int b);
        int multiply(int a, int b);
    }
}

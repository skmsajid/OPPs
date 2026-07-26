#Method Overloading(static Binding/ Compiletime Polimorphism) means when we have multiple methods with same name with different 
#then method for execution will be choosen at compile time
""""
class Calculator {
    // Method 1: Two parameters
    int add(int a, int b) { 
        return a + b; 
    }
    
    // Method 2: Three parameters (Overloaded)
    int add(int a, int b, int c) { 
        return a + b + c; 
    }

    public static void main(String[] args) {
        Calculator calc = new Calculator();
        System.out.println(calc.add(2, 3));     // Prints 5
        System.out.println(calc.add(2, 3, 4));  // Prints 9
    }
}
"""
#but in python , Python does not support method overloading
#because, if we have multiple methods with same name with different , then 
#python atomatically chooses the last method 
# even though it does not support , we can achieve method overloading 
class MO:
    def add(self,a=0,b=0,c=0):
        return a+b+c
mo=MO()
print(mo.add(12,23))
print(mo.add(12,2,3))
#OR
class Calculator:
    # Accepts an unlimited list of numbers
    def add(self, *args):
        print(args)
        return sum(args)

calc = Calculator()
print(calc.add(2, 3))        # Prints 5
print(calc.add(2, 3, 4, 5))  # Prints 14


def is_equilateral(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
         return False  
    if a + b <= c or a + c <= b or b + c <= a:
         return False  
    return a == b == c

def main():
     print("Enter the lengths of the three sides of the triangle:")
     try:
         a = float(input("Side 1: "))
         b = float(input("Side 2: "))
         c = float(input("Side 3: "))

         if is_equilateral(a, b, c):
             print("The triangle is an equilateral triangle.")
         else:
             print("The triangle is NOT an equilateral triangle.")
     except ValueError:
         print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
     main()
 

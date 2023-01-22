using System;

class MainProgram
{
    // Calculator class
    // Add method here - this is the method that will be called from the Main method to add two numbers
    public static int Add(int x, int y)
    {
        return x + y;
    }

    // Comparison class
    // Comparison method here - this is the method that will be called from the Main method to compare two numbers
    public static void Compare(int x, int y)
    {
        if (x > y)
        {
            Console.WriteLine("x is greater than y");
        }
        else
        {
            Console.WriteLine("x is not greater than y");
        }
    }

    // Counter class
    // Counter method here - this is the method that will be called from the Main method to count from 0 to the number of iterations specified by the user
    public static void Count(int iterations)
    {
        for (int i = 0; i < iterations; i++)
        {
            Console.WriteLine(i);
        }
    }

    // Person class
    // Person class here - this is the class that will be used to store the name and age of a person
    public class Person
    {
        public string name;
        public int age;

        public void PrintInfo()
        {
            Console.WriteLine("Name: " + name);
            Console.WriteLine("Age: " + age);
        }
    }

    // Structure class
    // Coordinates structure here - this is the structure that will be used to store the coordinates of two points
    public struct Coordinates
    {
        public int x;
        public int y;
    }
    // Distance method here - this is the method that will be called from the Main method to calculate the distance between two points
    public static double Distance(Coordinates point1, Coordinates point2)
    {
        int xDiff = point2.x - point1.x;
        int yDiff = point2.y - point1.y;
        // Pythagorean theorem to calculate the distance between two points (x1, y1) and (x2, y2) is the square root of (x2 - x1)^2 + (y2 - y1)^2 
        double distance = Math.Sqrt((xDiff * xDiff) + (yDiff * yDiff));
        return distance;
    }
    // Main method here - this is the method that will be called when the program is run from the command line (i.e. dotnet run)
    public static void Main(string[] args)
    {
        Console.WriteLine("Select the program you want to run:");
        Console.WriteLine("1. Calculator");
        Console.WriteLine("2. Comparison");
        Console.WriteLine("3. Counter");
        Console.WriteLine("4. Person Info");
        Console.WriteLine("5. Structure");

        int choice = int.Parse(Console.ReadLine());
// here is the switch statement that you need to use to call the appropriate method based on the user's choice
        switch (choice)
        {
            // Calculator class call here (case 1)
            case 1:
                Console.WriteLine("Enter the first number: ");
                int x = int.Parse(Console.ReadLine());
                Console.WriteLine("Enter the second number: ");
                int y = int.Parse(Console.ReadLine());
                int sum = Add(x, y);
                Console.WriteLine("The sum of x and y is: " + sum);
                break;
            // Comparison class call here (case 2)
            case 2:
                Console.WriteLine("Enter the first number: ");
                x = int.Parse(Console.ReadLine());
                Console.WriteLine("Enter the second number: ");
                y = int.Parse(Console.ReadLine());
                Compare(x, y);
                break;
            // Counter class call here (case 3)
            case 3:
                Console.WriteLine("Enter the number of iterations: ");
                int iterations = int.Parse(Console.ReadLine());
                Count(iterations);
                break;
            // Person class call here (case 4)
            case 4:
                Person person1 = new Person();
                Console.WriteLine("Enter the name: ");
                person1.name = Console.ReadLine();
                Console.WriteLine("Enter the age: ");
                person1.age = int.Parse(Console.ReadLine());
                person1.PrintInfo();
                break;
            // Structure class call here (case 5)
            case 5:
                Coordinates point1;
                Coordinates point2;
                Console.WriteLine("Enter the x coordinate for point 1: ");
                point1.x = int.Parse(Console.ReadLine());
                Console.WriteLine("Enter the y coordinate for point 1: ");
                point1.y = int.Parse(Console.ReadLine());
                Console.WriteLine("Enter the x coordinate for point 2: ");
                point2.x = int.Parse(Console.ReadLine());
                Console.WriteLine("Enter the y coordinate for point 2: ");
                point2.y = int.Parse(Console.ReadLine());
                double distance = Distance(point1, point2);
                Console.WriteLine("The distance between the two points is: " + distance);
                break;
            // Default case here (case 0) - this is the default case that will be executed if the user enters a number that is not 1, 2, 3, 4, or 5
            default:
                Console.WriteLine("Invalid choice");
                break;
        }
    }
}

using System;

class Program
{
    static void Main()
    {
        int rows = 5;
        int cols = 4;
        
        int[,] matrix = new int[rows, cols];
        
        Console.WriteLine("Введіть елементи матриці:");
        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                Console.Write($"Елемент [{i + 1}, {j + 1}]: ");
                matrix[i, j] = int.Parse(Console.ReadLine());
            }
        }
        Console.WriteLine("\nМатриця до:");
        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                Console.Write(matrix[i, j] + " ");
            }
            Console.WriteLine();
        }
        
        Console.Write("Введіть значення: ");
        int temp = int.Parse(Console.ReadLine());

        int count = 0; 
        int sum = 0;  
        
        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                if (matrix[i, j] < temp)
                {
                    sum += matrix[i, j];
                    count++;
                    matrix[i, j] = 0;
                }
            }
        }
        
        Console.WriteLine("\nМатриця після:");
        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                Console.Write(matrix[i, j] + " ");
            }
            Console.WriteLine();
        }
        
        Console.WriteLine($"\nКількість елементів: {count}");
        Console.WriteLine($"Сума елементів: {sum}");
    }
}
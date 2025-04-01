using System;

class Program
{
   
    static int[] CountGreaterElements(int[][] jaggedArray, int threshold)
    {
        int[] result = new int[jaggedArray.Length];

        for (int i = 0; i < jaggedArray.Length; i++)
        {
            int count = 0;
            foreach (int element in jaggedArray[i])
            {
                if (element > threshold)
                {
                    count++;
                }
            }
            result[i] = count;
        }
        return result;
    }

    static void Main()
    {
        int[][] jaggedArray = new int[][]
        {
            new int[] { 1, 5, 3, 7 },
            new int[] { 2, 8, 10, 4 },
            new int[] { 6, 3, 9, 2, 5 },
            new int[] { 7, 0, 12, 15 }
        };
        
        Console.Write("Введіть число число: ");
        int threshold = int.Parse(Console.ReadLine());
        
        int[] result = CountGreaterElements(jaggedArray, threshold);
        
        Console.WriteLine("\nКількість елементів більших за порогове число в кожному рядку:");
        for (int i = 0; i < result.Length; i++)
        {
            Console.WriteLine($"Рядок {i + 1}: {result[i]} елементів більших за {threshold}");
        }
    }
}
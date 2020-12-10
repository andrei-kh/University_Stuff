using System;
using System.Linq;

namespace lab_1_c_
{
    class Program
    {
        public static void Main(string[] args)
        {
            int start_time = DateTime.Now.Millisecond;

            double[,] matrix = new double[3, 3];
            double[] suminline = new double[3];
            Random random = new Random();
            for (int i = 0; i < matrix.GetLength(0); i++)
                for (int j = 0; j < matrix.GetLength(1); j++)
                {
                    matrix[i, j] = random.NextDouble() * (200.0) - 100.0;
                    suminline[i] += Math.Abs(matrix[i, j]);
                }

            double normal = suminline.Max();
            for (int i = 0; i < matrix.GetLength(0); i++)
            {
                for (int j = 0; j < matrix.GetLength(1); j++)
                    Console.Write(matrix[i, j] + " ");
                Console.WriteLine();
            }

            int end_time = DateTime.Now.Millisecond;
            Console.WriteLine("Normal: " + normal);
            Console.WriteLine("Time: " + (end_time - start_time) + " ms");
        }
    }
}

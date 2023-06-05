using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace kontrolltoo
{
    internal class susik
    {
        public static void Main(string[] args)
        {
            //string[] perenimi = { "Kulakova", "Abudabiev", "Mere", "Zimarina", "Smirnov" };
            //Console.WriteLine(perenimi[0]);
            //Console.WriteLine(perenimi[1]);
            //Console.WriteLine(perenimi[2]);
            //Console.WriteLine(perenimi[3]);
            //Console.WriteLine(perenimi[4]);

            //string pikkperenimi = perenimi[0];
            //for (int i = 1; i < perenimi.Length; i++)
            //{
            //    if (perenimi[i].Length > pikkperenimi.Length)
            //    {
            //        pikkperenimi = perenimi[i];
            //    }
            //}


            //Console.WriteLine("Kõige pikkem perekonnanimi on: " + pikkperenimi);

            //Console.Write("SIsestage oma nimi: ");
            //string nimi = Console.ReadLine();

            //// ljuboe imja
            //char[] letters = new char[nimi.Length];
            //for (int i = 0; i < nimi.Length; i++)
            //{
            //    letters[i] = nimi[i];
            //}

            //// vjivod na ekar s probelami
            //Console.WriteLine("Teie nimi on:");
            //foreach (char letter in letters)
            //{
            //    Console.Write(letter + " ");
            //}

            //// koli4estvo bykv
            //int vowelsCount = 0;
            //int consonantsCount = 0;
            //string vowels = "AEIOUYaeiouy"; // Список гласных букв
            //foreach (char letter in letters)
            //{
            //    if (vowels.Contains(letter))
            //    {
            //        vowelsCount++;
            //    }
            //    else
            //    {
            //        consonantsCount++;
            //    }
            //}

            //// vjivesti na ekran
            //Console.WriteLine("\nTäishäälikute arv teie nimes: " + vowelsCount);
            //Console.WriteLine("Konsonantide arv teie nimes: " + consonantsCount);

            // random 4isla s plav zjapjatoj
            double[] numbers = new double[10];
            Random random = new Random();
            for (int i = 0; i < numbers.Length; i++)
            {
                numbers[i] = random.NextDouble() * 100; // Генерируем случайное число от 0 до 100
            }

            // max min
            for (int i = 0; i < numbers.Length; i++)
            {
                Console.WriteLine(numbers[i]);
            }
               
              
            double maxNumber = numbers[0];
            double minNumber = numbers[0];
            for (int i = 1; i < numbers.Length; i++)
            {
                if (numbers[i] > maxNumber)
                {
                    maxNumber = numbers[i];
                }
                if (numbers[i] < minNumber)
                {
                    minNumber = numbers[i];
                }
            }

            // vjivod
            Console.WriteLine("max number: " + maxNumber);
            Console.WriteLine("min number: " + minNumber);


        }
    }
}

    


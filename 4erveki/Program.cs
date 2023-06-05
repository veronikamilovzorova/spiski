using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;

namespace Snake
{
    class Program
    {
        static void Main(string[] args)
        {
            int speed = 170;
            int score = 0;
            Console.SetWindowSize(90, 25);

            Walls walls = new Walls(80, 25);
            walls.Draw();

            // Отрисовка точек			
            Point p = new Point(4, 5, '*');
            Snake snake = new Snake(p, 4, Direction.RIGHT);
            snake.Draw();

            FoodCreator foodCreator = new FoodCreator(80, 25, '$');
            Point food = foodCreator.CreateFood();
            food.Draw();
            FoodCreator foodik = new FoodCreator(80, 25, '¤');
            Point food2 = foodik.skorosti();
            food2.Draw();
            FoodCreator foodiik = new FoodCreator(80, 25, '/');
            Point food3 = foodiik.mini();
            food3.Draw();



            while (true)
            {
                ReadText(score);
                if (walls.IsHit(snake) || snake.IsHitTail())
                {
                    break;
                }
                if (snake.Eat(food))
                {
                    food = foodCreator.CreateFood();
                    food.Draw();
                    score++;
                    WriteText($"score: {score}", 81, 8);
                }
                else if (snake.Eat2(food2))
                {
                    food2 = foodik.skorosti();
                    food2.Draw();
                    speed = 70;
                    score++;


                }
                else if (snake.Eat3(food3))
                {
                    food3 = foodiik.mini();
                    food3.Draw();
                    speed = 200;
                    score++;


                }
                else
                {
                    snake.Move();
                }

                Thread.Sleep(speed);
                if (Console.KeyAvailable)
                {
                    ConsoleKeyInfo key = Console.ReadKey();
                    snake.HandleKey(key.Key);
                }
            }
            WriteGameOver(score);
            WriteTxt(score);
            Console.ReadLine();

        }


        static void WriteGameOver(int score)

        {
            int xOffset = 25;


            WriteText($"score: {score}", 81, 8);
            int yOffset = 8;
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.SetCursorPosition(xOffset, yOffset++);
            WriteText("============================", xOffset, yOffset++);
            WriteText("G A M E  O V E R", xOffset + 1, yOffset++);
            yOffset++;
            WriteText("Autor: Veronika Milovzorova", xOffset + 2, yOffset++);
            WriteText($"score: {score}", xOffset + 2, yOffset++);


            WriteText("============================", xOffset, yOffset++);
        }

        static void WriteText(String text, int xOffset, int yOffset)
        {
            Console.SetCursorPosition(xOffset, yOffset);
            Console.WriteLine(text);

        }
        static void WriteTxt(int score)
        {

            string path = "../../../ogbuda.txt";


            using (StreamWriter writer = new StreamWriter(path, true))
            {
                int text = score;


                writer.WriteLine(text);
            }
        }
        static void ReadText(int score)
        {
            string path = "../../../ogbuda.txt";
            int maxNumber = ReadMaxNumberFromFile(path);

            WriteText($"best score: {maxNumber}", 40, 25);

            if (score <= maxNumber)
            {
                WriteText($"score: {score}", 81, 8);
            }
            else if (score > maxNumber)
            {
                WriteText($"score: {score}", 81, 8);
                WriteText($"best score: {score}", 80, 8);
            }
        }

        static int ReadMaxNumberFromFile(string filePath)
        {
            int maxNumber = int.MinValue;
            bool foundNumber = false;

            using (StreamReader reader = new StreamReader(filePath))
            {
                string line;
                while ((line = reader.ReadLine()) != null)
                {
                    if (int.TryParse(line, out int number))
                    {
                        if (!foundNumber || number > maxNumber)
                        {
                            maxNumber = number;
                            foundNumber = true;
                        }
                    }
                }
            }

            if (foundNumber)
            {
                return maxNumber;
            }
            else
            {
                // Возвращаемое значение, если не найдено ни одного числа
                return 0; // Или int.MinValue, в зависимости от требований
            }
        }
    }
}

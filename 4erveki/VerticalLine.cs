﻿using _4erveki;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Snake
{
	class Walls
	{
		List<Figure> wallList;

		public Walls( int mapWidth, int mapHeight )
		{
			wallList = new List<Figure>();
            Console.ForegroundColor = ConsoleColor.Green;

            // Отрисовка рамочки
            HorizontalLine upLine = new HorizontalLine( 0, mapWidth - 2, 0, '+' );
			HorizontalLine downLine = new HorizontalLine( 0, mapWidth - 2, mapHeight - 1, '+' );
			VerticalLinee leftLine = new VerticalLinee( 0, mapHeight - 1, 0, '+' );
			VerticalLinee rightLine = new VerticalLinee( 0, mapHeight - 1, mapWidth - 2, '+' );

			wallList.Add( upLine );
			wallList.Add( downLine );
			wallList.Add( leftLine );
			wallList.Add( rightLine );
		}

		internal bool IsHit( Figure figure )
		{
			foreach(var wall in wallList)
			{
				if(wall.IsHit(figure))
				{
					return true;
				}
			}
			return false;
		}

		public void Draw()
		{
			foreach ( var wall in wallList )
			{
				wall.Draw();
			}
		}
	}
}

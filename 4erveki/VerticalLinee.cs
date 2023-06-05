using Snake;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _4erveki
{
    internal class VerticalLinee : Figure
    {
        public VerticalLinee(int yUp, int Ydown, int x, char sym) 
         { 
            pList = new List<Point>();
            for(int y = yUp; y <=Ydown; y++) 
            {
                Point p = new Point(x, y,sym);
                pList.Add(p);
            }
         }
    }
}

using System;
using System.IO;
namespace atestation
{
    class Program
    {
        static void Main(string[] args)
        {
            //Taxipark
            StreamReader sr = File.OpenText("input.txt");
            string[] s;
            while((s = sr.ReadLine().Split()) != null)
            {
                if(s[0] + " " + s[1] == "cargo taxi")
                {
                    var mem = new CargoTaxi(s[2], s[3], Int32.Parse(s[4]), Int32.Parse(s[5]), Int32.Parse(s[6]), Int32.Parse(s[7]), Int32.Parse(s[8]));
                }
                else if(s[0] + " " + s[1] == "passenger taxi")
                {
                    var mem = new PassengerTaxi(s[2], s[3], Int32.Parse(s[4]), Int32.Parse(s[5]), Int32.Parse(s[6]), Int32.Parse(s[7]), Int32.Parse(s[8]));
                }
            }

            

        }
    }
}

using System;
using ObjectInstances;
using Objects;
using System.Xml.Serialization;
using System.IO;

namespace task_3
{
    class Program
    {
        static void Main(string[] args)
        {
            Airline someAirline = new Airline("SomeAirline");
            someAirline.addAircraft(new Cessna172());
            someAirline.addAircraft(new Cessna172());
            someAirline.addAircraft(new BoeingC17());
            someAirline.addAircraft(new Boeing737());
            someAirline.addAircraft(new AirbusA320());

            Console.WriteLine(someAirline.ToString());
            someAirline.sortPanesByFlightRange();
            Console.WriteLine(someAirline.ToString());

            foreach(var aircraft in someAirline.filterAircraftsByFuelConsuption(2000, 3000))
            {
                Console.WriteLine(aircraft.ToString());
            }

            Console.WriteLine();
            Console.WriteLine("Total cargo capacity: " + someAirline.calculateTotalCargoCapacity());
            Console.WriteLine("Total seats capacity: " + someAirline.calculateTotalSeatCapacity());
            Console.WriteLine();

            SerializeAirline(someAirline);

            var someAirline1 = DeserializeAirline();
            Console.WriteLine(someAirline1.ToString());
        }
        static void SerializeAirline(Airline airline)
        {
            XmlSerializer xml = new XmlSerializer(typeof(Airline));
            using(FileStream fileStream = new FileStream("Airline.xml", FileMode.Create))
                xml.Serialize(fileStream, airline);
        }
        static Airline DeserializeAirline()
        {
            XmlSerializer xml = new XmlSerializer(typeof(Airline));
            using (FileStream fileStream = new FileStream("Airline.xml", FileMode.OpenOrCreate))
                return  (Airline)xml.Deserialize(fileStream);
        }
    }
}

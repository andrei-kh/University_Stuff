using System;
using ObjectInstances;
using Objects;
using System.Xml.Serialization;
using System.IO;
using Objects.Exceptions;

namespace task_3
{
    class Program
    {
        static void Main(string[] args)
        {
            Airline someAirline = new Airline("SomeAirline");
            try
            {
                someAirline.removeAircraft(199);
                someAirline.addAircraft(new LightAircraft("a", "b", 1, 2, 3, 0));
                someAirline.addAircraft(new LightAircraft("a", "b", 1, 2, 3, 0));
                someAirline.addAircraft(ReadyAircrafts.Airbus320);
                someAirline.addAircraft(ReadyAircrafts.Boeing737);
                someAirline.addAircraft(ReadyAircrafts.Cessna172);
                someAirline.addAircraft(ReadyAircrafts.BoeingC17);

                Console.WriteLine(someAirline.ToString());
                someAirline.sortPanesByFlightRange();
                Console.WriteLine(someAirline.ToString());

                foreach (var aircraft in someAirline.filterAircraftsByFuelConsuption(2000, 3000))
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
            catch(AirlineContainerException e)
            {
                SerializeAirline(someAirline);
                Console.WriteLine(e.GetType().FullName);
                Console.WriteLine(e.Message);
            }
            catch (AircraftValueException e)
            {
                Console.WriteLine(e);
            }
            catch (AircraftCreationException e)
            {
                Console.WriteLine(e.GetType().FullName);
                Console.WriteLine(e.Message);
            }
            catch (Exception e)
            {
                Console.WriteLine("Unknown exception caught: {0}.", e);
            }
        }
        static void SerializeAirline(Airline airline)
        {
            XmlSerializer xml = new XmlSerializer(typeof(Airline));
            using (FileStream fileStream = new FileStream("Airline.xml", FileMode.Create))
                xml.Serialize(fileStream, airline);
        }
        static Airline DeserializeAirline()
        {
            XmlSerializer xml = new XmlSerializer(typeof(Airline));
            using (FileStream fileStream = new FileStream("Airline.xml", FileMode.OpenOrCreate))
                return (Airline)xml.Deserialize(fileStream);
        }
    }
}

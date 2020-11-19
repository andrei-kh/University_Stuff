using System;
using System.Collections.Generic;
using System.Linq;
using System.Xml.Serialization;
using Objects;
using System.Text;

namespace ObjectInstances
{
    [XmlInclude(typeof(AirbusA320))]
    [XmlInclude(typeof(Boeing737))]
    [XmlInclude(typeof(BoeingC17))]
    [XmlInclude(typeof(Cessna172))]

    public class Airline
    {
        public string airlineName;
        public Airline()
        {
            aircrafts = new List<Aircraft>();
        }
        public Airline(string airlineName)
        {
            this.airlineName = airlineName;
            aircrafts = new List<Aircraft>();
        }
        public List<Aircraft> aircrafts { get; }
        public void addAircraft(Aircraft aircraft)
        {
            aircrafts.Add(aircraft);
        }
        public int calculateTotalCargoCapacity() => aircrafts.Sum(x => x.getCargoCapacity());
        public int calculateTotalSeatCapacity() => aircrafts.Sum(x => x.getSeatCapacity());
        public void sortPanesByFlightRange()
        {
            aircrafts.Sort(new AicraftComparerByFlightRange());
        }
        public List<Aircraft> filterAircraftsByFuelConsuption(int minConsuption, int maxConsuption) =>
        aircrafts.Where(x => x.fuelConsumption >= minConsuption && x.fuelConsumption <= maxConsuption).ToList();

        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append($"{this.airlineName} airline:\n");
            foreach (var aircraft in aircrafts)
                sb.Append(aircraft.ToString() + '\n');

            return sb.ToString();
        }
    }
}
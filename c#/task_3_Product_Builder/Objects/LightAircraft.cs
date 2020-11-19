using System;
using System.Xml.Serialization;

namespace Objects
{
    public abstract class LightAircraft : Aircraft
    {
        public int seatCapacity { get; set; }
        public LightAircraft() { }
        public LightAircraft(string aircraftManufacturer, string aircraftModel, int seatCapacity, int flightRange, int fuelConsumption)
        : base(aircraftManufacturer, aircraftModel, flightRange, fuelConsumption)
        {
            this.seatCapacity = seatCapacity;
        }
        public override int getSeatCapacity()
        {
            return seatCapacity;
        }
        public override int getCargoCapacity()
        {
            return 0;
        }
    }
}

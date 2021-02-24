using System;
using System.Xml.Serialization;
using Objects.Exceptions;

namespace Objects
{
    public class LightAircraft : Aircraft
    {
        public int seatCapacity { get; set; }
        public LightAircraft() { }
        public LightAircraft(string aircraftManufacturer, string aircraftModel, int seatCapacity, int flightRange, int fuelConsumption, int id)
        : base(aircraftManufacturer, aircraftModel, flightRange, fuelConsumption, id)
        {
            if (seatCapacity < 0)
                throw new AircraftCreationException("Seat Capacity must be greater or equal to 0");
            this.seatCapacity = seatCapacity;
        }
        public override int getSeatCapacity()
        {
            if (seatCapacity < 0)
                throw new AircraftValueException("Seat Capacity Value is lower than 0");
            return seatCapacity;
        }
        public override int getCargoCapacity()
        {
            return 0;
        }
    }
}

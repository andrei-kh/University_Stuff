using System;
using System.Xml.Serialization;

namespace Objects
{
    public abstract class CommercialAircraft : Aircraft
    {
        public int seatCapacity { get; set; }
        public int cargoCapacity { get; set; }
        public CommercialAircraft() { }
        public CommercialAircraft(string aircraftManufacturer, string aircraftModel, int seatCapacity,
        int cargoCapacity, int flightRange, int fuelConsumption)
        : base(aircraftManufacturer, aircraftModel, flightRange, fuelConsumption)
        {
            this.seatCapacity = seatCapacity;
            this.cargoCapacity = cargoCapacity;
        }
        public override int getSeatCapacity()
        {
            return seatCapacity;
        }
        public override int getCargoCapacity()
        {
            return cargoCapacity;
        }
    }
}

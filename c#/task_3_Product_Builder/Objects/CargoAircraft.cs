using System;
using System.Xml.Serialization;

namespace Objects
{
    public abstract class CargoAircraft : Aircraft
    {
        public int cargoCapacity { get; set; }
        public CargoAircraft() { }
        public CargoAircraft(string aircraftManufacturer, string aircraftModel, int flightRange, int fuelConsumption, int cargoCapacity)
        : base(aircraftManufacturer, aircraftModel, flightRange, fuelConsumption)
        {
            this.cargoCapacity = cargoCapacity;
        }
        public override int getCargoCapacity()
        {
            return cargoCapacity;
        }
        public override int getSeatCapacity()
        {
            return 0;
        }
    }
}

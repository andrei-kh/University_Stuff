using System;
using System.Xml.Serialization;
using Objects.Exceptions;

namespace Objects
{
    public class CargoAircraft : Aircraft
    {
        public int cargoCapacity { get; set; }
        public CargoAircraft() { }
        public CargoAircraft(string aircraftManufacturer, string aircraftModel, int flightRange, int fuelConsumption, int cargoCapacity, int id)
        : base(aircraftManufacturer, aircraftModel, flightRange, fuelConsumption, id)
        {
            if(cargoCapacity < 0)
                throw new AircraftCreationException("Cargo Capacity must be greater or equal to zero");
            this.cargoCapacity = cargoCapacity;
        }
        public override int getCargoCapacity()
        {
            if(cargoCapacity < 0)
                throw new AircraftValueException("Cargo Capacity Value is lower than 0");
            return cargoCapacity;
        }
        public override int getSeatCapacity()
        {
            return 0;
        }
    }
}

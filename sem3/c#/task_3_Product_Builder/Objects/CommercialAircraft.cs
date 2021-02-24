using System;
using System.Xml.Serialization;
using Objects.Exceptions;

namespace Objects
{
    public class CommercialAircraft : Aircraft
    {
        public int seatCapacity { get; set; }
        public int cargoCapacity { get; set; }
        public CommercialAircraft() { }
        public CommercialAircraft(string aircraftManufacturer, string aircraftModel, int seatCapacity,
        int cargoCapacity, int flightRange, int fuelConsumption, int id)
        : base(aircraftManufacturer, aircraftModel, flightRange, fuelConsumption, id)
        {
            if (cargoCapacity < 0)
                throw new AircraftCreationException("Cargo Capacity must be greater or equal to 0");
            if (seatCapacity < 0)
                throw new AircraftCreationException("Seat Capacity must be greater or equal to 0");
            this.seatCapacity = seatCapacity;
            this.cargoCapacity = cargoCapacity;
        }
        public override int getSeatCapacity()
        {
            if (seatCapacity < 0)
                throw new AircraftValueException("Seat Capacity Value is lower than 0");
            return seatCapacity;
        }
        public override int getCargoCapacity()
        {
            if (cargoCapacity < 0)
                throw new AircraftValueException("Cargo Capacity Value is lower than 0");
            return cargoCapacity;
        }
    }
}

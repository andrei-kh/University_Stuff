using System;
using System.Xml.Serialization;
using System.Text;
using Objects.Exceptions;
using System.Linq;

namespace Objects
{
    public abstract class Aircraft
    {
        public int id { get; set; }
        public string aircraftManufacturer { get; set; }
        public string aircraftModel { get; set; }
        public int flightRange { get; set; }
        public int fuelConsumption { get; set; }
        public Aircraft() { }
        public Aircraft(string aircraftManufacturer, string aircraftModel, int flightRange, int fuelConsumption, int id)
        {
            if (aircraftManufacturer == string.Empty)
                throw new AircraftCreationException("Aircraft Manufacturer can't be an empty string");
            if (aircraftModel == string.Empty)
                throw new AircraftCreationException("Aircraft Model can't be an empty string");
            if (flightRange < 0)
                throw new AircraftCreationException("Flight Range must bew greater or equal to 0");
            if (fuelConsumption < 0)
                throw new AircraftCreationException("Fuel Consuption must bew greater or equal to 0");
            if (id < -1)
                throw new AircraftCreationException("Id must be -1 or higher");
            this.id = id;
            this.aircraftManufacturer = aircraftManufacturer;
            this.aircraftModel = aircraftModel;
            this.flightRange = flightRange;
            this.fuelConsumption = fuelConsumption;
        }
        public abstract int getSeatCapacity();
        public abstract int getCargoCapacity();

        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append(String.Format("Aircraft {0}|{1, 7}{2, 7} | ", this.id, this.aircraftManufacturer, this.aircraftModel));
            sb.Append(String.Format("Seat capacity: {0,5} | ", this.getSeatCapacity()));
            sb.Append(String.Format("Cargo capacity: {0, 5} | ", this.getCargoCapacity()));
            sb.Append(String.Format("Flight range: {0, 5} | ", this.flightRange));
            sb.Append(String.Format("Fuel consuption: {0, 5} | ", this.fuelConsumption));
            return sb.ToString();
        }
    }
}

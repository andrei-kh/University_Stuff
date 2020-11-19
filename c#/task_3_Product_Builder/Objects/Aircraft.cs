using System;
using System.Xml.Serialization;
using System.Text;


namespace Objects
{
    public abstract class Aircraft
    {
        public string aircraftManufacturer { get; set; }
        public string aircraftModel { get; set; }
        public int flightRange { get; set; }
        public int fuelConsumption { get; set; }
        public Aircraft() { }
        public Aircraft(string aircraftManufacturer, string aircraftModel, int flightRange, int fuelConsumption)
        {
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
            sb.Append($"Aircraft {this.aircraftManufacturer}{this.aircraftModel} ");
            sb.Append($"Seat capacity: {this.getSeatCapacity()} ");
            sb.Append($"Cargo capacity: {this.getCargoCapacity()} ");
            sb.Append($"Flight range: {this.flightRange} ");
            sb.Append($"Fuel consuption: {this.fuelConsumption} ");
            return sb.ToString();
        }
    }
}

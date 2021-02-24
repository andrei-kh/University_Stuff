using System;

namespace Objects.Exceptions
{
    [System.Serializable]
    public class AircraftCreationException : Exception
    {
        public AircraftCreationException() { }
        public AircraftCreationException(string message) : base(message) { }
    }
    [System.Serializable]
    public class AircraftValueException : Exception
    {
        public AircraftValueException() { }
        public AircraftValueException(string message) : base(message) { }
    }
}
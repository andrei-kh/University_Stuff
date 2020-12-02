using System;

namespace Objects.Exceptions
{
    [System.Serializable]
    public class AirlineContainerException : Exception
    {
        public AirlineContainerException() { }
        public AirlineContainerException(string message) : base(message) { }
    }

}

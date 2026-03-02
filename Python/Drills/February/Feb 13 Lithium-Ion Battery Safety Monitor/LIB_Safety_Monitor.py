
min_opp_temp = 0 # °C
max_opp_temp = 45 # °C
nominal_volt = 3.70 # V
min_safe_volt = 3.00 # V
max_safe_volt = 4.20 # V

def check_battery_status(temp, voltage):

    """Evaluating Temperature Range"""

    if temp < min_opp_temp:
        print("Warning: Temperature below Minimum Operating Temperature")
        print(f"Internal temperature must increase by {min_opp_temp - temp:.2f} °C")

    elif temp > max_opp_temp:
        print("Warning: Temperature above Maximum Operating Temperature")
        print(f"Internal temperature must decrease by {temp - max_opp_temp:.2f} °C")
    
    else:
        print("Temperature is within safe operating conditions.")

    # A future improvement could be to define a safe range and a danger zone to be 95% out of safe range.

    """Evaluating Voltage Range"""

    if voltage < min_safe_volt:
        print("Undervoltage Warning")
        print(f"Please increase voltage by {min_safe_volt - voltage :.2f} V")
    
    elif voltage > max_safe_volt:
        print("Overvoltage Warning")
        print(f"Please decrease voltage by {voltage - max_safe_volt :.2f} V")

    elif voltage == nominal_volt:
        print("Battery is operating at nominal voltage.")

    else:
        print("Voltage is within safe operating conditions.")

    # A future improvement could be to define a safe range and a danger zone to be 95% out of safe range.


def main():
    """Placeholder Text"""
    temperature = float(input("Enter the battery temperature in degrees Celsius: "))
    
    while temperature < -50 or temperature > 100:
        print("Temp Values out of Range")
        temperature = float(input("Enter a temperature in degrees Celcious between -50 °C to 100 °C: "))

    voltage = float(input("Enter the battery voltage in Volts: "))

    while voltage < 0:
        print("Voltage must be greater than cero")
        voltage = float(input("Enter the battery voltage in Volts: "))

    
    check_battery_status(temperature, voltage)


if __name__=="__main__":
    main()

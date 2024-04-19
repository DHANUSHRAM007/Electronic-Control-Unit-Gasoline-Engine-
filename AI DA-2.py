engine_rpm = float(input("Enter Engine RPM: "))
air_mass_flow = float(input("Enter Air Mass Flow Rate (g/s): "))
fuel_mass_flow = float(input("Enter Fuel Mass Flow Rates (g/s): "))
throttle_position = float(input("Enter Throttle Position (%): "))
oxygen_content = float(input("Enter Oxygen Content in Exhaust (%): "))
crank_position = float(input("Enter Crank Position (degrees): "))
cam_position = float(input("Enter Cam Position (degrees): "))
coolant_temp = float(input("Enter Coolant Temperature (C): "))

# Constants
stoichiometric_air_fuel_ratio = 14.7  # Stoichiometric air-fuel ratio for gasoline
wheel_circumference = 2.3 * 3.14     # Assuming wheel diameter of 0.6 m
gear_ratio = 3.5                    # Assuming a gear ratio of 3.5

# Calculations
air_fuel_ratio = air_mass_flow / fuel_mass_flow
lambda_value = air_fuel_ratio / stoichiometric_air_fuel_ratio  # Lambda value (air-fuel ratio relative to stoichiometric)

# Ignition timing calculation
if engine_rpm <= 3000:
    ignition_timing = 10  # degrees BTDC
elif engine_rpm > 3000:
    ignition_timing = 20  # degrees BTDC

# Fuel injection duration calculation
fuel_injection_duration = (fuel_mass_flow / engine_rpm) * 2 / 60000  # milliseconds

# Vehicle speed calculation
vehicle_speed = (crank_position / 360) * wheel_circumference * gear_ratio * (engine_rpm / 60)  # km/h

# Actuate ignition coil and fuel injector
print("Ignition Timing:", ignition_timing, "degrees BTDC")
print("Fuel Injection Duration:", fuel_injection_duration, "ms")

# Additional control logic based on sensor inputs
if lambda_value < 0.95:
    print("Mixture is lean, increasing fuel delivery.")
elif lambda_value > 1.05:
    print("Mixture is rich, decreasing fuel delivery.")

if coolant_temp < 60:
    print("Engine is cold, enriching mixture.")
elif coolant_temp >= 90:
    print("Engine is hot, leaning mixture.")

# Send information to dashboard
dashboard_data = {
    "engine_rpm": engine_rpm,
    "fuel_mass_flow": fuel_mass_flow,
    "vehicle_speed": vehicle_speed
}

print("Dashboard Data:")
for key, value in dashboard_data.items():
    print(f"{key.capitalize()}: {value}")

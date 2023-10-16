# Rui Xu
# Purpose: Create Bike Class for assignment 07

# Import the Bike Class
from bike import Bike

# Instantiate a new Bike object
my_bike = Bike(num_gears=15, num_wheels=2, brake_type="hand brakes")


# Set the gear to 10 using the set_current_gear method
my_bike.set_current_gear(10)

# Show that the gear has been set to 10
print("Current Gear:", my_bike.get_current_gear())

# Pause for user input before attempting to increase the gear
input("Press Enter to continue...")

# Attempt to increase the gear
try:
    for _ in range(10):
        my_bike.increase_gear()
    new_gear = my_bike.get_current_gear()
    if 1 <= new_gear <= 15:
        print("Current Gear:", new_gear)  # Print the current gear value
    else:
        raise ValueError("Gear change resulted in an invalid value, reset to 10")
except ValueError as e:
    print(f"Error: {e}")
    my_bike.set_current_gear(10)  # Reset the gear to 10

# Show the current gear after the attempted increase
print("Current Gear:", my_bike.get_current_gear())
# Pause for user input before attempting to decrease the gear
input("Press Enter to continue...")

# Attempt to decrease the gear below the minimum limit
try:
  for _ in range(20):
      my_bike.decrease_gear()
  new_gear = my_bike.get_current_gear()
  if 1 <= new_gear <= 15:
      print("Current Gear:", new_gear)  # Print the current gear value
  else:
      raise ValueError("Gear change resulted in an invalid value, reset to 10")
except ValueError as e:
  print(f"Error: {e}")
  my_bike.set_current_gear(10)  # Reset the gear to 10

# Show the current gear after the attempted decrease
print("Current Gear:", my_bike.get_current_gear())

# Pause for user input before attempting to set an invalid brake type
input("Press Enter to continue...")

# Attempt to set an invalid brake type
try:
    my_bike.set_brake_type("electric")  # Try to set the brake type to "electric"
except ValueError as e:
    print(f"Error: {e}")

input("Press Enter to continue...")

# An overview of my bike
# Print the current gear (which is retrieved from my bike)
print(f"The gears number of my bike: {my_bike.get_num_gears()}")

# Print the gear number set to 10
print(f"The current Gear number of my bike: {my_bike.get_current_gear()}")

# Print the wheel number (which is retrieved from my bike)
print(f"The wheel number of my bike: {my_bike.get_num_wheels()}")

# Print the brake type (which is retrieved from my bike)
print(f"Brake Type of my bike: {my_bike.get_brake_type()}")

# Increase the gear
my_bike.increase_gear()
# Print the current gear after increasing it
print("Current Gear After Increase:", my_bike.get_current_gear())

# Increase the gear
my_bike.decrease_gear()
# Print the current gear after increasing it
print("Current Gear After Decrease:", my_bike.get_current_gear())





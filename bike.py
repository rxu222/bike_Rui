class Bike:
    def __init__(self, num_gears, num_wheels, brake_type):
        # Initialize the Bike object with the provided number of gears, number of wheels, and brake type.
        if 1 <= num_gears <= 15:
            self.num_gears = num_gears  # Store the number of gears if it's within the valid range.
        else:
            raise ValueError("Number of gears must be between 1 and 15")

        self.current_gear = 1  # Initialize the current gear to 1 by default.

        if num_wheels in (1, 2, 3, 4):
            self.num_wheels = num_wheels  # Store the number of wheels if it's within the valid range.
        else:
            raise ValueError("Number of wheels must be 1, 2, 3, or 4")

        if brake_type in ("hand brakes", "foot brakes"):
            self.brake_type = brake_type  # Store the brake type if it's one of the valid options.
        else:
            raise ValueError("Brake type must be 'hand brakes' or 'foot brakes'")

    def set_num_gears(self, num_gears):
        # Set the number of gears for the Bike object, provided it falls within the valid range.
        if 1 <= num_gears <= 15:
            self.num_gears = num_gears
        else:
            raise ValueError("Number of gears must be between 1 and 15")

    def get_num_gears(self):
        # Retrieve the number of gears of the Bike object.
        return self.num_gears

    def set_current_gear(self, gear):
        # Set the current gear of the Bike object, provided it's within the valid range.
        if 1 <= gear <= self.num_gears:
            self.current_gear = gear
        else:
            raise ValueError("Invalid gear value")

    def get_current_gear(self):
        # Retrieve the current gear of the Bike object.
        return self.current_gear

    def set_num_wheels(self, num_wheels):
        # Set the number of wheels for the Bike object, provided it falls within the valid range.
        if num_wheels in (1, 2, 3, 4):
            self.num_wheels = num_wheels
        else:
            raise ValueError("Number of wheels must be 1, 2, 3, or 4")

    def get_num_wheels(self):
        # Retrieve the number of wheels of the Bike object.
        return self.num_wheels

    def set_brake_type(self, brake_type):
        # Set the brake type for the Bike object, provided it's one of the valid options.
        if brake_type in ("hand brakes", "foot brakes"):
            self.brake_type = brake_type
        else:
            raise ValueError("Brake type must be 'hand brakes' or 'foot brakes'")

    def get_brake_type(self):
        # Retrieve the brake type of the Bike object.
        return self.brake_type

    def reset_gears(self):
        # Reset the current gear of the Bike object to 1.
        self.current_gear = 1

    def increase_gear(self):
        # Increase the current gear of the Bike object, if it's within the maximum limit.
        if self.current_gear < self.num_gears:
            self.current_gear += 1
        else:
            raise ValueError("Cannot increase gear beyond the maximum of 15")

    def decrease_gear(self):
        # Decrease the current gear of the Bike object, if it's above the minimum limit.
        if self.current_gear > 1:
            self.current_gear -= 1
        else:
            raise ValueError("Cannot decrease gear below the minimum of 1")


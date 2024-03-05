# Main program for the sonar control system
# Draws 32 by 32 grid with walls and empty space
# grid points will be 10 cm apart
# Point value will represent probability of wall, 0 - no wall, 100 - wall

# Import necessary libraries
import periscope
import SignalLED as sl
from machine import Pin
from time import sleep

# Define pins for the motor and sonar
motor_pins = [Pin(2, Pin.OUT), Pin(3, Pin.OUT), Pin(4, Pin.OUT), Pin(5, Pin.OUT)]
trigger_pin = Pin(21, Pin.OUT)
echo_pin = Pin(20, Pin.IN)

grid_size = 32		# Size of the grid (in points)
point_distance = 10	# Distance between points in cm

# Create a periscope object
scope = periscope.periscope(motor_pins, trigger_pin, echo_pin)

map_plane = [[0 for i in range(grid_size)] for j in range(grid_size)]

def spawn_car(map_plane, x, y):
    if 0 < x < len(map_plane) - 1 and 0 < y < len(map_plane[0]) - 1:  # Ensure coordinates are within bounds and not blocking walls
        map_plane[x][y] = "S"
        return x, y
    else:
        raise ValueError("Invalid car position. Coordinates must be within the room bounds.")

angle_per_step = 22 # With the gearbox

def main():
	scope.setAngle(0)
	scope.setStepRatio(angle_per_step)
	# print("Check if the periscope is in home position (facing to the front)!")
	print("Map is set to " + str(grid_size) + "x" + str(grid_size) + " grid with " + str(point_distance) + " cm distance between points (" + str(grid_size*point_distance) + "x" + str(grid_size*point_distance) + " cm)")

	while True:
		for iterations in range(1):
			for i in range(0, 360, 5):
				scope.rotate(i)
				sleep(0.1)
				distance = scope.measure()
				print("Angle: ", str(i), " Distance: ", str(distance))
				x,y = scope.getXY(distance)
				x, y = int(x/point_distance), int(y/point_distance)
				if x < grid_size and y < grid_size:
					try:
						map_plane[int(grid_size/2 + x)][int(grid_size/2 + y)] += 1
					except:
						print("Out of range, may be a sensor failure")
		print("Scan finished. Printing map:")
		sl.red()
		spawn_car(map_plane, int(grid_size/2), int(grid_size/2))
		for i in range(grid_size):
			print(str(map_plane[i]))
		sleep(1)


if __name__ == "__main__":
	main()

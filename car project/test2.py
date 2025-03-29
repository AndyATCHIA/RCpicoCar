import time
from servo import Servo

# Create our Servo object, assigning the
# GPIO pin connected the PWM wire of the servo
my_servo = Servo(pin_id=3)


my_servo.write(50)  # Set the Servo to the mid-point (90 is half way between zero and 180 degrees)
time.sleep_ms(1000)  # Wait for 1 second
import socket
import _thread
from time import sleep
import utime
from servo import Servo
import network
import machine
from machine import Pin,PWM,time_pulse_us
 
# Set up the SSID and password for the WiFi network
ssid = 'CPE_R0516_1777'
password = 'P@1ll0t3'
dot = Pin('LED', Pin.OUT)

ENA =Pin(0,Pin.OUT) # Activer le moteur A 
pwm_A = PWM(ENA)
pwm_A.freq(500)

my_servo = Servo(pin_id=3)
my_servo.write(90)  # Set the Servo to the mid-point (90 is half way between zero and 180 degrees)

# Initialize pins for controlling the motor
Motor_A_Forward = Pin(1, Pin.OUT)
Motor_A_Backward = Pin(2, Pin.OUT)

 
# Define functions for moving the motor in different directions
def Forward():
    Motor_A_Forward.value(1)
    Motor_A_Backward.value(0)
    
def Backward():
    Motor_A_Forward.value(0)
    Motor_A_Backward.value(1)
 
def Stop():
    Motor_A_Forward.value(0)
    Motor_A_Backward.value(0)
 
def Left():
    my_servo.write(130)
 
def Right():
    my_servo.write(50)  

    
 
# Stop the motor initially
Stop()
    
def Connect():
    # Connect to the WiFi network
    red = network.WLAN(network.STA_IF)
    red.active(True)
    red.connect(ssid, password)
    while red.isconnected() == False:
        print('connecting ...')
        dot.value(1)
        utime.sleep_ms(500)
        dot.value(0)
        sleep(1)
    ip = red.ifconfig()[0]
    print(f'Connected with IP: {ip}')
    dot.value(1)
    return ip
    
def open_socket(ip):
    # Create a socket for the web server to listen on
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection
 
def pagina_web():
    html = f"""
        <!DOCTYPE html>
        <html>
        <head>
        
        
        </head>
        <body>
         
              <h1 style="text-align: center;">Raspberry Pi Pico W Wireless Car
              </body>
              <h6 style="text-align: center;">DIY Projects Lab
        <center>
        <form action="./Forward">
        <input type="submit" value="Forward" style="background-color: #04AA6D; border-radius: 15px; height:120px; width:120px; border: none; color: white; padding: 16px 24px; margin: 4px 2px"  />
        </form>
        <table><tr>
        <td><form action="./Left">
        <input type="submit" value="Left" style="background-color: #04AA6D; border-radius: 15px; height:120px; width:120px; border: none; color: white; padding: 16px 24px; margin: 4px 2px"/>
        </form></td>
        <td><form action="./Stop">
        <input type="submit" value="Stop" style="background-color: #FF0000; border-radius: 50px; height:120px; width:120px; border: none; color: white; padding: 16px 24px; margin: 4px 2px" />
        </form></td>
        <td><form action="./Right">
        <input type="submit" value="Right" style="background-color: #04AA6D; border-radius: 15px; height:120px; width:120px; border: none; color: white; padding: 16px 24px; margin: 4px 2px"/>
        </form></td>
        </tr></table>
        <form action="./Backward">
        <input type="submit" value="Backward" style="background-color: #04AA6D; border-radius: 15px; height:120px; width:120px; border: none; color: white; padding: 16px 24px; margin: 4px 2px"/>
        </form>
        </body>
        </html>
    """
    return str(html)
def serve(connection):
    while True:
        cliente = connection.accept()[0]
        peticion = cliente.recv(1024)
        peticion = str(peticion)
        try:
            peticion = peticion.split()[1]
        except IndexError:
            pass
        if peticion == '/Forward?':
            Forward()
        elif peticion =='/Left?':
            Left()
        elif peticion =='/Stop?':
            Stop()
        elif peticion =='/Right?':
            Right()
        elif peticion =='/Backward?':
            Backward()
        html = pagina_web()
        cliente.send(html)
        cliente.close()
 
try:
    ip = Connect()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()

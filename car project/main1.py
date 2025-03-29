import _thread
import machine
from servo import Servo
from machine import Pin,PWM,time_pulse_us
from blynklib import Blynk
import utime
import network
import constants


#============ Contrôle Moteurs ==================
#Contrôle Moteur A
ENA =Pin(0,Pin.OUT) # Activer le moteur A 
IN1 =Pin(1,Pin.OUT) 
IN2 =Pin(2, Pin.OUT)

pwm_A = PWM(ENA)
pwm_A.freq(500)


dot = Pin('LED', Pin.OUT)


def connect_to_internet(ssid, password):
    # Pass in string arguments for ssid and password

    # Just making our internet connection
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    # Wait for connect or fail
    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print('waiting for connection...')
        utime.sleep_ms(1000)
    # Handle connection error
    if wlan.status() != 3:
        print(wlan.status())
        raise RuntimeError('network connection failed')
    else:
        print(f"Connected to {constants.INTERNET_NAME} - IP Address : {wlan.ifconfig()[0]} ")
        print(wlan.status())
        status = wlan.ifconfig()        
        dot.value(1)
        utime.sleep_ms(2500)
        dot.value(0)


connect_to_internet(constants.INTERNET_NAME, constants.INTERNET_PASSWORD)
BLYNK = Blynk(constants.BLYNK_AUTH_TOKEN)

#=============================================

class Controls:
    
    def __init__(self):
        pass
    
    def turn_right(self, vitesse):
        
        my_servo.write(65)
        IN1.value(0)
        IN2.value(0)

        pwm_A.duty_u16(int(vitesse * 65535))

        
    def turn_left(self, vitesse):
        
        my_servo.write(125)
        IN1.value(0)
        IN2.value(0)
        pwm_A.duty_u16(int(vitesse * 65535))

        
    def forward(self, vitesse):

        IN1.value(1) 
        IN2.value(0)
        pwm_A.duty_u16(int(vitesse * 65535))

    def reverse(self, vitesse):
        
        IN1.value(0) 
        IN2.value(1)
        pwm_A.duty_u16(int(vitesse * 65535))


    def stop(self, vitesse):
        
        IN1.value(0) 
        IN2.value(0)
        pwm_A.duty_u16(int(vitesse * 65535))

    def brake(self, vitesse):

        
        IN1.value(0) 
        IN2.value(0)
        pwm_A.duty_u16(int(0 * 65535))

control = Controls()

control.stop(0)

#1tour ==> 3610


@BLYNK.on("V0") #virtual pin V0
def v0_write_handler( value): #read the value
    if int(value[0]) == 1:
        control.forward(1) #turn the led on        
    else:
        control.stop(1)    #turn the led off
        
@BLYNK.on("V1") #virtual pin V1
def v1_write_handler(value): #read the value
    if int(value[0]) == 1:
        control.brake(1) #turn the led on        
    else:
        control.stop(1)   #turn the led off
        
@BLYNK.on("V2") #virtual pin V1
def v2_write_handler(value): #read the value
    if int(value[0]) == 1:
        control.reverse(1) #turn the led on        
    else:
        control.stop(1)   #turn the led off

@BLYNK.on("V3") #virtual pin V1
def v3_write_handler(value): #read the value
    if int(value[0]) == 1:
        control.turn_left(1) #turn the led on        
    else:
        control.stop(1)   #turn the led off

@BLYNK.on("V4") #virtual pin V1
def v4_write_handler( value): #read the value
    if int(value[0]) == 1:
        control.turn_right(1) #turn the led on        
    else:
        control.stop(1)  #turn the led off

for i in range(5):
    utime.sleep_ms(100)         
    dot.value(1)        
    utime.sleep_ms(100)          
    dot.value(0)       


while True:
    BLYNK.run()




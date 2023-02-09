import RPi.GPIO as GPIO
from time import sleep

in1 = 24
in2 = 23
in3 = 10
in4 = 11
ena = 25
enb = 9
temp1=1

GPIO.setmode(GPIO.BCM)

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)

GPIO.setup(ena, GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

ma=GPIO.PWM(ena,1000)
mb = GPIO.PWM(enb,1000)

ma.start(25)
mb.start(25)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

while(1):

    x=raw_input()
    
    if x=='r':
        print("run")
        if(temp1==1):
         GPIO.output(in1,GPIO.HIGH)
         GPIO.output(in2,GPIO.LOW)
         GPIO.output(in3,GPIO.HIGH)
         GPIO.output(in4,GPIO.LOW)

         print("forward")
         x='z'
        else:
         GPIO.output(in1,GPIO.LOW)
         GPIO.output(in2,GPIO.HIGH)
         GPIO.output(in3,GPIO.LOW)
         GPIO.output(in4,GPIO.HIGH)

         print("backward")
         x='z'


    elif x=='s':
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)

        x='z'

    elif x=='f':
        print("forward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)

        temp1=1
        x='z'

    elif x=='b':
        print("backward")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)

        temp1=0
        x='z'

    elif x=='l':
        print("low")
        ma.ChangeDutyCycle(25)
        mb.ChangeDutyCycle(25)
        x='z'

    elif x=='m':
        print("medium")
        ma.ChangeDutyCycle(50)
        mb.ChangeDutyCycle(50)
        x='z'

    elif x=='h':
        print("high")
        ma.ChangeDutyCycle(90)
        mb.ChangeDutyCycle(90)
        x='z'

    elif x=='le':
        print("left")
        ma.ChangeDutyCycle(25)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
 
        mb.ChangeDutyCycle(25)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)

        x='z'
     
    elif x=='ri':
        print("right")
        ma.ChangeDutyCycle(25)
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
 
        mb.ChangeDutyCycle(25)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)

        x='z'
 
    elif x=='sp':
        print("spin")
        ma.ChangeDutyCycle(80)
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
 
        mb.ChangeDutyCycle(80)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)

        x='z'
    
    elif x=='e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")


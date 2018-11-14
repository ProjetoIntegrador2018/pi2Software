import time
import wiringpi


DIR = 28
STEP = 29
CW = 1
CCW = 0
SPR = 200
OUTPUT = 1
HIGH = 1
LOW = 0


def motor():
    wiringpi.wiringPiSetup()

    wiringpi.pinMode(DIR, OUTPUT)
    wiringpi.pinMode(STEP, OUTPUT)

    atraso = 1

    wiringpi.digitalWrite(DIR, CCW)

    i = 0
    while (i < 201):
        print('teste')
        wiringpi.digitalWrite(STEP, HIGH)
        wiringpi.delay(atraso)
        wiringpi.digitalWrite(STEP, LOW)
        wiringpi.delay(atraso)
        i += 1

if __name__ == "__main__":
    motor()
import time
from gpio import *

def main():
    # --- HARTA FINALE E PORTAVE ME NUMRA ---
    # Hyrje (Inputs)
    motion_sensor = 0       # D0 - Motion Sensor
    smoke_sensor = 4        # Portë për sensorin e tymit (u ndryshua nga 'A0')
    
    # Dalje (Outputs)
    garage_door = 1         # D1 - Garage Door
    siren = 2               # D2 - Siren
    lcd = 3                 # D3 - LCD
    smart_led = 5           # Portë për LED-in (u ndryshua nga 'A1')

    # --- Konfigurimi i portave ---
    pinMode(motion_sensor, IN)
    pinMode(smoke_sensor, IN)   # Tani funksionon sepse '4' është numër
    pinMode(garage_door, OUT)
    pinMode(siren, OUT)
    pinMode(lcd, OUT)
    pinMode(smart_led, OUT)     # Tani funksionon sepse '5' është numër

    # --- Gjendje fillestare ---
    analogWrite(smart_led, 1023)
    customWrite(lcd, "Statusi:\nVEND I LIRE")
    customWrite(garage_door, "0")
    customWrite(siren, "0")

    while True:
        smoke_value = analogRead(smoke_sensor)
        
        print("Vlera e tymit (0-255):", smoke_value)

        if smoke_value > 70:
            customWrite(lcd, "ALARM:\nTYM I ZBULUAR!")
            customWrite(siren, "1")
            customWrite(garage_door, "1")
            analogWrite(smart_led, 200)
        
        elif digitalRead(motion_sensor) == HIGH:
            customWrite(lcd, "Statusi:\nVEND I ZENE")
            customWrite(garage_door, "1")
            analogWrite(smart_led, 500)
            customWrite(siren, "0")
        
        else:
            customWrite(lcd, "Statusi:\nVEND I LIRE")
            customWrite(garage_door, "0")
            analogWrite(smart_led, 1023)
            customWrite(siren, "0")

        time.sleep(0.5)

if __name__ == "__main__":
    main()

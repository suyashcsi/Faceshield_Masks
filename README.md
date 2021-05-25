# EYANTRA HACKATHON 2021
# Smart Face Shield Masks
## Overview of Project
WHAT WE CREATED ":  WE HAVE CREATED A SMART FACE SHIELD MASK THAT CAN IDENTIFY THE UNUSUAL MOMENT OF YOUR/OTHER HAND NEARBY FACEMASK.
###### HOW IT WORKS": IN THIS PROJECT WE HAVE CREATED A SPECIFIC RANGE WHICH IS CALLED LAKSHAM REKHA. WHENEVER YOUR HAND CROSSES A LAKSHAM REKHA AN ALARM WILL RING AND TO ALERT YOU NOT TO TOUCH YOUR FACE. IF YOU DO SO, WE HAVE ALSO PUT A BACKUP THAT AN ALERT MESSAGE WILL GO ON YOUR MOBILE TO STEP SAFE TOWARDS YOU TO KEEP AWAY FROM CORONAVIRUS AND TELL YOU TO WASH YOUR HAND IMMEDIATELY.
## Hardware Components Used
- Arduino UNO
- ESP8266
- HC-SR04 Sensor
- Buzzer
- LED
- Resistor
- Breadboard
- Jumper Wires
## Software Used
- Arduino IDE
- Linux Terminal 
- Python 3 IDE
- Virtual Host OS
## Other Online Service 
- Telegram
- Mailgun
## Hardware Connections
-  The HC-SR04 Ultrasonic Module has 4 pins, Ground, VCC, Trig and Echo.
-  The Ground and the VCC pins of the module needs to be connected to the Ground and the 5 volts pins on the Arduino Board respectively and the trig and echo pins to any Digital I/O pin on the Arduino Board.
-   The HC-SR04 sensor attach to the Breadboard
-   The Sensor VCC connect to the Arduino Board +5V
-   The Sensor GND connect to the Arduino Board GND
-   The Sensor Trig connect to the Arduino Board Digital I/O 9
-   The Sensor Echo connect to the Arduino Board Digital I/O 10
-   The Buzzer attach to the Breadboard
-   The Buzzer long leg (+) connect to the Arduino Board Digital 11
-   The Buzzer short leg (-) connect to the Arduino Board GND
-   The LED attach to the Breadboard - The Resistor connect to the LED long leg (+)
-   The Resistor other leg (from LED's long leg) connect to the Arduino Board Digital 13
-   The LED short leg (-) connect to the Arduino Board GND
-   Connect ESP8266 GND with Gnd of Arduino UNO and 5V to Arduino
-   Connect RX to TX of Arduino UNO  
-   Connect TX to RX of Arduino UNO
## Software Setup 
  I have used two libraries from arduino IDE which are in-built
-   #include <SoftwareSerial.h>
-   #include <Ultrasonic.h>
#include <SoftwareSerial.h> is used to connect the Bolt Iot device to the arduino Uno and other for HC-SR04 Sensor
## To download these files
- For [Software Serial](https://www.arduino.cc/en/Reference/softwareSerial).
- For [Ultrasonic](https://www.arduino.cc/reference/en/libraries/hcsr04-ultrasonic-sensor/)
## Demonstartion Of Video
[YOUTUBE](https://www.youtube.com/watch?v=njAoky-EAK0)

# THANK YOU



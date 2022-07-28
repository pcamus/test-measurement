## Ground path issue when connecting several USB devices.

In the hardware setup section we have noticed a unexpected behavior :

> Before connecting the logic analyser ground connection, the measured current was 18.6 mA when the LED is off and 20.7 mA when it is on.
> 
> When I connected the ground wire, these values changed a lot.

The displayed current on the USB tester changed when we just put a ground connection between the analyser and the Raspberry Pi Pico. 
When testing, **with the same Pico program**, I noticed an increase in the current ranging from 20 to 80 mA depending of the USB cable in use.

When I inserted an ampermeter instead of the ground wire, I also measured this current. So something goes from one USB1 ground to US2 ground.

If you think about it for a moment, you realize that this is completely normal. Current flows always through the path of least resistance, so if you have two ground connections

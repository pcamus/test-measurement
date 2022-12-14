## Ground path issue when connecting several USB devices.

In the hardware setup section, we have noticed an unexpected behaviour :

> Before connecting the logic analyser ground connection, the measured current was 18.6 mA when the LED is off and 20.7 mA when it is on.
> 
> When I connected the ground wire, these values changed a lot.

The displayed current on the USB tester changed when we just put a ground connection between the analyser and the Raspberry Pi Pico. 
When testing, **with the same Pico program**, I noticed an increase in the current ranging from 20 to 80 mA depending on the USB cable in use.

When I inserted an ammeter instead of the ground wire, I also measured this current. So something goes from USB1 ground connection to USB2 ground connection.

If you think about it for a moment, you realise that this is completely normal. Current flows always through the path of least resistance, so if you have two ground connections coming **from the same source** and you connect them, current will be shared in proportion to the ground resistances of each cable. **It doesn't change what each circuit consumes** (to be precise: a tiny bit) but the way current returns to the source.

The big difference given by our tester comes from the fact that this device doesn't measure the current in the V+ connection but measure it in the ground connection.

The detail of this process is in this pdf : [Return_current_path.pdf](Return_current_path.pdf)

Conclusion: the tester is wrong and can only give a reliable measurement in circuits where no common return ground exists.

- [ ] To do : buy a better tester

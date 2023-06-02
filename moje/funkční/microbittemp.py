from microbit import *
import power
import log


class MCP9808:
    def __init__(self):
        print("Init MCP9808")

    def ReadTemp(self):
        i2c.write(0x18, bytearray([0x05]))  # select ambient temp. register
        sleep(100)  # small pause needed to allow the device to update
        t_amb = i2c.read(0x18, 2)  # read two bytes from the ambient temp. register
        t_hi = (t_amb[0] & 0x0F) << 4  # mask upper 4 bits (alarm settings)
        t_lo = t_amb[1] / 16  # lower 8 bits (LSB)
        if t_amb[0] & 0x10 == 0x10:  # take twos complement for -ve readings
            temp = (t_hi + t_lo) - 256.0
        else:
            temp = t_hi + t_lo
        return temp


device = MCP9808()


def teplota():
    return "%.1f" % round(device.ReadTemp(), 1)


@run_every(min=5)
def log_temperature():
    log.add(temp=teplota())


while True:
    if button_a.is_pressed():
        sleep(100)
        display.scroll(teplota())

    if button_b.is_pressed() and button_a.is_pressed():
        display.show(Image.SQUARE_SMALL)
        sleep(1000)
        display.show(Image.SQUARE)
        if button_a.is_pressed() and button_b.is_pressed():
            log.delete()
            display.show(Image.YES)
            sleep(100)
            display.clear()

    # To go sleep, wake up when button A is pressed, and ensure the
    # function scheduled with run_every still executes in the background
    power.deep_sleep(wake_on=button_a, run_every=True)

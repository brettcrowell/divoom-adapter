import divoom_examples
import divoom_protocol
import divoom_device
import time
import sys

examples = divoom_examples.DivoomExamples()
protocol = divoom_protocol.DivoomAuraBoxProtocol()
device = divoom_device.DivoomDevice(sys.argv[1])

device.connect()

print("firework")
examples.firework(protocol, device)

files = ["images/example.bmp", "images/example2.bmp", "images/example3.bmp", "images/example4.bmp", "images/example5.bmp", "images/example6.bmp", "images/example7.bmp", "images/example8.bmp", "images/example9.bmp"]
print("showing files")
examples.show_files(protocol, device, files)

print("blinking")
examples.blink(protocol, device, "images/example7.bmp")

print("show time")
device.send(protocol.create_time_package())
time.sleep(10)

print("show temperature")
device.send(protocol.create_temp_package())
time.sleep(10)

print("write hello world")
examples.hello_world(protocol, device)
time.sleep(10)

print("scrolling")
examples.scroll_sequence(protocol, device)

print("program firework")
examples.firework_predefined(protocol, device)

device.disconnect()
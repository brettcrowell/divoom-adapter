import divoom_examples
import time
import sys

with divoom_examples.DivoomExamples(sys.argv[1]) as examples:

    print("firework")
    examples.firework()

    files = ["images/example.bmp", "images/example2.bmp", "images/example3.bmp", "images/example4.bmp", "images/example5.bmp", "images/example6.bmp", "images/example7.bmp", "images/example8.bmp", "images/example9.bmp"]
    print("showing files")
    examples.show_files(files)

    print("blinking")
    examples.blink("images/example7.bmp")

    print("show time")
    examples.show_time()
    time.sleep(10)

    print("show temperature")
    examples.show_temperature()
    time.sleep(10)

    print("write hello world")
    examples.hello_world()
    time.sleep(10)

    print("scrolling")
    examples.scroll_sequence()

    print("program firework")
    examples.firework_predefined()
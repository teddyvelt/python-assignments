#test_sensor.py
import hal_pc as hw
import morse_code

print("DOT_MS =", morse_code.DOT_MS, " SAMPLE_MS =", morse_code.SAMPLE_MS)
hw.play("E")
for i in range(12):
    print(i, hw.read_u16())
    hw.sleep_ms(50)
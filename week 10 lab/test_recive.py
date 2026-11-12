import hal_pc as hw
import morse_code

def receive():
    message = ""
    pattern = ""
    dot_reads = morse_code.DOT_MS // morse_code.SAMPLE_MS
    previous_on = None
    count = 0
    reads = 0
    t0 = hw.now_ms()

    while reads < 3000:                      # safety cap
        value = hw.read_u16()
        reads += 1
        light_on = value > 500

        if previous_on is None:
            previous_on = light_on
            count = 1
        elif light_on == previous_on:
            count += 1
        else:
            print("changed to", "ON" if light_on else "OFF", "after", count, "reads")
            if previous_on:
                pattern += "." if count < dot_reads * 2 else "-"
            else:
                if count >= dot_reads * 7:
                    if pattern != "":
                        message += morse_code.decode_pattern(pattern)
                        pattern = ""
                    message += " "
                elif count >= dot_reads * 3:
                    if pattern != "":
                        message += morse_code.decode_pattern(pattern)
                        pattern = ""
            previous_on = light_on
            count = 1

        if not light_on and count >= dot_reads * 8:
            if pattern != "":
                message += morse_code.decode_pattern(pattern)
            break

        hw.sleep_ms(morse_code.SAMPLE_MS)

    print("reads:", reads, " ms:", hw.elapsed_ms(t0))
    return message

hw.play("E")
print("received:", repr(receive()))
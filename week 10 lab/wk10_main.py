# =============================================================================
# main.py  -  STARTER for this week's lab: a Morse SEND / RECEIVE station
#
# What is given to you:
#   - the exception that picks the hardware layer (hal_pico on a Pico / Wokwi,
#     hal_pc on your PC)
#   - a short DEMO that shows how to use the photoresistor
#   - the station loop that asks "send or receive?" each round
#
# What YOU write (this is the lab):
#   - send_message(message)   week 9 you wrote how to send a word, now (week 10)extend to a whole message (add word gaps)
#   - receive()               week 10, read the photoresistor and decode the message
#
# =============================================================================

# NEW in WEEK 10 - replace the hal_pico import and hal_pc imports with this try/except. 
# It will pick the right one for you, and you can run the same code on a Pico or on your PC.
try:
    import hal_pico as hw
except ImportError:
    import hal_pc as hw
 
import morse_code
 
 
def send_message(message):
    words = message.split()

    for w in range(len(words)):
        if w > 0:
            hw.set_led_timed(False, morse_code.WORD_GAP_MS)

        patterns = morse_code.encode_message(words[w])
        for p in range(len(patterns)):
            if p > 0:
                hw.set_led_timed(False, morse_code.LETTER_GAP_MS)

            pattern = patterns[p]
            for s in range(len(pattern)):
                if s > 0:
                    hw.set_led_timed(False, morse_code.SYMBOL_GAP_MS)
                if pattern[s] == ".":
                    hw.set_led_timed(True, morse_code.DOT_MS)
                else:
                    hw.set_led_timed(True, morse_code.DASH_MS)
hw.set_led(False)

def receive():
    message = ""
    pattern = ""
    dot = morse_code.DOT_MS
 
    previous_on = None
    start = 0
    started = False          # becomes True after the first ON pulse
 
    while True:
        light_on = hw.read_u16() > 500
 
        if previous_on is None:
            previous_on = light_on
            start = hw.now_ms()
 
        elif light_on != previous_on:
            length = hw.elapsed_ms(start)      # how long the run that just ended lasted
 
            if previous_on:                    # an ON run ended
                pattern += "." if length < dot * 2 else "-"
                started = True
            elif started:                      # an OFF run ended
                if length >= dot * 5:          # word gap
                    if pattern != "":
                        message += morse_code.decode_pattern(pattern)
                        pattern = ""
                    message += " "
                elif length >= dot * 2:        # letter gap
                    if pattern != "":
                        message += morse_code.decode_pattern(pattern)
                        pattern = ""
 
            previous_on = light_on
            start = hw.now_ms()
 
        # a long dark stretch after the message began means the message is over
        if started and not light_on and hw.elapsed_ms(start) >= dot * 12:
            if pattern != "":
                message += morse_code.decode_pattern(pattern)
            break
 
        hw.sleep_ms(morse_code.SAMPLE_MS)
 
    return message
 
 
# =============================================================================
# THE MORSE CODE STATION
# =============================================================================
print("Board:", hw.board_info())
print("Morse station. Choose a mode each round.")
 
while True:
    mode = input("\n[s]end or [r]eceive? (blank to quit) ")
    mode = mode.strip().lower()
    if mode == "":
        break
 
    if mode == "s" or mode == "send":
        message = input("  message to SEND: ")
        message = message.strip().upper()
        if message != "":
            send_message(message)
 
    elif mode == "r" or mode == "receive":
        message = input("  message being sent to you: ")
        message = message.strip().upper()
        if message != "":
            hw.play(message)
            decoded = receive()
            print("  you received:", decoded)
 
    else:
        print("  please type s or r")
 
print("done.")
 #hi
print("done.")
from lib import *

    

def main():
    ir_detector = threading.Thread(target=check_ir)
    impact_detector = threading.Thread(target=check_impact)
    light_detector = threading.Thread(target=check_light)
    ir_detector.start()
    impact_detector.start()
    impact_detector.join()
    
    time.sleep(MIN_ROCKET_TIME)
    light_detector.start()
    light_detector.join()
    
    ir_detector.join()


if __name__ == "__main__":
    try:
        global stop_detecting
        stop_detecting = False
        main()
    except KeyboardInterrupt:
        stop_detecting = True
        print("\nKeyboard interrupted. Exiting...")
    finally:
        GPIO.output(RELAY_PIN, GPIO.LOW)
        GPIO.output(ROCKET_PIN, GPIO.LOW)
        GPIO.output(LED_PIN, GPIO.LOW)
        GPIO.output(BUZZER_PIN, GPIO.LOW)
        GPIO.cleanup()


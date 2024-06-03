import RPi.GPIO as GPIO
import time
import copy

# Define the GPIO pin connected to the IR sensor
IR_SENSOR_PIN = 17  # You can change this to the GPIO pin you connected to

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_SENSOR_PIN, GPIO.IN)


def print_values():
    start = time.time()
    data = []
    dataline = [0, 0]
    try:
        
        old_sensor_value = GPIO.input(IR_SENSOR_PIN)
        dataline[0] = old_sensor_value

        while True:
            sensor_value = GPIO.input(IR_SENSOR_PIN)
            if sensor_value != old_sensor_value:
                now = time.time()
                dataline[1] = now - start
                data.append(copy.copy(dataline))
                dataline[0] = sensor_value
                old_sensor_value = sensor_value
                start = now


    except KeyboardInterrupt:
        print("Program terminated")

    finally:
        # Clean up GPIO settings before exiting
        
        for line in data:
            print(line)
        GPIO.cleanup()

def print_duty_cycle_digital():
    start = time.time()
    data = []
    dataline = [0, 0]
    off_duration = 0
    on_duration = 0
    try:
        
        value = GPIO.input(IR_SENSOR_PIN)
        old_value = value

        while True:
            value = GPIO.input(IR_SENSOR_PIN)
            if value != old_value:

                duration = time.time() - start
                if value == 1:

                    off_duration = duration
                    total_duration = on_duration + off_duration
                    if total_duration != 0:
                        duty_cycle = round(100 * on_duration / total_duration, 2)
                        if duty_cycle > 1 and duty_cycle < 99:
                            print(f"{duty_cycle}%")

                else:
                    on_duration = duration
                start = time.time()
                old_value = value
            


    except KeyboardInterrupt:
        print("Program terminated")

    finally:
        # Clean up GPIO settings before exiting
        GPIO.cleanup()

def print_IR_digital():
    start = time.time()
    off_duration = 0
    on_duration = 0

    same = 0
    sure_IR = False
    old_sure_IR = True
    IR_detected = False
    old_IR_detected = True

    try:
        
        value = GPIO.input(IR_SENSOR_PIN)
        old_value = value



        while True:
            value = GPIO.input(IR_SENSOR_PIN)
            print(value)
            if value != old_value:
                print("a")
                duration = time.time() - start
                if value == 1:
                    off_duration = duration
                    total_duration = on_duration + off_duration
                    if total_duration != 0:
                        duty_cycle = round(100 * on_duration / total_duration, 2)
                        print("a")
                        if duty_cycle > 1 and duty_cycle < 99:
                            print(duty_cycle)
                            # if duty_cycle < 30:
                            #     IR_detected = True
                            # else:
                            #     IR_detected = False

                            # if IR_detected == old_IR_detected:
                            #     same += 1
                            # else:
                            #     same = 0
                            # old_IR_detected = IR_detected
                            # if same >=2:
                            #     sure_IR = IR_detected

                            
                            # if sure_IR != old_sure_IR:
                            #     print(duty_cycle)
                            #     print(sure_IR)
                            # old_sure_IR = sure_IR
                                



                else:
                    on_duration = duration
                start = time.time()
            old_value = value
            


    except KeyboardInterrupt:
        print("Program terminated")

    finally:
        # Clean up GPIO settings before exiting
        GPIO.cleanup()

# def print_IR():
#     start = time.time()
#     off_duration = 0
#     on_duration = 0
#     old_ir_detected = False
#     same = 0
#     old_sure_ir = False
#     try:
#         value = GPIO.input(IR_SENSOR_PIN)
#         old_value = value
#         while True:
#             value = GPIO.input(IR_SENSOR_PIN)
#             if value != old_value:
#                 duration = time.time() - start

#                 if value == 1:
#                     off_duration = duration
#                     total_duration = on_duration + off_duration

#                     if total_duration != 0:
#                         duty_cycle = 100* on_duration / total_duration
#                         if duty_cycle > 1 and duty_cycle < 99:
#                             ir_detected = (duty_cycle < 30)
#                             if ir_detected == old_ir_detected:
#                                 same += 1
#                             else:
#                                 same = 0

#                             old_ir_detected = ir_detected
#                             if same >= 3:
#                                 is_ir_sure = True

#                             else:
#                                 is_ir_sure = False
#                             sure_ir = ir_detected

#                             if is_ir_sure and old_sure_ir != sure_ir:
                                
#                                 print(sure_ir)
#                             old_sure_ir = sure_ir




                            
#                 else:
#                     on_duration = duration
                    
#             old_value = value
        
        


#     except KeyboardInterrupt:
#         print("Program terminated")

#     finally:
#         # Clean up GPIO settings before exiting
#         GPIO.cleanup()

if __name__ == "__main__":
    print_IR()
import serial
import time

if __name__ == '__main__':
    try:
        ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
        time.sleep(2)  # Allow time for the connection to stabilize
        ser.reset_input_buffer()

        while True:
            try:
                if ser.in_waiting > 0:
                    line = ser.readline().decode('utf-8').rstrip()
                    print(line)
            except serial.SerialException as e:
                print(f"Serial error: {e}")
                break  # Exit the loop if there's a serial error
    except serial.SerialException as e:
        print(f"Failed to open serial port: {e}")

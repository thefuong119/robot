from microbit import *
import machine
i2c = machine.I2C(0, machine.Pin(19), machine.Pin(18))  # Khởi tạo I2C trên chân SDA và SCL
# Địa chỉ I2C của Drone
drone_address = 0x12

def send_command(command):
    i2c.writeto(drone_address, command)  # Gửi tín hiệu điều khiển đến Drone

while True:
    if button_a.is_pressed():
        send_command(b'forward')  # Gửi lệnh điều khiển Drone di chuyển về phía trước
    elif button_b.is_pressed():
        send_command(b'backward')  # Gửi lệnh điều khiển Drone di chuyển về phía sau
    else:
        send_command(b'stop')  # Gửi lệnh dừng Drone
    sleep(100)  # Đợi 100ms
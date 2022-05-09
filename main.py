import machine
import utime
from machine import Pin, I2C
import dht, ssd1306

i2c = I2C(sda=Pin(4), scl=Pin(5))
display = ssd1306.SSD1306_I2C(128, 64, i2c)
sensor = dht.DHT11(Pin(13))

graph_coords_temp = [

]

graph_coords_hum = []
graph_end = 128


def draw():
    sensor.measure()
    temp = sensor.temperature()
    humidity = sensor.humidity()
    print('\nTemperature: '+str(temp)+'\n'+'Humidity: '+str(humidity))

    display.rect(0, 0, 128, 64, 1)
    display.text('Temperature: ' + str(temp), 2, 2, 1)
    display.text('Humidity: ' + str(humidity), 2, 12, 1)
    display.hline(0, 22, 128, 1)

    # temp_scaled = round(64-((temp)))
    # graph_coords_temp.append(temp_scaled)
    # if len(graph_coords_temp) >= 128:
    #     graph_coords_temp.clear()

    hum_scaled = round(64-((humidity*42)/100))
    graph_coords_hum.append(hum_scaled)
    if len(graph_coords_hum) >= 128:
        graph_coords_hum.clear()
    # print(temp_scaled, hum_scaled)


led1 = Pin(2, Pin.OUT)
led2 = Pin(16, Pin.OUT)


display.text('==Zurain Nazir==', 0, 0, 1)
display.text('Grade 9th', 0, 10, 1)
display.text('Daffodil', 0, 20, 1)

display.text('Temperature/', 0, 35, 1)
display.text('Humidity', 0, 45, 1)
display.text('Display', 0, 55, 1)

display.show()
utime.sleep(5)

display.fill(0)

while True:
    led1.on()
    led2.off()
    utime.sleep(1)
    led1.off()
    led2.on()

    last = 0, 0

    display.fill(0)
    draw()
    # for i, v in enumerate(graph_coords_temp):
    #     display.pixel(i, v, 1)

    for i, v in enumerate(graph_coords_hum):
        display.line(i, 63, i, v, 1)
        last = i, v


    display.line(0, last[1], 128, last[1], 1)
    display.line(last[0], 128, last[0], 22, 1)
    display.show()

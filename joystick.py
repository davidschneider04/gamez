import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn


spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5)
mcp = MCP.MCP3008(spi, cs)

left_sel = AnalogIn(mcp, MCP.P0)
left_y = AnalogIn(mcp, MCP.P1)
left_x = AnalogIn(mcp, MCP.P2)
right_sel = AnalogIn(mcp, MCP.P7)
right_y = AnalogIn(mcp, MCP.P5)
right_x = AnalogIn(mcp, MCP.P6)

def get_input(x, y, select):
    select_val = not bool(select.voltage)
    inputs = {'X': x.value, 'Y': y.value, 'SELECT': select_val}
    return inputs

while True:
    left = get_input(left_x, left_y, left_sel)
    right = get_input(right_x, right_y, right_sel)
    print(f'left: {left}')
    print(f'right: {right}')
    print()
    time.sleep(1)

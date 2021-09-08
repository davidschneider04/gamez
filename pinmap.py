import board
import microcontroller

print(dir(board))
board_pins = []

for pin in dir(microcontroller.pin):
    pass
    #print(pin)
    #print(isinstance(getattr(microcontroller.pin, pin), microcontroller.Pin))
    """    pins = []
        for alias in dir(board):
            print(alias)
            if getattr(board, alias) is getattr(microntroller.pin, pin):
                pins.append(f'board.{alias}')
        
        print(pins)
        #if len(pins) > 0:
            #board_pins.append(" ".join(pins))

for pins in sorted(board_pins):
    print(pins)
"""

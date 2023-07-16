from hub import light_matrix, button, port
import motor
from time import sleep


pass_word = "23#125"
input_word = ""
cursor = 1

keypad = {1:'1',2:'2',3:'3',
          4:'4',5:'5',6:'6',
          7:'6',8:'7',9:'9',
          10:'*',11:'0',12:'#'
          }

key_position = {
        1: (0,0), 2: (2,0), 3: (4,0),
        4: (0,1), 5: (2,1), 6: (4,1),
        7: (0,2), 8: (2,2), 9: (4,2),
        10: (0,3), 11: (2,3), 12: (4,3)
}


def input_key(cursor):
    global input_word
    input_word+= keypad[cursor]
    print("input_word= {}".format(input_word))


def display_key():
    for dot in list(key_position.values()):
        x = dot[0]
        y = dot[1]
        light_matrix.set_pixel(x, y, 25)


    # 허브 중앙의 픽셀을 켭니다
    x = key_position[cursor][0]
    y = key_position[cursor][1]
    light_matrix.set_pixel(x, y, 100)

motor.run_to_absolute_position(port.B, 0, 80, direction=motor.SHORTEST_PATH)
display_key()
while True:
    if button.pressed(button.RIGHT) > 0  and cursor < 12:
        cursor += 1
        display_key()

        # 오른쪽 버튼을 뗄때 때까지 기다립니다
        while  button.pressed(button.RIGHT):
            pass

    elif button.pressed(button.LEFT) > 0 and cursor > 0:
        cursor -= 1
        display_key()

        # 왼쪽 버튼을 뗄때 때까지 기다립니다
        while button.pressed(button.LEFT):
            pass

    
    if 45>motor.absolute_position(port.B) > 10:
        input_key(cursor)
        sleep(1)
        motor.run_to_absolute_position(port.B, 0, 40, direction=motor.SHORTEST_PATH)
        while motor.absolute_position(port.B)>2:
            pass
        


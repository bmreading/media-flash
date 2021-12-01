#! /usr/bin/env python

import os

def main():
    print("Please specify the following: \n")

    print("Installation path? [~/.config/conky]")
    install_path = input()
    if install_path == "":
        install_path = "~/.config/conky"
    if install_path[-1] == '/':
        install_path = install_path.rstrip(install_path[-1])
    install_path = f'{install_path}/MediaFlash'

    print("Font to use? [Cantarell]")
    font = input()
    if font == "":
        font = "Cantarell"

    print("Font size to use? [13]")
    font_size = input()
    if font_size == "":
        font_size = "13"

    print("X coordinate placement on screen? [38]")
    x_coord = input()
    if x_coord == "":
        x_coord = "38"

    print("Y coordinate placement on screen? [38]")
    y_coord = input()
    if y_coord == "":
        y_coord = "38"
    
    print("Player name? (Use \"playerctl --list-all\" if unsure)")
    player_name = input()
    empty_string = True
    while empty_string:
        if player_name != "":
            empty_string = False
        else:
            print("Invalid player name. Try again.")
            player_name = input()

    install_path = os.path.expanduser(install_path)
    os.makedirs(install_path)

    rc_template_file = open("./templates/conkyrc")
    rc_template = rc_template_file.read()

    rc = rc_template.replace("INSTALL_PATH", install_path)
    rc = rc.replace("FONT_SIZE", font_size)
    rc = rc.replace("FONT", font)
    rc = rc.replace("X_COORD", x_coord)
    rc = rc.replace("Y_COORD", y_coord)
    rc = rc.replace("PLAYER_NAME", player_name)

    rc_file = open(f"{install_path}/media-flash", "x")
    rc_file.write(rc)
    rc_file.close()

    draw_template_file = open("./templates/draw.lua")
    draw_template = draw_template_file.read()

    draw = draw_template.replace("PLAYER_NAME", player_name)

    draw_file = open(f"{install_path}/draw.lua", "x")
    draw_file.write(draw)
    draw_file.close()

if __name__ == "__main__":
    main()
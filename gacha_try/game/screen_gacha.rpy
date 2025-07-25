
screen gacha_screen():
    tag gacha
    add "pull_menu_bg"
    vbox:
        spacing 20
        align (0.0, 0.5)

        text "Крутани!" size 40

        textbutton "Крутить x1" action Call("gacha_screen_1pull")
        textbutton "Крутить x10" action Call("gacha_screen_10pull")

        textbutton "Выход" action Return()

label gacha_screen_1pull:
    $ prizes = pull_gacha(1)

    python:
        renpy.say(None, f"Ты получил:")
        for prize in prizes:
            renpy.show(prize["splash"])
            renpy.pause(1.0)
            renpy.hide(prize["splash"])
    call screen gacha_screen
    return


label gacha_screen_10pull:
    $ prizes = pull_gacha(10)

    python:
        renpy.say(None, f"Ты получил :")
        for prize in prizes:
            renpy.show(prize["splash"])
            renpy.pause(1.0)
            renpy.hide(prize["splash"])
    call screen gacha_screen
    return

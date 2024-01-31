def on_button_pressed_a():
    basic.show_string("Doveridge")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    music.play(music.builtin_playable_sound_effect(soundExpression.hello),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_string("is great!")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    music.play(music.create_sound_expression(WaveShape.SINE,
            5000,
            0,
            255,
            0,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.UNTIL_DONE)
    basic.show_string("Ouch!")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_touched():
    basic.show_icon(IconNames.GHOST)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def on_logo_released():
    basic.clear_screen()
input.on_logo_event(TouchButtonEvent.RELEASED, on_logo_released)

basic.show_string("Hi!")

def on_forever():
    if input.sound_level() > 150:
        basic.show_string("Shhhh!")
basic.forever(on_forever)

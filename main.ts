input.onButtonPressed(Button.A, function () {
    basic.showString("Doveridge")
})
input.onButtonPressed(Button.AB, function () {
    music.play(music.builtinPlayableSoundEffect(soundExpression.giggle), music.PlaybackMode.UntilDone)
})
input.onButtonPressed(Button.B, function () {
    basic.showString("is great!")
})
input.onGesture(Gesture.Shake, function () {
    music.play(music.createSoundExpression(WaveShape.Sine, 5000, 0, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
    basic.showString("Ouch!")
})
input.onLogoEvent(TouchButtonEvent.Touched, function () {
    basic.showIcon(IconNames.Ghost)
})
input.onLogoEvent(TouchButtonEvent.Released, function () {
    basic.clearScreen()
})
basic.showString("Hello")
music.play(music.builtinPlayableSoundEffect(soundExpression.hello), music.PlaybackMode.UntilDone)
basic.forever(function () {
    if (input.soundLevel() > 150) {
        basic.showString("Shhhh!")
    }
})

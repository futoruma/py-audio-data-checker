import PySimpleGUI as sg
import wave

layout = [
    [sg.Text("", key="-TEXT-")],
    [sg.Button("Open", expand_x=True)],
    [sg.Canvas(key="-CANVAS-")]
]

window = sg.Window("Audio Data Checker", layout)

while True:
    event, values = window.read(timeout=100)
    if event == sg.WIN_CLOSED:
        break

    if event == "Open":
        file_path = sg.popup_get_file("open", no_window=True)
        if file_path:
            with wave.open(file_path, "r") as file:
                file_framerate = file.getframerate()
                file_nframes = file.getnframes()
                file_length = round(file_nframes / file_framerate, 2)

            window["-TEXT-"].update(
                f"Sampling frequency: {file_framerate} \nNumber of audio frames: {file_nframes} \nLength: {file_length} seconds")

window.close()
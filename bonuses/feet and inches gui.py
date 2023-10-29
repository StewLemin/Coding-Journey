import PySimpleGUI as sg
from feet_and_inches_convertor import convert


label1 = sg.Text("Enter feet")
label2 = sg.Text("Enter inches")

input_bar1 = sg.Input(key="feet")
input_bar2 = sg.Input(key="inches")
button = sg.Button("Convert")
output_label = sg.Text("",key="output")
window = sg.Window("Convertor", layout=[[label1, input_bar1], [label2, input_bar2], [button,output_label]])

while True:
    event, values = window.read()
    inches = float(values["inches"])
    feet = float(values["feet"])

    result = convert(feet, inches)
    window["output"].update(value=f"{result}m", text_color="white")

window.close()
import getCoordinates
import extractText
import createWindow
import tranlateText
import tkinter as tk
import test2


"""if __name__ == "__main__":
    logger = getCoordinates.CoordinateLogger()
    print("select area.")
    logger.start()

    if hasattr(logger, 'coordinates'):
        coordinates = logger.coordinates['start'] + logger.coordinates['end']

    print(coordinates)
    text = extractText.extract_text(coordinates)
    translated_text = tranlateText.translate(text)

    outputText.output_text(translated_text)"""
"""def update_text():
    logger.start()

    if hasattr(logger, 'coordinates'):
        coordinates = logger.coordinates['start'] + logger.coordinates['end']

    print(coordinates)
    text = extractText.extract_text(coordinates)
    translated_text = tranlateText.translate(text)

    return tranlateText"""


def main():
    root = tk.Tk()
    root.title("Translater")
    root.geometry("400x400+1520+580")
    root.attributes("-alpha",0.7)
    root.attributes("-topmost",True)
    app = test2.App(master=root)
    
    app.mainloop()

def translate():
    logger = getCoordinates.CoordinateLogger()
    logger.start()
    if hasattr(logger, 'coordinates'):
        coordinates = logger.coordinates['start'] + logger.coordinates['end']

    print(coordinates)
    plane_text = extractText.extract_text(coordinates)
    translated_text = tranlateText.translate(plane_text)
    print(f"planeText{translated_text}")
    del logger
    print("trText" + translated_text.text.replace("：","。").replace("。","。\n"))
    return translated_text.text.replace("：","。").replace("。","。\n").replace(" ","")



if __name__ == "__main__":
    main()

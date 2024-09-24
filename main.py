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

logger = getCoordinates.CoordinateLogger()

def main():
    root = tk.Tk()
    root.title("test")
    root.geometry("400x400+1520+580")
    root.attributes("-alpha",0.7)
    root.attributes("-topmost",True)
    app = test2.App(master=root)
    
    app.mainloop()

def translate():
    
    logger.start()
    if hasattr(logger, 'coordinates'):
        coordinates = logger.coordinates['start'] + logger.coordinates['end']

    print(coordinates)
    text = extractText.extract_text(coordinates)
    translated_text = tranlateText.translate(text)

    return translated_text



if __name__ == "__main__":
    main()

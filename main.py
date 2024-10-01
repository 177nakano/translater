import getCoordinates
import extractText
import tranlateText
import tkinter as tk
import createWindow
import elaborationText


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
    app = createWindow.App(master=root)
    
    app.mainloop()

def translate():
    global plane_text
    logger = getCoordinates.CoordinateLogger()
    logger.start()
    if hasattr(logger, 'coordinates'):
        coordinates = logger.coordinates['start'] + logger.coordinates['end']

    print(coordinates)
    plane_text = extractText.extract_text(coordinates).replace(";",",").replace("_"," ").replace(":",".")
    #print(f"plane_text : {plane_text}")
    translated_text = tranlateText.translate(plane_text)
    #print(f"translated_text : {translated_text}")
    del logger
    return translated_text

def elaboration():
    try:
        print(plane_text)
        elaborated_text = elaborationText.elaboration(
            plane_text)

        translated_text = tranlateText.translate(elaborated_text)
        return  translated_text
    except NameError:
        return "翻訳済みのテキストがないため、再生成ができません。"

if __name__ == "__main__":
    main()

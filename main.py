import getCoordinates
import extractText
import outputText

if __name__ == "__main__":
    logger = getCoordinates.CoordinateLogger()
    print("select area.")
    logger.start()
    coordinates = []
    if hasattr(logger, 'coordinates'):#左上右下
        """coordinates = {"left" : logger.coordinates["start"][0],
                       "top" : logger.coordinates["start"][1],
                       "right" : logger.coordinates["end"][0],
                       "bottom" : logger.coordinates["end"][1]}"""
        coordinates = logger.coordinates['start'] + logger.coordinates['end']

    text = extractText.extract_text(coordinates)
    print(f"text : {text}")

    outputText.output_text(text)
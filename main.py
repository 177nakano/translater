import getCoordinates
import extractText
import outputText
import tranlateText

if __name__ == "__main__":
    logger = getCoordinates.CoordinateLogger()
    print("select area.")
    logger.start()
    coordinates = []
    if hasattr(logger, 'coordinates'):

        coordinates = logger.coordinates['start'] + logger.coordinates['end']

    text = extractText.extract_text(coordinates)
    translated_text = tranlateText.translate(text)

    outputText.output_text(translated_text)
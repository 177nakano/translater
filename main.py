import lisntener


if __name__ == "__main__":
    logger = lisntener.CoordinateLogger()
    print("Click and drag to select area. Press ESC to exit.")
    logger.start()
    coordinate = []
    if hasattr(logger, 'coordinates'):
        coordinate = [logger.coordinates['start'],logger.coordinates['end']]

    print(coordinate)

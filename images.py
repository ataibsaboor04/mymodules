import pyautogui as pag


def isImageOnScreen(image, path="E:/Python Programs/Automation/BrowserAutomation/images", extension='.png'):
    """
    Find specified image on screen.
    Return True if the image is on screen else False.
    """

    location = pag.locateCenterOnScreen(path+"/"+image+extension, confidence=0.9)
    if location is None:
        return False
    return True


def imageName(image):
    """
    Extract the image name.
    """
    for c in image:
        if c.isnumeric():
            image = image.replace(c, '')
    image = image.replace('my', '')
    return image.replace('_', ' ')


def clickImage(image, path="E:/Python Programs/Automation/BrowserAutomation/images", extension='.png'):
    """
    Find specified image and click on it
    """
    if isImageOnScreen(image, path, extension):
        x, y = pag.locateCenterOnScreen(path+"/"+image+extension, confidence=0.9)
        pag.moveTo(x, y, 0.5)
        pag.click()


def isAnyImageOnScreen(image, number_of_images=2, path="E:/Python Programs/Automation/BrowserAutomation/images", extension='.png'):
    """
    Find an image in a number of images.
    Return True of any of the specified images are found else False
    """
    if type(image) is str:
        for i in range(1, number_of_images+1):
            if isImageOnScreen(image+str(i), path, extension):
                return True
    elif type(image) is list:
        for img in image:
            if isImageOnScreen(img, path, extension):
                return True
    return False


def clickAnyImage(image, number_of_images=2, path="E:/Python Programs/Automation/BrowserAutomation/images", extension='.png'):
    """
    Find any of specified images and click on it
    """
    if isAnyImageOnScreen(image, number_of_images+1, path, extension):
        if type(image) is str:
            for i in range(1, number_of_images+1):
                if isImageOnScreen(image+str(i), path, extension):
                    clickImage(image+str(i), path, extension)
                    return

        elif type(image) is list:
            for img in image:
                if isImageOnScreen(img, path, extension):
                    clickImage(img, path, extension)


def findImageAndClick(image, path="E:/Python Programs/Automation/BrowserAutomation/images", extension='.png'):
    """
    Find specified image till found and click on it.
    """
    while True:
        if isImageOnScreen(image, path, extension):
            clickImage(image, path, extension)
            return


def findAnyImageAndClick(image, number_of_images=2, path="E:/Python Programs/Automation/BrowserAutomation/images", extension='.png'):
    """
    Find any of specified images till found and click on it.
    """
    while True:
        if isAnyImageOnScreen(image, path, extension):
            clickAnyImage(image, path, extension)
            return

import cv2 


def main(img):
    image = cv2.imread(img)
    #cv2.imshow('image',image)

    #crop image
    croped_image = image[:, :600]
    cv2.imshow('croped_image', croped_image)

    #resized image
    resized_image = cv2.resize(image, (600, 500))
    cv2.imshow('resized_image', resized_image)

    grayscaled = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('grayscale image', grayscaled)

    #image size
    print(image.shape)
    
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main('C:\\Users\\lette\\OneDrive\\Desktop\\onceagain\\9376.jpg')
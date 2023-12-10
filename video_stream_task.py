import cv2 as cv

vd = cv.VideoCapture(0)

show_gray = False
show_hsv = False
show_original = False

while True:
    ret, frame = vd.read()

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

    elif cv.waitKey(1) & 0xFF == ord('h'):
        show_hsv = not show_hsv
        show_gray = False
        show_original = False

    elif cv.waitKey(1) & 0xFF == ord('g'):
        show_gray = not show_gray
        show_hsv = False
        show_original = False

    elif cv.waitKey(1) & 0xFF == ord('o'):
        show_original = not show_original
        show_gray = False
        show_hsv = False

    elif cv.waitKey(1) & 0xFF == ord('s'):

        if show_hsv:
            cv.imwrite('saved_frame.png', vdhsv)
            print('Frame saved as saved_frame.png')
        elif show_gray:
            cv.imwrite('saved_frame.png', vdgray)
            print('Frame saved as saved_frame.png')
        else:
            cv.imwrite('saved_frame.png', frame)
            print('Frame saved as saved_frame.png')

    if show_original:
        cv.imshow('Video', frame)

    elif show_hsv:
        vdhsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        cv.imshow('Video', vdhsv)

    elif show_gray:
        vdgray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('Video', vdgray)

    else:
        cv.imshow('Video', frame)

# Release the video capture and close all windows
vd.release()
cv.destroyAllWindows()

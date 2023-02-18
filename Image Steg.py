import cv2
import time
def encrypt(binary):
    imgfile = input("Input the file name you would like to encode. (Only accepts .png. Do not include extension. Must be same directory as file)") #ask user to encode
    try:
        img = cv2.imread("{}.png".format(imgfile), cv2.IMREAD_COLOR)           #load file to encode
    except:
        print("Invalid Input Exiting")
        time.sleep(2.5)
        exit()
    #print(img[1][1])
    H = int(0)
    Count = int(0)             #varible setup
    End = False
    for i, row in enumerate(img):         #get pixel values by iterating in a cross pattern
        for j, pixel in enumerate(img):
            if (i == j or i + j == img.shape[0]):
                for i in range(len(binary)):         #loop for each char in the encoding sentence
                    binary1 = binary[:3]       #get the first 3 char of the encoded binary message
                    binary = binary[3:]        #remove the first 3 chars from the encoded binary message
                    r, g, b = img[i][j]      #get RGB for the specfic pixel location
                    binary1 = list(binary1)
                    #print(r)
                    #print(g)            #debuging prints
                    #print(b)
                    #print(binary1)
                    while H != 3 and End == False:        #ensuring r g b iteration
                        try:
                            V = (binary1[0])          #ensuring list length (8bits dosnt fit in 3)
                        except:
                            End = True
                            H = 3
                        if H == 0 and End == False:
                            if (binary1[H] == '0' and r % 2 != 0):
                                r = r - 1                      #change rgb value to corraspond to the binary odd or even
                                H = H + 1         #adding to pixel count
                                Count = Count + 1         #adding to master overall count
                                #print("after {}".format(r))
                            elif (binary1[H] == '1' and r % 2 == 0):
                                if (r != 0):
                                    r = r - 1                     #change rgb value to corraspond to the binary odd or even
                                    H = H + 1        #adding to pixel count
                                    Count = Count + 1         #adding to master overall count
                                    #print("after {}".format(r))
                                else:
                                    r = r + 1                     #change rgb value to corraspond to the binary odd or even
                                    H = H + 1        #adding to pixel count
                                    Count = Count + 1         #adding to master overall count
                                    #print("after {}".format(r))
                            else:
                                H = H + 1        #adding to pixel count
                                Count = Count + 1         #adding to master overall count
                                try:
                                    V = (binary1[1])        #ensuring list length (8bits dosnt fit in 3)
                                except:
                                    End = True
                        elif H == 1 and End == False:
                            try:
                                V = (binary1[1])            #ensuring list length (8bits dosnt fit in 3)
                            except:
                                End = True
                                break
                            if (binary1[H] == '0' and g % 2 != 0):
                                g = g - 1                     #change rgb value to corraspond to the binary odd or even
                                H = H + 1        #adding to pixel count
                                Count = Count + 1         #adding to master overall count
                                #print("after {}".format(g))
                            elif (binary1[H] == '1' and g % 2 == 0):
                                if (g != 0):
                                    g = g - 1                     #change rgb value to corraspond to the binary odd or even
                                    H = H + 1        #adding to pixel count
                                    Count = Count + 1         #adding to master overall count
                                    #print("after {}".format(g))
                                else:
                                    g = g + 1                     #change rgb value to corraspond to the binary odd or even
                                    H = H + 1        #adding to pixel count
                                    Count = Count + 1         #adding to master overall count
                                    #print("after {}".format(g))
                            else:
                                H = H + 1        #adding to pixel count
                                Count = Count + 1         #adding to master overall count
                        elif H == 2 and End == False:
                            try:
                                V = (binary1[2])           #ensuring list length (8bits dosnt fit in 3)
                            except:
                                End = True
                                break

                            if (binary1[H] == '0' and b % 2 != 0):
                                b = b - 1                     #change rgb value to corraspond to the binary odd or even
                                H = H + 1        #adding to pixel count
                                Count = Count + 1         #adding to master overall count
                                #print("after {}".format(b))
                            elif (binary1[H] == '1' and b % 2 == 0):
                                if (b != 0):
                                    b = b - 1                     #change rgb value to corraspond to the binary odd or even
                                    H = H + 1        #adding to pixel count
                                    Count = Count + 1         #adding to master overall count
                                   # print("after {}".format(b))
                                else:
                                    b = b + 1                     #change rgb value to corraspond to the binary odd or even
                                    H = H + 1        #adding to pixel count
                                    Count = Count + 1         #adding to master overall count
                                   # print("after {}".format(b))
                            else:
                                H = H + 1        #adding to pixel count
                                Count = Count + 1          #adding to master overall count
                    H = 0
                    #print("{} {} {} Being Wrote to {}".format(r, g, b, img[i][j]))    Debugging String to ensure the pixels are being edited correctly
                    img[i][j] = [r, g, b]             #Setting the edited rgb values to the orginal pixel location
                    #print("{} {} {} Being Wrote to {}".format(r,g,b,img[i][j]))       Debugging String to ensure the pixels are being edited correctly
                    if End == True:
                        print("Decoding Concluded")
                        print("Your Key is {}. THIS IS REQUIRED TO DECRYPT".format(Count))  # Supplying end user with the key
                        cv2.imwrite("{}_encoded.png".format(imgfile), img)           #Creating the encoding image file
                        print("The encoded image is {}_encoded.png and is saved in the same directory as this python file".format(imgfile))
                        return Count



def decrypt(Count):
    H = int(0)
    Key = int(0)         #varible setup
    decoded = str("")
    imgfile = input("Input the file name you would like to decode. (Only accepts .png. Do not include extension. Must be same directory as file)")      #ask user to point to file to decode
    try:
        img = cv2.imread("{}.png".format(imgfile), cv2.IMREAD_COLOR)   #Open image file
    except:
        print("Invalid Input Exiting")
        time.sleep(2.5)
        exit()
    for i, row in enumerate(img):       #get pixel values by iterating in a cross pattern
        for j, pixel in enumerate(img):
            if (i == j or i + j == img.shape[0]):
                for i in range(Count):     #loop for each char in the encoding sentence
                    r, g, b = img[i][j]       #get RGB for the specfic pixel location
                    if Count == Key:
                        return decoded
                    while H != 3:      #ensuring r g b iteration
                        if H == 0:
                            if r % 2 == 0:           #if r even
                                A = 0          #setting binary bit to 0 or 1 depending if r g b is odd or even
                                H = H + 1         #adding to pixel count
                                Key = Key + 1         #adding to key count
                                if Count == Key:
                                    decoded = decoded + str(A)#add the extracted binary translation to the final decoded string
                                    return decoded
                            else:
                                A = 1          #setting binary bit to 0 or 1 depending if r g b is odd or even
                                H = H + 1         #adding to pixel count
                                Key = Key + 1         #adding to key count
                                if Count == Key:
                                    decoded = decoded + str(A)#add the extracted binary translation to the final decoded string
                                    return decoded
                        elif H == 1:
                            if g % 2 == 0:           #if g even
                                B = 0          #setting binary bit to 0 or 1 depending if r g b is odd or even
                                H = H + 1         #adding to pixel count
                                Key = Key + 1        #adding to key count
                                if Count == Key:
                                    decoded = decoded + str(A)#add the extracted binary translation to the final decoded string
                                    decoded = decoded + str(B)
                                    return decoded
                            else:
                                B = 1          #setting binary bit to 0 or 1 depending if r g b is odd or even
                                H = H + 1         #adding to pixel count
                                Key = Key + 1         #adding to key count
                                if Count == Key:
                                    decoded = decoded + str(A)#add the extracted binary translation to the final decoded string
                                    decoded = decoded + str(B)
                                    return decoded
                        elif H == 2:
                            if b % 2 == 0:           #if b even
                                C = 0          #setting binary bit to 0 or 1 depending if r g b is odd or even
                                H = H + 1         #adding to pixel count
                                Key = Key + 1         #adding to key count
                                if Count == Key:
                                    decoded = decoded + str(A)
                                    decoded = decoded + str(B)#add the extracted binary translation to the final decoded string
                                    decoded = decoded + str(C)
                                    return decoded
                            else:
                                C = 1          #setting binary bit to 0 or 1 depending if r g b is odd or even
                                H = H + 1         #adding to pixel count
                                Key = Key + 1         #adding to key count
                                if Count == Key:
                                    decoded = decoded + str(A)
                                    decoded = decoded + str(B)#add the extracted binary translation to the final decoded string
                                    decoded = decoded + str(C)
                                    return decoded
                    H = 0

                    decoded = decoded + str(A)
                    decoded = decoded + str(B)         #add the extracted binary translation to the final decoded string
                    decoded = decoded + str(C)


def process():
    z = str("")       #varible setup
    word = input("Sentence to Encode (for numbers type them out for example one instead of 1)")           #ask user for sentance to encode
    word = word.split()      #split into list for each word
    for i in word:        #for each word in the potential sentance inputted run the process for each word
        temp = str(i)
        z = z + ''.join(format(ord(x), 'b') for x in temp)       #turn each char into binary and ammend
    #print(z)          code to debug correct binary output value
    return(z)

def bin_string(binary):                                         #https://stackoverflow.com/questions/29102121/how-to-convert-a-word-in-string-to-binary
    bingen = (binary[i:i+7] for i in range(0, len(binary), 7))
    return ''.join(chr(eval('0b'+n)) for n in bingen)


def Start():
    print("""
                                                                                                                           
  ###                                       ###    #                                                      #            
   #                                       #   #   #                                                      #            
   #    ## #    ###    ## #   ###          #      ####    ###   # ##    ###    ## #  # ##    ###   # ##   # ##   #   # 
   #    # # #      #  #  #   #   #          ###    #     #   #  ##  #  #   #  #  #   ##  #      #  ##  #  ##  #  #   # 
   #    # # #   ####   ##    #####             #   #     #####  #   #  #   #   ##    #       ####  ##  #  #   #  #  ## 
   #    # # #  #   #  #      #             #   #   #  #  #      #   #  #   #  #      #      #   #  # ##   #   #   ## # 
  ###   #   #   ####   ###    ###           ###     ##    ###   #   #   ###    ###   #       ####  #      #   #      # 
                      #   #                                                   #   #                #             #   # 
                       ###                                                     ###                 #              ###  
    --------------------------------------------by peel1--------------------------------------------------------------
    
    """)    #banner
    idiot = False
    while idiot == False:
        choice = input("Input 0 for encoding and 1 for decoding")        #user choice encoding or decoding
        if choice == str(0):
            encoded = process()          #get encoded text
            encrypt(encoded)             #encode image
        elif choice == str(1):
            Count = int(input("Input the key provided when encoding"))           #get key for decoding
            decoded = decrypt(Count)                  #decode image
            print("The text is: {}".format(bin_string(decoded)))   #show user the decoded text
        else:
            idiot = True          #if 0 or 1 are not inputed
    print("Invalid input restart program")     #if 0 or 1 are not inputed 
    time.sleep(2.5)
    exit()

#encoded = process()
#Count = encrypt(encoded)
#decoded = decrypt(Count)                      #Faster debug alternative running method
#print("Decoded {}".format(decoded))
#print("the text is {}".format(bin_string(decoded)))


Start()      #script start
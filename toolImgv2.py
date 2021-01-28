from PIL import Image, ImageDraw, ImageFont
import os 
  
def main(): 
    # path of the folder containing the raw images 
    inPath ="C:\\Users\\pok\\Downloads\\MissingPic"
  
    # path of the folder that will contain the modified image 
    outPath ="C:\\Users\\pok\\Downloads\\MissingPicNum"
  
    i = 1
    for imagePath in os.listdir(inPath): 
        # imagePath contains name of the image  
        inputPath = os.path.join(inPath, imagePath) 
  
        # inputPath contains the full directory name 
        image = Image.open(inputPath)
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf", 200)
 
        # starting position of the message
        (x, y) = (50, 50)
        message = str(i)
        color = 'rgb(1, 1, 1)' # black color
 
        # draw the message on the background
 
        draw.text((x, y), message, fill=color, font=font)        
  
        fullOutPath = os.path.join(outPath, imagePath) 
        # fullOutPath contains the path of the output 
        # image that needs to be generated 
        image.save(fullOutPath) 
  
        print(fullOutPath) 

        i = i+1
  
# Driver Function 
if __name__ == '__main__': 
    main() 
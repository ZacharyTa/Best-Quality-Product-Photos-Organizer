import os
from pathlib import Path

# import timeit
# start = timeit.default_timer()

def RecursivelyListImages(folder, folderSize, productList):
  if os.path.isdir(folder) == False:
    if Product.itemExist(CleanImageName(folder)): productList[Product.getItemIndex(CleanImageName(folder))].addImage(os.path.basename(folder), os.path.getsize(folder))
    else: productList.append(Product(CleanImageName(folder), os.path.basename(folder), os.path.getsize(folder)))
  else:
    with os.scandir(folder) as folders:
      for folderDir in folders:
        RecursivelyListImages(folderDir,len([name for name in os.listdir('.') if os.path.isfile(folderDir)]), productList)

def CleanImageName(imgName):
  #Grab file name from path
  newImgName = Path(imgName).stem
  
  #remove everything after spaces ("CT28 White" -> "CT28")
  newImgName = newImgName.rsplit(" ")[0]
  
  #remove "-1", "-2"..."-9" if its an extra picture
  partitionImgNames = newImgName.rsplit("-")
  if len(partitionImgNames) > 1:
    if partitionImgNames[-1].isdigit():
      if int(partitionImgNames[-1]) >= 1 and int(partitionImgNames[-1]) <= 9:
        partitionImgNames.pop()
    return '-'.join(partitionImgNames)
  else: return newImgName

class Product:
  #Dictionary {Product Name(Clean): productList[Index]}
  names = {}
  def __init__(self, name, image, imagesize):
      Product.names[name] = len(Product.names)
      self.name = name
      self.images = [image]
      self.imagesizes = [imagesize]

  def addImage(self, image, imagesize):
      self.images.append(image)
      self.imagesizes.append(imagesize)

  def printProduct(self):
    print(self.name)
    size = len(self.images)
    print("     IMAGES     ")
    for index in range(size):
      print("[" + self.images[index] + "_____" + str(self.imagesizes[index]) + "]")
    print("                ")

  def itemExist(itemName): 
    try:
        if Product.names[itemName]: return True
    except KeyError:
        return False
  
  def getItemIndex(itemName): return Product.names.get(itemName)
  def getNames(): return Product.names.keys()
  def getNumOfProducts(): return len(Product.names)

path = 'G:ALL PHOTOS/Office'
productList = []
RecursivelyListImages(path, 13, productList)

for product in productList:
  product.printProduct()
  
print("done")

# stop = timeit.default_timer()
# print('Time: ', stop - start)  
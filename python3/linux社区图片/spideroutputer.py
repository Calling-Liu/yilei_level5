class SpiderOutputer(object):
    def outputer(self, img, times):
        for i in range(times):
            with open("{}.jpg".format(i),"wb") as f:
                f.write(img[i].content)
        print("successful!")

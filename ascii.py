import cv2

print("WWWWWWWWWWWWWWWWWWWWWWWWWWUUUUUUUUUUUUUUUWWWWWWWWW")
print("WWWWWWWWU^^^UY^WWWWWWWWWWWUUUUUUUUUWWWUUUUWWWWWWWW")
print("WWWWWWW^`^^UUY^^^WWWWWWWWWWUUUUUUWUUUWWWUWWWWWWWWW")
print("WWWWWW^```UYY^^^^^WWWWWWWWWWUUUUUUWWWWWWUUWWWWWWWW")
print("WWWWW^```YYY^^^^^^YUWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
print("WWWWU^`^^UY^^Y^^^YYUWWWWWWWWWWWWUWWWWWWWWWWWWWWWWW")
print("WWWWY``^^U^YUYUWY^^UUWWWWWWWWUUUUUWWWUWWWWWWWWWWWW")
print("WWWW^`^^`Y^U^YYYY^^YUWWWWWWWWUUUUWWWWWWWWWWWWWWWWW")
print("WWWWU``^UY^^Y^YYYU^YWWWWWWWWWWWUWWWWWWWWWWWWWWWWWW")
print("WWWWY^`^WYYY^YYYUY^YUWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
print("WWWUY``^YWYYYYYUU^^YYWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
print("WWWW^```YYUUYYYUYYYYYUWWWWWWWWWWWWWWWWUUUUUWWWWWWW")
print("WWWW``^^^^^YYUUYUYUYYUWWWWWWWWWWWWWWWWWWUUUUUWWWWW")
print("WWWW^`^^^^^^^^^YYYYU^^UWWWWWWWWWWWWWWWWWWUUUUWUWWW")
print("WWWWY^^^^^^^^^^^^^^^``^^^^`WWUUUWWWWWWWWWWWWWWWWWW")
print("WWWWY^^^^^^^^^^^^^^^^`^^^^^^^^^^YUUWWWWWWWWWWUWUWW")
print("WWWW^^^^^^^^^^^^^````^^^^^^^^^Y^^^^WWWWWWWWWWWWWWW")
print("WWWU^^^^^Y`^Y^^`^````````^^^^^^^^^^^YWWWWWWWWWWWWW")
print("WWWU^^^YY^`^^^^^^^^``````^^^^^^Y^^^^^YWWWWWWWWWWWW")
print("WWWU^^^Y^^^^^^^^^^`^``````^^^YYY^^^^^YUUWWWWWWWWWW")
print("WWWY^^^^^^^Y^^^^^^^^````^^^YYYUUY^^^YYUWUWWWWWWWWW")
print("WWWY^^Y^Y^^U^^^^^^^^^^^^^^^YYUUUYYYYYUUUUWWWWWWWWW")
print("WWWY^^^^Y^YWY^^^^^^^^^^^^YYYUUUUUYYYYUUUUWWWWWWWWW")
print("UUWYY^^YYY^WY^^^^^^^^YYYYYYYUWWUUUUUUUWWWWWWWWWWWW")
print("UUUYY^^^YYUWUYYYYY^YYYYYYUUUUWUUUUUUUUWWWWWWWWWWWW")
print("UUUY^^^U^YYUUUUUYYYYYUUUUUUYYUWUUUWWUUWWWWWWWWWWWW")
print("UUUYU^YY^YYUUUUUYUUUUUUUUUYYYUWWWUUUUUWWWWWWWWWWWW")
print("WELCOME load your image: ")
print("\n\n")
class Img:

    def __init__(self, name):
        self.name = name;

    def load(self, w, h):
        self.img = cv2.imread(self.name)
        self.w = w
        self.h = h

    def ascii_low_contrast(self):

        imres = cv2.resize(self.img, (self.w,self.h))
        imgr = cv2.cvtColor(imres, cv2.COLOR_RGB2GRAY)

        for i in range(self.h):
            for j in range(self.w):
                if imgr[i][j] < 50:
                    print("W", end='')
                elif imgr[i][j] < 100:
                    print("U", end='')
                elif imgr[i][j] < 150:
                    print("Y", end='')
                elif imgr[i][j] < 200:
                    print("^", end='')
                else:
                    print("`", end='')

            print("")

    #better
    def ascii_high_contrast(self):

        imres = cv2.resize(self.img, (self.w,self.h))
        imgr = cv2.cvtColor(imres, cv2.COLOR_RGB2GRAY)

        for i in range(self.h):
            for j in range(self.w):
                if imgr[i][j] < 50:
                    print("`", end='')
                elif imgr[i][j] < 100:
                    print("^", end='')
                elif imgr[i][j] < 150:
                    print("Y", end='')
                elif imgr[i][j] < 200:
                    print("U", end='')
                else:
                    print("W", end='')

            print("")


    def ascii_high_detail_beta(self):

        imres = cv2.resize(self.img, (self.w,self.h))
        imgr = cv2.cvtColor(imres, cv2.COLOR_RGB2GRAY)

        for i in range(self.h):
            for j in range(self.w):
                if imgr[i][j] < 33:
                    print("`", end='')
                elif imgr[i][j] < 255:
                    print(chr(imgr[i][j]), end='')
                else:
                    print("W", end='')


            print("")


img = Img('head2.png')
img.load(200, 200)
img.ascii_high_contrast()
# #__author__ = 'litongyang'
# # -*- coding: utf-8 -*-
# '''
# 局部加权回归
# '''
#
# from numpy import *
#
# def loadDataSet(fileName):      #general function to parse tab -delimited floats
#     # numFeat = len(open(fileName).readline().split('\t')) - 1 #get number of fields
#     # dataMat = []; labelMat = []
#     # fr = open(fileName)
#     # for line in fr.readlines():
#     #     lineArr =[]
#     #     curLine = line.strip().split('\t')
#     #     for i in range(numFeat):
#     #         lineArr.append(float(curLine[i]))
#     #     dataMat.append(lineArr)
#     #     labelMat.append(float(curLine[-1]))
#     dataMat = [i for i in range(0,10)]
#     labelMat = [i for i in range(0,10)]
#     return dataMat,labelMat
#
# def standRegres(xArr,yArr):
#     xMat = mat(xArr); yMat = mat(yArr).T
#     xTx = xMat.T*xMat
#     if linalg.det(xTx) == 0.0:
#         print "This matrix is singular, cannot do inverse"
#         return
#     ws = xTx.I * (xMat.T*yMat)
#     return ws
#
# def lwlr(testPoint,xArr,yArr,k=1.0):
#     xMat = mat(xArr); yMat = mat(yArr).T
#     m = shape(xMat)[0]
#     weights = mat(eye((m)))
#     for j in range(m):                      #next 2 lines create weights matrix
#         diffMat = testPoint - xMat[j,:]     #
#         weights[j,j] = exp(diffMat*diffMat.T/(-2.0*k**2))
#     xTx = xMat.T * (weights * xMat)
#     if linalg.det(xTx) == 0.0:
#         print "This matrix is singular, cannot do inverse"
#         return
#     ws = xTx.I * (xMat.T * (weights * yMat))
#     return testPoint * ws
#
# def lwlrTest(testArr,xArr,yArr,k=1.0):  #loops over all the data points and applies lwlr to each one
#     m = shape(testArr)[0]
#     yHat = zeros(m)
#     for i in range(m):
#         yHat[i] = lwlr(testArr[i],xArr,yArr,k)
#     return yHat
#
# def lwlrTestPlot(xArr,yArr,k=1.0):  #same thing as lwlrTest except it sorts X first
#     yHat = zeros(shape(yArr))       #easier for plotting
#     xCopy = mat(xArr)
#     xCopy.sort(0)
#     for i in range(shape(xArr)[0]):
#         yHat[i] = lwlr(xCopy[i],xArr,yArr,k)
#     return yHat,xCopy
#
# def rssError(yArr,yHatArr): #yArr and yHatArr both need to be arrays
#     return ((yArr-yHatArr)**2).sum()
#
# def ridgeRegres(xMat,yMat,lam=0.2):
#     xTx = xMat.T*xMat
#     denom = xTx + eye(shape(xMat)[1])*lam
#     if linalg.det(denom) == 0.0:
#         print "This matrix is singular, cannot do inverse"
#         return
#     ws = denom.I * (xMat.T*yMat)
#     return ws
#
# def ridgeTest(xArr,yArr):
#     xMat = mat(xArr); yMat=mat(yArr).T
#     yMean = mean(yMat,0)
#     yMat = yMat - yMean     #to eliminate X0 take mean off of Y
#     #regularize X's
#     xMeans = mean(xMat,0)   #calc mean then subtract it off
#     xVar = var(xMat,0)      #calc variance of Xi then divide by it
#     xMat = (xMat - xMeans)/xVar
#     numTestPts = 30
#     wMat = zeros((numTestPts,shape(xMat)[1]))
#     for i in range(numTestPts):
#         ws = ridgeRegres(xMat,yMat,exp(i-10))
#         wMat[i,:]=ws.T
#     return wMat
#
# def regularize(xMat):#regularize by columns
#     inMat = xMat.copy()
#     inMeans = mean(inMat,0)   #calc mean then subtract it off
#     inVar = var(inMat,0)      #calc variance of Xi then divide by it
#     inMat = (inMat - inMeans)/inVar
#     return inMat
#
# def stageWise(xArr,yArr,eps=0.01,numIt=100):
#     xMat = mat(xArr); yMat=mat(yArr).T
#     yMean = mean(yMat,0)
#     yMat = yMat - yMean     #can also regularize ys but will get smaller coef
#     xMat = regularize(xMat)
#     m,n=shape(xMat)
#     #returnMat = zeros((numIt,n)) #testing code remove
#     ws = zeros((n,1)); wsTest = ws.copy(); wsMax = ws.copy()
#     for i in range(numIt):
#         print ws.T
#         lowestError = inf;
#         for j in range(n):
#             for sign in [-1,1]:
#                 wsTest = ws.copy()
#                 wsTest[j] += eps*sign
#                 yTest = xMat*wsTest
#                 rssE = rssError(yMat.A,yTest.A)
#                 if rssE < lowestError:
#                     lowestError = rssE
#                     wsMax = wsTest
#         ws = wsMax.copy()
#         #returnMat[i,:]=ws.T
#     #return returnMat
#
# #def scrapePage(inFile,outFile,yr,numPce,origPrc):
# #    from BeautifulSoup import BeautifulSoup
# #    fr = open(inFile); fw=open(outFile,'a') #a is append mode writing
# #    soup = BeautifulSoup(fr.read())
# #    i=1
# #    currentRow = soup.findAll('table', r="%d" % i)
# #    while(len(currentRow)!=0):
# #        title = currentRow[0].findAll('a')[1].text
# #        lwrTitle = title.lower()
# #        if (lwrTitle.find('new') > -1) or (lwrTitle.find('nisb') > -1):
# #            newFlag = 1.0
# #        else:
# #            newFlag = 0.0
# #        soldUnicde = currentRow[0].findAll('td')[3].findAll('span')
# #        if len(soldUnicde)==0:
# #            print "item #%d did not sell" % i
# #        else:
# #            soldPrice = currentRow[0].findAll('td')[4]
# #            priceStr = soldPrice.text
# #            priceStr = priceStr.replace('$','') #strips out $
# #            priceStr = priceStr.replace(',','') #strips out ,
# #            if len(soldPrice)>1:
# #                priceStr = priceStr.replace('Free shipping', '') #strips out Free Shipping
# #            print "%s\t%d\t%s" % (priceStr,newFlag,title)
# #            fw.write("%d\t%d\t%d\t%f\t%s\n" % (yr,numPce,newFlag,origPrc,priceStr))
# #        i += 1
# #        currentRow = soup.findAll('table', r="%d" % i)
# #    fw.close()
#
# '''
# from time import sleep
# import json
# import urllib2
# def searchForSet(retX, retY, setNum, yr, numPce, origPrc):
#     sleep(10)
#     myAPIstr = 'AIzaSyD2cR2KFyx12hXu6PFU-wrWot3NXvko8vY'
#     searchURL = 'https://www.googleapis.com/shopping/search/v1/public/products?key=%s&country=US&q=lego+%d&alt=json' % (myAPIstr, setNum)
#     pg = urllib2.urlopen(searchURL)
#     retDict = json.loads(pg.read())
#     for i in range(len(retDict['items'])):
#         try:
#             currItem = retDict['items'][i]
#             if currItem['product']['condition'] == 'new':
#                 newFlag = 1
#             else: newFlag = 0
#             listOfInv = currItem['product']['inventories']
#             for item in listOfInv:
#                 sellingPrice = item['price']
#                 if  sellingPrice > origPrc * 0.5:
#                     print "%d\t%d\t%d\t%f\t%f" % (yr,numPce,newFlag,origPrc, sellingPrice)
#                     retX.append([yr, numPce, newFlag, origPrc])
#                     retY.append(sellingPrice)
#         except: print 'problem with item %d' % i
#
# def setDataCollect(retX, retY):
#     searchForSet(retX, retY, 8288, 2006, 800, 49.99)
#     searchForSet(retX, retY, 10030, 2002, 3096, 269.99)
#     searchForSet(retX, retY, 10179, 2007, 5195, 499.99)
#     searchForSet(retX, retY, 10181, 2007, 3428, 199.99)
#     searchForSet(retX, retY, 10189, 2008, 5922, 299.99)
#     searchForSet(retX, retY, 10196, 2009, 3263, 249.99)
#
# def crossValidation(xArr,yArr,numVal=10):
#     m = len(yArr)
#     indexList = range(m)
#     errorMat = zeros((numVal,30))#create error mat 30columns numVal rows
#     for i in range(numVal):
#         trainX=[]; trainY=[]
#         testX = []; testY = []
#         random.shuffle(indexList)
#         for j in range(m):#create training set based on first 90% of values in indexList
#             if j < m*0.9:
#                 trainX.append(xArr[indexList[j]])
#                 trainY.append(yArr[indexList[j]])
#             else:
#                 testX.append(xArr[indexList[j]])
#                 testY.append(yArr[indexList[j]])
#         wMat = ridgeTest(trainX,trainY)    #get 30 weight vectors from ridge
#         for k in range(30):#loop over all of the ridge estimates
#             matTestX = mat(testX); matTrainX=mat(trainX)
#             meanTrain = mean(matTrainX,0)
#             varTrain = var(matTrainX,0)
#             matTestX = (matTestX-meanTrain)/varTrain #regularize test with training params
#             yEst = matTestX * mat(wMat[k,:]).T + mean(trainY)#test ridge results and store
#             errorMat[i,k]=rssError(yEst.T.A,array(testY))
#             #print errorMat[i,k]
#     meanErrors = mean(errorMat,0)#calc avg performance of the different ridge weight vectors
#     minMean = float(min(meanErrors))
#     bestWeights = wMat[nonzero(meanErrors==minMean)]
#     #can unregularize to get model
#     #when we regularized we wrote Xreg = (x-meanX)/var(x)
#     #we can now write in terms of x not Xreg:  x*w/var(x) - meanX/var(x) +meanY
#     xMat = mat(xArr); yMat=mat(yArr).T
#     meanX = mean(xMat,0); varX = var(xMat,0)
#     unReg = bestWeights/varX
#     print "the best model from Ridge Regression is:\n",unReg
#     print "with constant term: ",-1*sum(multiply(meanX,unReg)) + mean(yMat)
#
# '''

import numpy as np

class Locally_Weighted_Linear_Regression():
    """Iterative version of Locally Weighted Linear Regression """

    def fit(self, X, y, X_est, tau = 1):
        """
        Fit X_est with Locally weighted linear regression according to X and y
        Parameters
        ----------
        X : {array-like, sparse matrix}, shape = [n_samples, n_features]
            Training vectors, where n_samples is the number of samples and
            n_features is the number of features.
        y : array-like, shape = [n_samples]
            Target values.
        X_est : {array-like, sparse matrix}, shape = [n_samples, n_features]
            Estimation vectors, where n_samples is the number of samples and
            n_features is the number of features.
        tau : float, tau >= 0
            The the bandwidth parameter tau controls how quickly the weight of a training example falls off with distance of its x(i) from the query point x.
        References
        ----------
        CS229 Lecture notes1, Chapter 3 Locally weighted linear regression, Prof. Andrew Ng
        http://cs229.stanford.edu/notes/cs229-notes1.pdf
        """
		
        thetas = [] #init estimated thetas
        estimation = [] #init estimation of X_est

        if tau <= 0:
            print "tau should be greater than 0."
            return [],[]

        for x in X_est: #for every sample in X_est
            #calculate weights that depend on the particular vector x
            weights =  np.exp((-(X - x)*(X - x)).sum(axis = 1)/(2 * tau**2))
            W = np.diag(weights) #diagonal matrix with weights
            x_W = np.dot(X.T, W)
            A = np.dot(x_W, X)
            b = np.dot(x_W, y)
            thetas.append(np.linalg.lstsq(A,b)[0])# calculate thetas for given x with: A^-1 * b
            estimation.append(np.dot(x, thetas[-1])) # calculate estimation for given x and thetas

        return thetas, estimation

if __name__ == '__main__':
    """
    Example was taken from:
    http://www.dsplog.com/2012/02/05/weighted-least-squares-and-locally-weighted-linear-regression/
    """
    # import load_dataset
    from sklearn import datasets

    import matplotlib.pyplot as plt
    iris = datasets.load_iris() #Load data
    print iris.data
    X,y = datasets.load_iris() #iris.data()
    # y = iris.target()

    lwlr = Locally_Weighted_Linear_Regression()
    taus = [1, 10, 25]
    plt.scatter(X[:,1], y) #Plot train data

    color = ["r","g", "b"]
    for i, tau in enumerate(taus):
        thetas, estimation = lwlr.fit(X, y, X, tau = tau)
        plt.plot(X[:,1] ,estimation, c = color[i]) #Plot prediction

    plt.show()

import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from data_retrieval import data_retrieval
from img_collection import img_collect
import pickle

X,y = data_retrieval()
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

#i = 0
#best_acc = 0
#while i < 50:
    #X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
    #lmbda = 0.1
    #model = LogisticRegression(max_iter=500,C = 1/lmbda)
    #model.fit(X_train,y_train[:,2])
    #acc = model.score(X_test,y_test[:,2])
    #print('Accuracy :',acc)

    #if acc > best_acc:
        #best_acc = acc
        #print('BEST :',best_acc)
        #with open('third_model'+str(i)+'.pickle','wb') as file:
            #pickle.dump(model,file)
    #i += 1


pickle_model = open('first_model.pickle','rb')
model1 = pickle.load(pickle_model)

pickle_model = open('second_model.pickle','rb')
model2 = pickle.load(pickle_model)

pickle_model = open('third_model.pickle','rb')
model3 = pickle.load(pickle_model)

pred1 = model1.predict(X_test)
pred2 = model2.predict(X_test)
pred3 = model3.predict(X_test)

count = 0
for i in range(len(pred1)):
    pred = np.array([pred1[i],pred2[i],pred3[i]])

    if np.any(y_test[i] != pred):
        print('FALSE :',y_test[i],'-->',pred)
    else:
        count += 1
        print('TRUE :',count,'/',i+1)

#X_test = img_collect('name.png')
#print(model.predict(X_test))

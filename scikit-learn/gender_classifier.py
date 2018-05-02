from sklearn import tree
x = [[190,70,43],[166,65,45],[190,90,47],[175,64,39],[171,75,40],[177,80,42],[160,60,38],[144,54,37]]
y = ['male','male','male','male','female','female','female','female']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(x,y)

pred = clf.predict([[190,70,43]])

print pred

from sklearn import tree

#[height,weight,shoe size]

X=[[188,76,43],[177,68,43],[143,65,45],[153,98,50],[120,60,42],[100,55,42]]

Y=['male','male','female','male','female','female']


clf=tree.DecisionTreeClassifier()

clf=clf.fit(X,Y)

prediction=clf.predict([[184,70,43]])

print (prediction)
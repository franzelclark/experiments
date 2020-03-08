__author__ = 'clark ronquillo ust-computerscience'

from sklearn import tree
#features = weight, 0 for bumpy 1 for smooth
#labels = 0 for apples 1 for oranges

features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [0, 0, 1, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print("I will predict if it is an Apple or Orange.\n")
prediction = clf.predict([[int(input("Weight (in grams): ")), int(input("Smoothness: "))]])
if prediction == [0]:
    print("I predict that it is an Apple")
elif prediction == [1]:
    print("I predict that it is an Orange")

#print(prediction)
#[0] or [1]

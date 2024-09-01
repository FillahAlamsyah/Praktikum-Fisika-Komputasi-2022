from sklearn.neighbors import NearestCentroid
#database : gerbang logika AND
# x = data, Y = Target

x = [[0 , 0, 0],
     [0 , 5, 0],
     [0 , 0, 5],
     [0 , 5, 5],
     [5 , 5, 0],
     [5 , 0, 5],
     [5 , 5, 5],
     [10, 5, 5],
     [5 , 10, 5],
     [10, 10, 10]
     ]
y = [0,0,0,5,5,5,10,10,5,0]

# Training and Classify
clf = NearestCentroid()
clf = clf.fit(x,y)

#prediksi
print ("logika AND Metode Decision Tree")
print ("Logika = Prediksi")
print ("10 10  5  = ", clf.predict([[10 ,10  ,5] ] ) )
print ("5  10  2  = ", clf.predict([[5  ,10  ,2] ] ) )
print ("2  0   10 = ", clf.predict([[2  ,0   ,10]] ) )
print ("5  0   2  = ", clf.predict([[5  ,0   ,2] ] ) )
print ("0  0   2  = ", clf.predict([[0  ,0   ,2] ] ) )
print ("2  10  2  = ", clf.predict([[2  ,10  ,2] ] ) )
print ("1  12  5  = ", clf.predict([[1  ,12   ,5] ] ) )
print ("2  2   6  = ", clf.predict([[2  ,2   ,6] ] ) )
print ("10 5   7  = ", clf.predict([[10 ,5   ,7] ] ) )

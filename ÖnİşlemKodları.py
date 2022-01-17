import numpy as np # Matematiksel işlemler için
import pandas as pd # Veri işlemleri. (Veri okuma)
from  openpyxl import * #Excel için

# Veri setimizi atarıyoruz.
dataset = pd.read_excel(r'C:\Users\oski_\.spyder-py3\veriseti.xlsx')
x = dataset.iloc[:, :-1].values #Son sütun hariç hepsini al.
y = dataset.iloc[:, -1].values #Sadece son kolonu al.

#Boş verileri doldurma
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent') # En çok tekrar eden veriyi yazar
imputer.fit(x[:, 0:1]) # En çok tekrar eden değeri hazırlıyor 0. sütunda yani Renk sütununda
x[:, 0:1] = imputer.transform(x[:, 0:1]) # En çok tekrar eden değeri aktarıyor.

# One Hot Encoder için kütüphaneler -- Sorun çıkardığı için yapılmadı.
#from sklearn.compose import ColumnTransformer
#from sklearn.preprocessing import OneHotEncoder
#ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough') # 0. kolona uygulayacağız ve diğer kolonları pas geçeçeğiz.
#x = np.array(ct.fit_transform(x))


# Test ve Train Bölümü
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)

#Ölçekleme
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train[:, 1:] = sc.fit_transform(x_train[:, 1:])
x_test[:, 1:] = sc.transform(x_test[:, 1:])
#print(y_train)
#print(y_test)
#print(x_train)
#print(x_test)

kitap = load_workbook("veriseti.xlsx")
veriler = kitap.active

sendData = pd.DataFrame(x_train)
sendData2 = pd.DataFrame(x_test)
sendData3 = pd.DataFrame(y_train)
sendData4 = pd.DataFrame(y_test)

sendData.to_excel('x_train.xlsx', sheet_name = 'islenmis', index=False)
sendData2.to_excel('x_test.xlsx', sheet_name = 'islenmis', index=False)
sendData3.to_excel('y_train.xlsx', sheet_name = 'islenmis', index=False)
sendData4.to_excel('y_test.xlsx', sheet_name = 'islenmis', index=False)


kitap.save("veriseti.xlsx")
kitap.close() #Üstteki satırda kaydediyoruz ve bu satırda kapatıyoruz.







# Analytics-Model-Deployment
Pada case ini akan dilakukan deployment model menggunakan postman. Sebelumnya model sudah di buat menggunakan jupyter notebook menggunakan data testing kemudian disimpan menggunakan format (.pkl). Kemudian dibentuk server menggunakan framework/packages flask dipython.
Dengan menggunakan 'pythonanywhere.com' dibuat agar model tersebut bisa di deploy ke public menggunakan API (Application Programming Interface). Kemudian dengan menggunakan pythonanywhere.com/api dapat dilakukan testing model dengan menambah input nilai-nilai variable yang digunakan mengguanakan software postman.

# Content
- dataset :
    - input.txt : contoh inputan dengan menggunakan lebih dari 1 observasi untuk di prediksi 
- code :
    - Credit Scoring using Random Forest.pkl : model klasifikasi dengan menggunakan random forest yang telah disimpan ke dalam format .pkl
    - server.py : code untuk membuat server di prompt dan di 'pythonanywhere.com'
    - request.py : code untuk membuat request/prediksi model di prompt.

# Cara Deployment Model di POSTMAN
1. Pastikan software "POSTMAN" sudah ada di laptop
2. Kemudian lakukan request di postman, dengan klik tanda "+NEW" di kiri atas dan pilih request
3. Pilih 'POST' lalu Copy url ini (faizah.pythonanywhere.com/api) pada 'Enter Request URL' 
4. Kemudian pilih tab 'Body' lalu pilih 'raw'
5. Lalu kemudian tulisankan nilai-nilai dari variabel prediktor sehingga hasil yang diharapkan adalah melihat kreditnya akan terlambat atau tidak. Sebagai contoh:
    
    Diketahui Bapak Anton seorang suami yang berumur 50 tahun dan saat ini bekerja sebagai pegawai negeri sipil dengan status pendidikan terakhir S2 telah mengajukan kredit di ASTRA tahun lalu dengan jumlah limit kredit yang diambil sebesar 50000 selama 2 tahun, pada bulan pertama tagihan pak 
    Anton sebesar 22000, bulan keduan 24000, dan bulan ketiga 21000, kemudian jumlah pembayaran yang dibayar pada bulan pertama adalah 1230, bulan kedua adalah 1345, dan bulan ketiga adalah 1500. Kemudian menurut data di bank ASTRA, Bapak Anton
    pada tagihan pertama tidak mengalami keterlambatan, kemudian tagihan kedua tidak mengalami keterlambatan dan begitu pula tagihan ketiga tidak mengalami keterlambatan. Dengan informasi diatas kita dapat meprediksikan status kredit pak Anton akan terlambat atau tidak. Dengan membuat inputan di postman sebagai berikut:

       [{"LIMIT_BAL":50000, "AGE":50, "BILL_AMT1":22000, "BILL_AMT2":24000, "BILL_AMT3":21000, "PAY_AMT1":1230,
       "PAY_AMT2":1345, "PAY_AMT3":1500, "MARRIAGE_1":0, "MARRIAGE_2":1, "MARRIAGE_3":0,
       "EDUCATION_1":1, "EDUCATION_2":0, "EDUCATION_3":0, "EDUCATION_4":0, "SEX_1":1,
       "SEX_2":0, "PAY_1_0":1, "PAY_1_1":0, "PAY_1_2":0, "PAY_1_3":0, "PAY_1_4":0,
       "PAY_2_0":1, "PAY_2_1":0, "PAY_2_2":0, "PAY_2_3":0, "PAY_2_4":0, "PAY_3_0":1,
       "PAY_3_1":0, "PAY_3_2":0, "PAY_3_3":0, "PAY_3_4":0}]
       
    Input ini juga dapat digunakan untuk beberapa observasi secara langsung, dengan menambah infromasi data di bawah observasi pertama dan seterusnya. Hal ini dapat dilihat pada folder dataset 'input.txt' dengan 10 observasi sebagai contoh.
6. Setelah menginput informasi-informasi pada poin(5) selanjutnya pilih 'SEND' yang berada di sebelah kanan.
7. Setelah itu, kita akan dapat mengetahui apakah jenis kredit dari kreditor tersebut terlambat atau tidak. Output : "Tidak Terlambat" dan "Terlambat".

# Informasi Dataset
Pada case ini saya menggunakan dataset tentang credit scoring di ASTRA. Dimana variabel prediktor yang saya gunakan ada 14 variable, dimana diantaranya ada 5 variable yang di dummies sehingga menjadi 32 variabel.
Sebagai keterangan variabel prediktor sebagai berikut:
1. "LIMIT_BAL": Jumlah limit Uang Kredit yang diberikan
2. "AGE": Umur kreditor 
3. "BILL_AMT1": Jumlah Bill bulan pertama 
4. "BILL_AMT2": Jumlah Bill bulan kedua 
5. "BILL_AMT3": Jumlah Bill bulan ketiga
6. "PAY_AMT1": Jumlah pembayaran bulan pertama
7. "PAY_AMT2": Jumlah pembayaran bulan kedua
8. "PAY_AMT3": Jumlah pembayaran bulan pertama 

Variable dummies:
9. "MARRIAGE_1": Status pernikah : 'Belum Menikah'
10. "MARRIAGE_2": Status pernikah : 'Menikah' 
11. "MARRIAGE_3": Status pernikah : 'Lainnya'
note: Sehingga jika diketahui kreditor berstatus menikah maka untuk "MARRIAGE_1": 0, "MARRIAGE_2": 1, "MARRIAGE_3":0 

12. "EDUCATION_1": Status Pendidikan Terakhir : 'S2/S3' 
13. "EDUCATION_2": Status Pendidikan Terakhir : 'Dipl/S1'
14. "EDUCATION_3": Status Pendidikan Terakhir : 'SMA' 
15. "EDUCATION_4": Status Pendidikan Terakhir : 'Lainnya' 
note: Sehingga jika diketahui kreditor berstatus pendidikan terakhir S2/S3 maka untuk "EDUCATION_1": 1, "EDUCATION_1": 0, "EDUCATION_2":0, "EDUCATION_3":0, "EDUCATION_4":0

16. "SEX_1": Jenis Kelamin : 'Pria'
17. "SEX_2": Jenis Kelamin : 'Wanita'
note: Sehingga jika diketahui kreditor berjenis kelamin wanita maka untuk "SEX_1":0, "SEX_1":1
 
18. "PAY_1_0": Status tagihan pembayaran kredit pertama : 'tidak terlambat'
19. "PAY_1_1": Status tagihan pembayaran kredit pertama : 'terlambat 1 bulan'
20. "PAY_1_2": Status tagihan pembayaran kredit pertama : 'terlambat 2 bulan' 
21. "PAY_1_3": Status tagihan pembayaran kredit pertama : 'terlambat 3 bulan' 
22. "PAY_1_4": Status tagihan pembayaran kredit pertama : 'terlambat 4 bulan'
note: Sehingga jika diketahui kreditor berjenis status tagihan pembayaran pertama terlambat 2 bulan maka "PAY_1_0":0, "PAY_1_1":0, "PAY_1_2":1, "PAY_1_3":0, "PAY_1_4":0.

23. "PAY_2_0": Status tagihan pembayaran kredit bulan kedua : 'tidak terlambat'
24. "PAY_2_1": Status tagihan pembayaran kredit bulan kedua : 'terlambat 1 bulan'
25. "PAY_2_2": Status tagihan pembayaran kredit bulan kedua : 'terlambat 2 bulan' 
26. "PAY_2_3": Status tagihan pembayaran kredit bulan kedua : 'terlambat 3 bulan' 
27. "PAY_2_4": Status tagihan pembayaran kredit bulan kedua : 'terlambat 4 bulan'
note: Sehingga jika diketahui kreditor berjenis status tagihan pembayaran kedua terlambat 1 bulan maka "PAY_2_0":0, "PAY_2_1":1, "PAY_2_2":1, "PAY_2_3":0, "PAY_2_4":0.

28. "PAY_3_0": Status tagihan pembayaran kredit bulan ketiga : 'tidak terlambat'
29. "PAY_3_1": Status tagihan pembayaran kredit bulan ketiga : 'terlambat 1 bulan'
30. "PAY_3_2": Status tagihan pembayaran kredit bulan ketiga : 'terlambat 2 bulan' 
31. "PAY_3_3": Status tagihan pembayaran kredit bulan ketiga : 'terlambat 3 bulan' 
32. "PAY_3_4": Status tagihan pembayaran kredit bulan ketiga : 'terlambat 4 bulan'
note: Sehingga jika diketahui kreditor berjenis status tagihan pembayaran ketiga tidak terlambat maka "PAY_3_0":1, "PAY_3_1":0, "PAY_3_2":1, "PAY_3_3":0, "PAY_3_4":0.







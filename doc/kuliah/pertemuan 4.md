<h2 align="center">PEMBUATAN METHOD DAN CLASS RETRIVE DATA GEOSPASIAL</h2> 
<p align="justify">
<br>
Latar belakang masalah : 
Pengetahuan mengenai cara memanipulasi data retrieve(melihat data/menghitung jumlah data) masih sangat sedikit, saya akan menjeaskan sedikit bagaimana caranya dengan penggunaan data shapefile geospasial dengan menggunakan bahasa pemrograman phyton dan juga cara penggunaan class dan method.<br>
1.	Apa itu Retrive Data ?<br>
2.	Apa itu Shapefile ?<br>
3.	Apa itu Geometri ?<b>
4.	Bagaimana Operasi Pengambilan Data ?<br>
5.	Buatlah Class Geospasial Editor ?<br>
6.	Bauatlah Method Select, Where Negara ?<br>
<br>
Isi :<br>
Retrive Data Geospasial adalah Meretrive Data Vektor.<br>
Data Shapefile.shp<br>
Operasi Retrive Data menggunakan Library python yang bernama py.shp<br> 
Shapefile adalah Syandard file<br>
Vektor Geospasial dikeluarkan oleh ESRI<br>
 <br>
 <p align="center">
<br>
<img src="../../img/1.jpg" width="200" height="400">
</p><br>
Geometri<br>
Data koordinat yang membentuk bangun datar atau ruang diantaranya :<br>
1.	Point/titik [1]<br>
2.	Line/garis [3] shapefile,type<br>
3.	Polygon [5]<br>
<br>
Operasi Pengambilan Data<br>
Menggunakan library pyshp, class shapefile<br>
1.	Buka/baca<br>
2. <br>
<img src="../../img/2.jpg" width="200" height="400">
</p><br>
 
<br>
DBF adalah sebuah file yang menyimpan file tabular yang menyimpan data attribut.<br>
Method dari DBF<br>
Fields : nama field<br>
record(n)<br>
Record (n) baris ke (n) records<br>
# (n) adalah nomor sequence record<br>
<br>
Method dari SHP<br>
shapes() - Menampilkan semua<br>
shape(n) - Menampilkan dengan parameter<br>
<br>
1.	Bbox adalah sebuah boundary box (koordinat 4 titik) atau koordinat batas view yang ada pada peta.<br>
Contohnya :<br>
<br>
<img src="../../img/3.jpg" width="200" height="400">
</p><br>
 <br>
 Koordinat a,b,c,d itu di sebut bbox<br>
<br>
2.	Parts itu apakah record ini bagian dari record lain/ precahan relasi<br>
3.	points adalah koordinat pembentukan peta<br>
4.	shapetype adalah jenis geometri dari points<br>
<br>
polygon digunakan untuk batas tertutup/kembali ke titik awal<br>
contoh : bentuk suatu benua atau wilayah<br>
<br>
polyline tidak kembali ketitik awal <br>
contoh : jalan, sungai, batas wilayah, dll.<br>
<br>
<br>
Membuat Class pada Retrive di editor
<br>
<img src="../../img/pertama.JPG" width="200" height="400">
</p><br>
 <br>
 Menampilkan Select Negara
<br>
<img src="../../img/kedua.JPG" width="200" height="400">
</p><br>
 <br>
Penutup<br>
Kesimpulan<br>
Dapat kita ketahui bagaimana membuat class dan penggunaan method method yang terdapat pada retrieve data
<br>
<br>
Saran<br>
sulitnya memahami penggunaan method, kurang nya latihan praktek di kelas, diperbanyak praktek di dalam kelas nya

<h2 align="center">PEMBUATAN CRUD DATA GEOSPASIAL</h2> 
<p align="justify">
<br>
<br>
Latar Belakang Masalah :<br>
Pada Implementasi GIS banyak hal yang dapat dilakukan. Namun untuk memulainya kita harus belajar terlebih dahulu bagaimana cara memanipulasi data CRUD (Create, Retrieve, Update, Delete). Kali ini saya akan menjelaskan sedikit  tentang bagaimana cara penggunaan data shapefile geospasial menggunakan CRUD.<br>
<br>
1. Bagaimana Cara Create shapefile?<br>
2. Bagaimana Cara Update shapefile?<br>
3. Bagaimana Cara Delete shapefile?<br>
<br>
CREATE DATA GEOSPASIAL<br>
Dalam pembuatan data geospasial kita akan menggunakan lybrari pyshp dan membutuhkan file filename.shp beserta file filename.dbf.<br>
Langkah-langkah yang harus dilakukan, seperti di bawah ini:<br>
1. Meng-import shapefile<br>
2. Meng-instansiasi writer method<br>
    Caranya :<br>
Sf = shapefile.Writer(param)<br>
Param disini dengan memilih shapetype di bawah ini:<br>
a. shapeType = 1<br>
b. shapeType = 3<br>
c. shapeType = 5<br>
3. Melakukan method dbf dan shp sama seperti read.<br>
<br>
Pada Shapefile (shp)<br>
Untuk menambahkan record (ESRI)<br>
1. sf.point (x,y)<br>
3. sf.line = (parts: [[x,y],[z,w],...])<br>
5. sf.poly = (parts: [[x,y],[z,w],...])<br>
<br>
Pada Databasefile (dbf)<br>
Langkah yyang dapat dilakukan yaitu :<br>
1. Membuat atribut terlebih dahulu kemudian menambahkan record.<br>
Contoh:<br>
sf.field (‘Name Field’, ’C’, ’40’)<br>
Maksudnya C adalah Character atau tipe datanya, dan 40 adalah length atau panjang data. Pada contoh di atas dapat diartikan bahwa nama field dengan panjang 40 karakter.<br>
2. Menambahkan record  seperti contoh di bawah ini<br>
sf.record(‘Bandung’)<br>
sf.record(‘Bandung’,’Sarijadi’)<br>
3. Setelah selesai selanjutnya simpan dengan intruksi seperti di bawah ini:<br>
sf.save(‘namefile.shp’)<br>
<br>
UPDATE/EDIT DATA GEOSPASIAL<br>
Editor merupakan alat yang digunakan untuk melakukan editing pada shapefile. Contohnya yaitu delete road. Selain itu ada writer yang merupakan sebuah method yang ada di shapefile untuk membuat file shp baru (shp dan dbf). Di bawah ini merupakan langkah-langkah untuk melakukan editing.<br>
Import shape file<br>
Sf = shape file.editor(warnas.shp)<br>
Sf.point(17,12,0,0)<br>
Sf.record (‘sunda’)<br>
Sf.save<br>
Sf.save (‘warnas.shp’)<br>
a=shapefile.reoder(‘warnas.shp’)<br>
a.recorders()<br>
a.shapes().points<br>
a.shape()[0]<br>
a.shape()[0] points<br>
<br>
[(10,0,10,0)]<br>
<br>
DELETE DATA GEOSPASIAL<br>
Sf.delete(0)<br>
a.shapes()[0].points [(10,0,10,0)]<br>
sf.points [17,12,0,0]<br>
sf.record(‘sunda’)<br>
sf.saver(‘wrns.shp’)<br>
<br>
Penutup<br>
Kesimpulan<br>
Kesempatan kali ini kita dapat mengetahui bagaimana cara membuat CRUD (Creat Update Delete)Data Geospasial.<br>
<br>
Saran<br>
Untuk lebih memahaminya bisa dengan memperbanyak melakukan praktek sendiri.<br>
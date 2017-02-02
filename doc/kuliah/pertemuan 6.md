<h2 align="center">Instalasi Map Proxy dan Map Server</h2> 
<p align="justify">
<br>
<br>
Latar Belakang Masalah :<br>
Dalam pemanfaatan geografis pada sistem digital ada berbagai macam cara, bahkan sudah sampai ada yang menyediakan map yang dapat kita custom sesuai dengan keinginan kita. yaitu "Google Maps". Siapa yang tidak tahu google maps? Penggunaannya di Indonesia maupun dunia sudah menjadi kebutuhan pokok banyak orang, tetapi apakah kalian tahu bahwa kita dapat membuat Maps Custom kita sendiri?
<br>
<br>
1. Apa itu Map Proxy?<br>
2. Apa itu Map Server?<br>
3. Bagaimana cara install Map Proxy?<br>
4. Bagaimana cara install Map Server?<br>
<br>
Solusi Masalah adalah sebagai berikut:<br>
<br>
- Map Server adalah sebuah lingkungan pengembangan open source untuk membangun aplikasi internet spasial diaktifkan. Hal ini dapat dijalankan sebagai program CGI atau melalui Mapscript yang mendukung beberapa bahasa pemrograman (menggunakan SWIG). MapServer dikembangkan oleh University of Minnesota - jadi, sering dan lebih khusus disebut sebagai "UMN MapServer", untuk membedakannya dari komersial "peta server". MapServer awalnya dikembangkan dengan dukungan dari NASA, yang membutuhkan cara untuk membuat citra satelit yang tersedia untuk umum.<br>
<br>
- Map Proxy (mapproxy.org) adalah open source ubin geospasial proxy yang mendukung proyeksi ulang. Awalnya dikembangkan oleh Omniscale Mapproxy adalah server proxy python untuk gambar geospasial. Hal ini dapat membaca data dari WMS, ubin, mapserver dan mapnik, dan cache dan melayani data bahwa sebagai WMS, WMTS, TMS dan KML. Hal ini juga dapat melakukan reprojections antara berbagai sistem koordinat referensi<br>
<br>
Installasi Map server & map proxy<br>
Menggunakan Linux Ubuntu <br>
1. Persiapkan terlebih dahulu sistem operasi ubuntu (bisa menggunakan versi linux yang lain, karena perintahnya kurang lebih sama).<br>
2. Buka terminal kemudian masukkan perintah :<br>
sudo apt-get install cgi-mapserver<br>
3. Untuk mengetahui struktur direktori Map Server, gunakan perintah :<br>
dpkg -L cgi-mapserver<br>
4. Karena saya mengeksekusinya menggunakan python, install python juga dengan perintah :<br>
sudo apt-get install python-pip python-dev<br>
5. Kemudian install uwsgi, dengan perintah :<br>
sudo pip install uwsgi<br>
6. Kemudian install Map Proxy, dengan perintah :<br>
sudo pip install MapProxy <br>
<br>
Penutup<br>
Kesimpulan<br>
jadi pada pertemuan 6 ini , kita dapat mengetahui bagaimana cara menginstall map server dan map proxy di dalam sistem operasi ubuntu di laptop kita dengan menggunakan virtual box.<br>
<br>
Saran<br>
Lebih banyak  di pelajari, dengan mencari referensi referensi di internet maupun di buku.<br>
Nama : Desi Febrianti<br>
NPM : 1144005<br>
Kelas : 3A<br>
Prodi : D4 Teknik Informatika<br>
Mata Kuliah : Sistem Informasi Geografis<br>
<br>
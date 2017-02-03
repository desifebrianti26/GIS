<h2 align="center">Menjalankan Map Proxy dan Map Server</h2> 
<p align="justify">
<br>
<br>
Latar Belakang Masalah :<br>
Untuk cara pemanfaatan geografis yang ada pada sistem digital bisa dengan berbagai macam cara, bahkan sudah ada yang menyediakan map sesuai dengan keinginan kita. yaitu "Maps". Siapa yang tidak tahu google maps? Penggunaannya telah menjadi kebutuhan pokok banyak orang di indonesia atau di dunia, tetapi apakah kalian tahu bahwa kita dapat membuat Maps Custom kita sendiri?<br>
<br>
1. Cara menjalankan Map Proxy dan Map Server<br>
<br>
Solusi Masalah :<br>
1. Jika kita hendak meload data geonya, kita perlu menyiapkannya terlebih dulu akan ditampilkan nantinya di Map Proxy. Kalian bisa mendownload data geospasial di situs ini,<br>
http://www.halaman.download/<br>
kemudian pilih "Producer" dan klik "Indonesia Mapproxy".<br>
2. Jika sudah download file tersebut (Penting!! anda mengekstrak file tersebut dimana, karena path-nya akan digunakan untuk mengedit file yang sudah ada di direktori yang telah di ekstrak tersebut.<br>
Disini saya simpan di direktori Downloads (Huruf kecil dan besar di perhatikan.)<br>
3. Pada file indomap -> mapproxy, akan terdapat 3 file. Buka file agm.yaml<br>
4. Pada file agm.yaml, edit beberapa baris ini sesuai dengan direktory tempat anda menyimpan filenya:<br>
- pada baris<br>
binary: /usr/libexec/mapserver<br>
ubah menjadi<br>
binary: /usr/lib/cgi-bin/mapserv<br>
- pada baris<br>
map: var/mapdata/mapfile/indo.map<br>
ubah menjadi<br>
map: /home/desi/Downloads/indomap/mapfile/indo.map<br>
- Kemudian buat direktori baru dengan nama tmp pada direktori indomap<br>
ubah baris<br>
working_dir: /var/mapdata/tmp<br>
menjadi<br>
/home/desi/Downloads/indomap/tmp<br>
Kemudian Save <br>

5. Kemudian pada direktori mapproxy(di terminal/cmd), gunakanlah perintah :<br>
vi mapproxy.ini<br>
edit baris<br>
chdir = /var/mymapproxy/<br>
menjadi<br>
chdir = /home/desi/Downloads/indomap/mapproxy<br>
Kemudian Save<br>
6. edit file config.py pada direktori mapproxy<br>
ubah ini<br>
application = make_wsgi_app(r'/var/mymapproxy/agm.yaml')<br>
menjadi<br>
application = make_wsgi_app(r'/home/desi/Downloads/indomap/mapproxy/agm.yaml')<br> 
7. Untuk menjalankan programnya gunakan perintah<br>
uwsgi mapproxy.ini<br>
8. Untuk mencobe cek apakah mapproxy sudah terinsall atau belum, buka browser kemudian ketik localhost:8080<br>
9.  Klik demo atau ketik localhost:8080/demo<br>
10. Pada bagian WMTS klik di bawah Image Format yaitu png<br>
11. Tunggu beberapa saat karna datanya sedang di load.<br>
12. Map Peta akan muncul<br>
Penutup<br>
Kesimpulan<br>
jadi pada pertemuan 7 ini , kita dapat mengetahui bagaimana cara menjalankan map server dan map proxy di dalam sistem operasi ubuntu dalam virtual box.<br>
<br>
Saran<br>
Lebih banyak di pelajari lagi, dengan mencari referensi referensi di internet maupun di buku.<br>


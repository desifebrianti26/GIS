<h2 align="center">Menjalankan Map Proxy dan Map Server</h2> 
<p align="justify">
<br>
<br>
Latar Belakang Masalah :<br>
Dalam pemanfaatan geografis pada sistem digital ada berbagai macam cara, bahkan sudah sampai ada yang menyediakan map yang dapat kita custom sesuai dengan keinginan kita. yaitu "Google Maps". Siapa yang tidak tahu google maps? Penggunaannya di Indonesia maupun dunia sudah menjadi kebutuhan pokok banyak orang, tetapi apakah kalian tahu bahwa kita dapat membuat Maps Custom kita sendiri?<br>
<br>
1. Cara menjalankan Map Proxy dan Map Server<br>
<br>
Solusi Masalah :<br>
1. Untuk meload data geospasial, kita perlu menyiapkannya dulu agar akan ditampilkan nantinya di Map Proxy. Kalian bisa mendownload data geospasial di situs ini,<br>
http://www.halaman.download/<br>
kemudian pilih "Producer" dan klik "Indonesia Mapproxy".<br>
2. Jika sudah download ekstrak file tersebut (Penting!! Ketahui dimana anda mengekstrak file tersebut, karena path-nya akan digunakan untuk mengedit file yang ada di direktori yang telah di ekstrak tersebut.<br>
Disini saya simpan di direktori Downloads (Huruf kecil dan besar di perhatikan.)<br>
3. Pada file indomap -> mapproxy, akan terdapat 3 file. Buka file agm.yaml<br>
4. Pada file agm.yaml, edit beberapa baris ini sesuai dengan direktori tempat anda menyimpan file tersebut :<br>
- pada baris<br>
binary: /usr/libexec/mapserver<br>
ubah menjadi<br>
binary: /usr/lib/cgi-bin/mapserv<br>
- pada baris<br>
map: var/mapdata/mapfile/indo.map<br>
ubah menjadi<br>
map: /home/ali/Downloads/indomap/mapfile/indo.map<br>
- Kemudian direktori baru dengan nama tmp pada direktori indomap<br>
ubah baris<br>
working_dir: /var/mapdata/tmp<br>
menjadi<br>
/home/ali/Downloads/indomap/tmp<br>
Kemudian Save <br>
<br>
5. Kemudian pada direktori mapproxy(di terminal/cmd), gunakan perintah :<br>
vi mapproxy.ini<br>
edit baris<br>
chdir = /var/mymapproxy/<br>
menjadi<br>
chdir = /home/ali/Downloads/indomap/mapproxy<br>
Kemudian Save<br>
6. edit file config.py pada direktori mapproxy<br>
ubah<br>
application = make_wsgi_app(r'/var/mymapproxy/agm.yaml')<br>
menjadi<br>
application = make_wsgi_app(r'/home/ali/Downloads/indomap/mapproxy/agm.yaml') <br>
7. Untuk menjalankan programnya gunakan perintah<br>
uwsgi mapproxy.ini<br>
8. Untuk mengecek apakah mapproxy sudah terinsall atau belum, buka browser kemudian ketik localhost:8080<br>
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


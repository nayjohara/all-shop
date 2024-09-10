# Link Deployment
http://najya-johara-allshop.pbp.cs.ui.ac.id/

# Cara mengimplementasikan checklist secara step by step
1) Membuat sebuah direktori lokal dengan nama sesuai dengan nama aplikasi saya yaitu all shop.
2) Setelah itu membuka direktori di terminal dan mengaktifkan virtual environmentnya.
3) Melakukan setup project django dengan cara melakukan penginstalan django dan membuat sebuah project django sesuai dengan nama aplikasi saya yaitu all_shop dan menjalankan perintah untuk startproject yaitu 'python -m django startproject all_shop .'
4) Setelah berhasil membuat project django, pada repositori dibuat file .gitignore. File ini digunakan untuk memilah file yang ada di repositori agar mengetahui apa saja file yang diabaikan.
5) Lalu melakukan pembuatan aplikasi yang dinamakan 'main' dan mengatur pada file 'setting.py' agar Django mengetahui aplikasi tersebut.
6) Melakukan pembuatan file html pada direktori baru yang diberikan nama 'template', file html tersebut saya namakan 'main'.
7) Setelah membuat file html, saya mengganti beberapa kode pada file 'models.py' agar sesuai dengan soal. Pada file ini saya menambahkan atribut 'name', 'price', dan 'description'.
8) Dilakukan migrasi model agar perubahannya diketahui server
9) Lalu saya menghubungkan model, view, dan template pada file 'views.py' agar http dapat menampilkan tampilan yang sesuai.
10) Terakhir dilakukan routing URL pada file 'urls.py'.

# Bagan request client ke web aplikasi berbasis Django beserta responnya 
![bagan](https://github.com/user-attachments/assets/2cfbb72a-8c8b-4952-958c-ea265765720b)

# Fungsi git dalam pengembangan perangkat lunak
Git berfungsi sebagai sistem kontrol versi untuk menyimpan, mengelola, dan berbagi source code. Git dapat membantu melacak setiap perubahan yang dilakukan pada file mencakup siapa yang melakukan perubahan, kapan perubahannya dilakukan, dan kenapa perubahan tersebut dilakukan. Git juga dapat membantu seuatu tim developer untuk melakukan kolaborasi sehingga mereka dapat melakukan pengerjaan bagian proyek secara bersamaan.

# Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak
Django lebih ramah terhadap pemula dikarenakan Django memiliki dokumentasi yang lengkap sehingga lebih mudah dipahami. Django juga menggunakan struktur pola MVT sehingga memudahkan pengguna untuk lebih memahami strukturnya. Django juga menggunakan bahasa pemrograman yang mudah dipahami yaitu python sehingga ramah untuk para pemula.

# Mengapa model pada Django disebut sebagai ORM
Django ORM (Object-Relational Mapping) merupakan kerangka kerja Django yang bertugas untuk memetakan objek Python ke struktur basis data relasional. Django ORM memberikan kemudahan dalam pengembangan, portabilitas, keamanan dari serangan SQL Injection.

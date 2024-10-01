# Link Deployment
http://najya-johara-allshop.pbp.cs.ui.ac.id/

# Tugas 2
## Cara mengimplementasikan checklist secara step by step
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

## Bagan request client ke web aplikasi berbasis Django beserta responnya 
![bagan](https://github.com/user-attachments/assets/2cfbb72a-8c8b-4952-958c-ea265765720b)

## Fungsi git dalam pengembangan perangkat lunak
Git berfungsi sebagai sistem kontrol versi untuk menyimpan, mengelola, dan berbagi source code. Git dapat membantu melacak setiap perubahan yang dilakukan pada file mencakup siapa yang melakukan perubahan, kapan perubahannya dilakukan, dan kenapa perubahan tersebut dilakukan. Git juga dapat membantu seuatu tim developer untuk melakukan kolaborasi sehingga mereka dapat melakukan pengerjaan bagian proyek secara bersamaan.

## Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak
Django lebih ramah terhadap pemula dikarenakan Django memiliki dokumentasi yang lengkap sehingga lebih mudah dipahami. Django juga menggunakan struktur pola MVT sehingga memudahkan pengguna untuk lebih memahami strukturnya. Django juga menggunakan bahasa pemrograman yang mudah dipahami yaitu python sehingga ramah untuk para pemula.

## Mengapa model pada Django disebut sebagai ORM
Django ORM (Object-Relational Mapping) merupakan kerangka kerja Django yang bertugas untuk memetakan objek Python ke struktur basis data relasional. Django ORM memberikan kemudahan dalam pengembangan, portabilitas, keamanan dari serangan SQL Injection.

# Tugas 3
## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform
Data delivery dibutuhkan agar suatu informasi ataupun data bisa berpindah dari satu titik ke titik lain dengan efektif. Terdapat beberapa alasan pentingnya pengimplementasian data delivery:
1) Perlindungan pada data: Data delivery yang baik mencakup enkripsi dan perlindungan data saat dalam proses pengiriman sehingga menjamin keamanan data.
2) Memberikan UX yang baik: dengan data delivery yang baik dapat memastikan user-experience yang mulus dan lancar contohnya saat seperti melakukan streaming tidak terjadi buffering.
3) Memberikan kinerja optimal: dengan mekanisme dari data delivery meningkatkan efisiensi sehingga meningkatkan kinerja dari platform.

## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML
Menurut saya, JSON lebih baik dan lebih populer karena beberapa alasan berikut:
1) JSON memiliki sintaks yang lebih mudah untuk dibaca sehingga menjadi lebih efisien dalam pengembangan web ataupun aplikasi
2) JSON dapat melakukan parsing dengan fungsi JavaScript standar sehingga dia lebih cepat dan efisien
3) JSON lebih kompatibel dengan banyak bahasa pemrograman sehingga bagus untuk digunakan dalam banyak platform

## Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut
Method is_valid() penting untuk melakukan validasi  data yang diterima pada form valid, aman, dan sesuai dengan ketentuan yang sudah dibuat untuk mencegah kesalahan ataupun mengganggu keamanan di aplikasi/web

## Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang
csrf_token penting untuk menlindungi dari serangan CSRF (Cross-Site Request Forgery) dengan cara memastikan setiap permintaan yang adamodifikasi data berasal dari sumber yang benar. Tanpa csrf_token, aplikasi menjadi lebih rentan diserang dengan memanfaatkan user session yang sah tanpa sepengatahuan user

## Cara mengimplementasikan checklist secara step by step
1) Buat forms.py:
   Tambahkan file forms.py di direktori main dan buat form berdasarkan model Product.
2) Implementasi create_product di views.py:
- Import form yang baru dibuat dan redirect.
- Buat fungsi create_product untuk menangani validasi input dan menyimpan data dari form.
- Di fungsi show_main, tambahkan Product.objects.all() untuk mengambil semua data Product  dari database dan kirimkan ke template melalui context.
3) Routing URL:
  Di urls.py, import fungsi create_product dan tambahkan path untuk mengaksesnya.
4) Template HTML (create_product.html):
  Buat file HTML di main/templates dengan form menggunakan metode POST, tambahkan {% csrf_token %}, dan button untuk submit.
5) Fungsi untuk Mengembalikan Data JSON dan XML:
  Di views.py, buat empat fungsi: show_xml, show_json, show_xml_by_id, dan show_json_by_id untuk menampilkan data Product dalam format JSON dan XML.
6) Routing untuk JSON dan XML:
  Tambahkan path di urls.py untuk menampilkan data dalam format JSON dan XML.
7) Push ke PWS dan GitHub:
  Lakukan push perubahan ke repositori PWS dan GitHub.

## XML
![XML](https://github.com/user-attachments/assets/32a9e4e1-ce15-425b-a38f-0d3a487a8f64)

## XML by id
![XMLById](https://github.com/user-attachments/assets/d474fecb-d0f5-41ec-a0a2-c9fbb911be92)

## JSON
![JSON](https://github.com/user-attachments/assets/e502422e-c314-41b5-828d-ae66ca709a0b)

## JSON by id
![JSONById](https://github.com/user-attachments/assets/99530139-6f8c-4136-ba3d-a8fcbba1e982)

# Tugas 4
## Perbedaan antar HttpResponseRedirect() dan redirect()
pada HttpResponseRedirect() dia secara langsung membuat objek HTTP response yang mengarahkan user sesuai dengan URL yang sesuai. untuk redirect(), dia merupakan shortcut dari HttpResponseRedirect namun bisa menerima lebih banyak jenis argumen. redirect() juga menggunakan parameter positional sehingga kita hanya perlu memberikan nama biew atau URL tujuan dan Django akan mengonversinya menjadi URL yang tepat.

## Cara kerja penghubungan model Product dan User
Pada Django, product bisa dihubungkan dengan User dengan menggunakan ForeignKey dimana setiap produk hanya bisa dimiliki satu user, namun user bisa memiliki banyak produk. Owner pada model Product akan menyimpan informasi tentang produk sehingga produk tersebut akan terhubung secara otomatis dengan User melalui penggunaan ForeignKey.

## Perbedaan Authentication dan Authorization dan bagaimana Django mengimplementasinya
1) Authentication: merupakan proses pemeriksaan apakah user sesuai dengan data biasanya dengan cara memasukkan username dan password dan informasi yang dimasukkan user benar maka mereka bisa masuk kedalam sistem.
2) Authorization: merupakan proses yang terjadi setelah user berhasil masuk ke sistem sehingga nanti Django akan menentukan hal apa saja yang bisa diakses oleh pengguna dan apa saja yang tidak bisa dikases oleh pengguna.

Implementasi Django pada proses authentication yaitu saat user melakukan login dengan authentication view Django dimana informasi yang mereka masukkan akan dicek apakah sesuai dengan data. Saat informasi sudah terverifikasi, Django akan membuat sesi untuk user dan user bisa masuk kedalam sistem. Implementasi pada authorization yaitu menggunakan permission classes dan decorators dimana jika kita menggunakan @login_required pada suatu view maka view itu hanya dapat diakses oleh user yang sudah terverifikasi.

## Bagaimana Django mengingat pengguna yang telah login dan kegunaan lain dari cookies dan apakah semua cookies aman
Django menggunakan sesi untuk mengingat pengguna yang sudah login. Saat login berhasil, Django akan membuat sesi dan menyimpan identifier atau session ID dalam bentuk cookie di browser pengguna.

Pengelolaan Cookie: Cookie memungkinkan Django mengenali pengguna yang kembali tanpa perlu login lagi, kecuali sesi tersebut telah kedaluwarsa atau pengguna melakukan logout. Selain untuk otentikasi, cookie juga berguna untuk:
1) Melacak perilaku pengguna, karena cookie dapat menyimpan informasi seperti preferensi dan aktivitas pengguna selama sesi berlangsung.
2) Menyimpan pengaturan pengguna, seperti bahasa yang dipilih atau tema tampilan, sehingga pengalaman mereka lebih personal.

Namun, tidak semua cookie aman digunakan, tergantung pada bagaimana pengamanannya diterapkan. Django menyediakan dua fitur penting untuk melindungi cookie: HttpOnly dan Secure. HttpOnly mencegah akses cookie oleh JavaScript di browser, sehingga hanya server yang bisa membaca atau memodifikasinya melalui protokol HTTP/HTTPS. Sementara itu, Secure memastikan cookie hanya dikirim melalui koneksi HTTPS yang terenkripsi, sehingga lebih aman dari serangan luar.

## Cara mengimplementasikan checklist secara step-by-step
1. Membuat Form Register:
   - membuat fungsi register di view untuk menampilkan form pendaftaran akun baru
   - membuat file HTML agar user bisa melakukan pendaftaran dengan mengisi informasi yang dibutuhkan
   - menambahkan path di url untuk menghubungkan fungsi register
2. Membuat Fungsi Login dan Logout:
   - Buat fungsi login yang memungkinkan pengguna masuk. Saat pengguna berhasil login, Django akan membuat cookie bernama last_login yang mencatat kapan pengguna terakhir kali login.
   - Buat fungsi logout yang menghapus cookie last_login menggunakan response.delete_cookie('last_login') ketika pengguna keluar.
3. Menampilkan Cookie last_login di Halaman Web:
   - menambahkan last_login: request.COOKIES['last_login'] di views
4. Menambahkan URL path untuk login dan logout di url
5. Menambahkan decorator @login_required pada views agar user harus login dahulu sebelum masuk
6. Menghubungkan Product dengan User:
   - menggunakan ForeignKey untuk menghubungkan product dengan user di models.py dan melakukan migrasi agar perubahan tersimpan.


# Tugas 5

## Urutan PRioritas Pengambilan CSS Selector 
Dalam CSS, urutan prioritas menentukan mana gaya yang diterapkan ketika beberapa aturan berlaku untuk elemen yang sama. Pertama, inline styles (gaya langsung di elemen) memiliki prioritas tertinggi. Selanjutnya, ID selectors (yang menggunakan tanda #) lebih kuat daripada class selectors (yang menggunakan tanda .) dan pseudo-classes (seperti :hover), yang semuanya memiliki prioritas yang sama. Kemudian, ada tag selectors (seperti div atau p), dan terakhir adalah universal selector (tanda *), yang memiliki prioritas terendah. Jika ada dua aturan dengan prioritas yang sama, aturan yang muncul terakhir di CSS akan digunakan.

## Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web dan contoh aplikasi yang sudah dan belum menerapkan responsive design
Responsive Design penting dalam pengembangan aplikasi web dikarenakan dengan responsive design memmungkinkan sebuah web untuk menyesuaikan UI nya dengan berbagai ukuran layar mulai dari desktop hingga layar mobile. Dengan responsive design, kita dapat meningkatkan user experience yang kita berikan seperti memudahkan user membaca suatu informasi, selain itu juga memudahkan untuk diakses dengan segala perangkat. Contoh web yang sudah menerapkan responsive design: 'https://www.tokopedia.com'. Contoh web yang belum menerapkan responsive design: 'https://jatengprov.go.id/'

## Perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tesrbut
Margin, border, dan padding adalah tiga properti CSS yang digunakan untuk mengatur ruang di sekitar elemen HTML. Margin adalah ruang di luar elemen yang memisahkan elemen tersebut dari elemen lainnya, dan dapat diatur dengan properti seperti margin: 10px;. Border adalah garis yang mengelilingi elemen dan dapat dikustomisasi dengan ketebalan, jenis, dan warna menggunakan properti seperti border: 2px solid black;. Padding adalah ruang di dalam elemen, antara konten dan batas border, yang memberikan jarak antara konten dan garis batasnya, dan diatur dengan padding: 10px;. 

## Jelaskan konsep flex box dan grid layput dan kegunaannya
lexbox digunakan untuk membuat tata letak satu dimensi, baik secara horizontal maupun vertikal, sehingga memudahkan pengaturan posisi dan distribusi ruang antar elemen, seperti pada menu navigasi atau tombol. Sementara itu, Grid Layout dirancang untuk tata letak dua dimensi, memungkinkan pengaturan elemen dalam baris dan kolom, sehingga cocok untuk struktur yang lebih kompleks, seperti galeri gambar atau halaman dengan banyak konten. 

## Cara mengimplementasikan checklist secara step-by-step
1. Buat Fitur Edit Product: Tambahkan fungsi edit_product di views.py dan buat path URL untuk fitur edit product di urls.py.
2. Buat Fitur Delete Product: Tambahkan fungsi delete_product di views.py yang menerima parameter request dan id, lalu buat path URL untuk fitur delete product di urls.py.
3. Buat File HTML untuk Edit Product: Buat file HTML khusus untuk mengedit produk dan file HTML untuk navigasi (navbar).
4. Konfigurasi Static Files: Di settings.py, tambahkan middleware WhiteNoise dan atur STATIC_ROOT, STATICFILES_DIRS, dan STATIC_URL untuk mengelola file statis.
5. Tambahkan Tailwind CSS: Buat folder static yang berisi global.css dan tambahkan script Tailwind ke dalam base.html.
6. Styling Halaman Login dan Register: Terapkan gaya pada halaman login dan register agar lebih menarik.
7. Styling Halaman Create Product dan Edit Product: Sesuaikan tampilan halaman untuk membuat produk dan mengedit produk.
8. Styling pada Card Info, Card Product, Main, dan Navbar: Berikan gaya pada elemen card info, card product, bagian utama, dan navbar.



Nama : Dimas Bayu Nugroho

NPM : 2506534636

Kelas : PBP B

Baru Belajar banh

TUGAS 1 :
AI Disclosure:
Dalam pengerjaan Tugas 1 ini, saya memanfaatkan alat bantu AI (ChatGPT) untuk membantu proses debugging konfigurasi berkas statis (static files) Django serta eksplorasi struktur layout HTML dan CSS.
1. https://chatgpt.com/share/6a9e6fba-0048-83ec-962e-f41f0701b518
2. https://chatgpt.com/share/6a9ea9c2-47c8-83ec-b6f6-5ddb0f5c55ac

Manual Fix:
1. Saya mengubah nilai warna yang masih bersifat hardcoded (Hex Code) dari saran AI pada section Education agar konsisten menggunakan variabel :root yang telah saya definisikan sebelumnya (seperti var(--ink) dan var(--text-muted)).
2. Saya menambahkan card konten baru secara mandiri dengan memanfaatkan struktur dan template HTML/CSS yang disajikan oleh AI.
3. Pada tampilan Education, saya mengubah properti justify-content pada bagian logo dan tahun dari space-between menjadi center. Hal ini dilakukan karena tata letak sebelumnya terlihat kurang seimbang dan posisinya terlalu tinggi (terlalu ke atas).
4. Saya menambahkan tautan navigasi menuju section Education pada bagian header halaman agar memudahkan navigasi pengguna (smooth scrolling).

Pertanyaan Reflektif:
1. Ya, saya menggunakan elemen semantik seperti <header> dan <section>. Elemen ini membuat struktur kode lebih rapi dan mempermudah penerapan styling CSS lebih terstruktrur.
2. Ketika mengatur logo untuk Education, tata letak yang sebelumnya bagus di desktop menjadi aneh dan terlalu sempit ketika pindah ke mobile. Maka dari itu, saya mengubah tata letak logo di mobile sehingga logo diletakkan di atas daripada di kiri seperti pada desktop, hal ini membuat kolom teks menjadi lebih luas, sehingga tidak mepet dan terlalu panjang ke bawah.
3. Batasan yang saya rasakan pada static web murni adalah seluruh informasi harus ditulis secara manual di dalam HTML, sehingga proses pembaruan data menjadi kurang efisien. Saya ingin mengintegrasikan arsitektur MVT Django untuk mengambil data portofolio dari database.




TUGAS 2:

AI Disclosure:
1. Meminta AI menganalisis error Django terkait penambahan field photo pada model Education.
2. Meminta penjelasan penyebab error dan langkah perbaikannya.
3. Menerapkan dan menyesuaikan solusi dari AI secara manual pada proyek.

Log AI:
1. https://chatgpt.com/share/6aa6a2d4-b1e8-83ec-b5b5-d11b9c6b8f6e

Manual Fix:
1. Error terjadi karena field photo bersifat non-nullable, sedangkan database sudah memiliki data lama.
2. Menambahkan penanganan nilai default/kosong pada field photo.
3. Menjalankan python manage.py makemigrations.
4. Menjalankan python manage.py migrate.
5. Menguji kembali aplikasi untuk memastikan error telah teratasi.

Pertanyaan Reflektif:
1. Jelaskan alur yang terjadi ketika pengguna membuka halaman portofolio baru, mulai dari permintaan yang diterima proyek hingga data ditampilkan pada browser. Dalam jawabanmu, jelaskan peran urls.py proyek, urls.py aplikasi, view, model, dan template.

= Ketika pengguna membuka halaman portofolio baru, browser mengirim request ke server Django. Request tersebut pertama kali dicocokkan oleh urls.py portofolio, lalu diteruskan ke urls.py main. Setelah URL ditemukan, Django memanggil view, yang mengambil data portofolio dari model melalui database. Data tersebut kemudian dikirim melalui context ke template, yang mengolahnya menjadi HTML. HTML tersebut dikirim kembali sebagai response dan ditampilkan oleh browser.

2. Mengapa data untuk bagian portofolio baru sebaiknya disimpan pada model dan tidak ditulis langsung di dalam template? Jelaskan dampaknya terhadap kemudahan pemeliharaan dan pengembangan aplikasi.

= Data portofolio sebaiknya disimpan dalam model karena data dapat berubah dan bertambah tanpa harus mengubah kode pada template. Jika data ditulis langsung di template, setiap perubahan data mengharuskan developer mengedit html sehingga menjadi rawan kesalahan. Dengan menyimpan data pada model, template cukup menampilkan data yang diberikan oleh view, sehingga aplikasi menjadi lebih terstruktur.

3. Apa perbedaan fungsi makemigrations dan migrate pada Django? Berikan contoh perubahan model yang mengharuskanmu menjalankan kedua perintah tersebut.

= makemigrations digunakan untuk membuat file migration yang mencatat perubahan pada model, sedangkan migrate digunakan untuk menerapkan perubahan tersebut ke database. Contohnya, jika pada model Education ditambahkan field year = models.IntegerField(), kita menjalankan python manage.py makemigrations untuk membuat migration baru, kemudian python manage.py migrate untuk menerapkan penambahan field tersebut ke database.


TUGAS 3:

AI Disclosure:
1. Meminta AI menganalisis dan membantu memperbaiki error NoReverseMatch pada proyek Django.
2. Meminta penjelasan mengenai penyebab error dan cara kerja URL routing Django.
3. Menerapkan dan menyesuaikan solusi dari AI secara manual pada proyek.

Log AI:
1. https://chatgpt.com/share/6ab15310-efc0-83ec-9256-d2f164cc0fa9

Manual Fix:
1. Menganalisis pesan error NoReverseMatch untuk mengetahui penyebab kegagalan pencarian URL.
2. Memeriksa konfigurasi URL pada urls.py dan penggunaan url name dalam template atau view.
3. Menyesuaikan nama URL atau parameter yang digunakan agar sesuai dengan konfigurasi Django.
4. Memperbaiki kode secara manual berdasarkan hasil analisis AI.
5. Menjalankan kembali aplikasi Django untuk memastikan error telah teratasi.
6. Menguji navigasi dan fungsi terkait untuk memastikan URL dapat diakses dengan benar.


Pertanyaan Reflektif:
1. Jelaskan mengapa kita menggunakan ModelForm pada Django alih-alih membuat form HTML secara manual. Selain itu, jelaskan pula mengapa kita diwajibkan menambahkan {% csrf_token %} pada form tersebut!

= ModelForm mempermudah pembuatan form berdasarkan model Django, termasuk validasi dan penyimpanan data ke database, sehingga lebih efisien daripada membuat form HTML manual. {% csrf_token %} melindungi form dari serangan Cross-Site Request Forgery (CSRF) dengan memastikan request berasal dari sumber yang sah.


2. Pada Tutorial 03, kita membahas format data JSON dan XML. Mengapa JSON lebih disukai dalam pengembangan aplikasi web modern dibandingkan XML?

= JSON lebih disukai karena sintaksnya sederhana, ringan, mudah dibaca, dan mudah diproses oleh JavaScript. JSON juga lebih efisien untuk pertukaran data antara frontend dan backend dibandingkan XML yang menggunakan tag lebih panjang.


3. Jelaskan alur yang terjadi saat kamu menggunakan fungsi view untuk mengembalikan data portofoliomu dalam bentuk JSON. Mengapa kita perlu melakukan proses serialization pada model Django sebelum datanya dikembalikan?

= View mengambil data portofolio dari database menggunakan Django, kemudian melakukan serialization untuk mengubah objek model menjadi format JSON. JSON dikembalikan melalui response agar dapat dibaca dan digunakan oleh client. Serialization diperlukan karena objek Django tidak dapat langsung dikonversi menjadi JSON.


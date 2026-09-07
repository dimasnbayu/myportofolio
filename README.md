Nama : Dimas Bayu Nugroho

NPM : 2506534636

Kelas : PBP B

Baru Belajar banh


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
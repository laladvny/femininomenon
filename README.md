Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama, saya membuat repositori baru di GitHub dan direktori lokal untuk proyek baru ini. Kemudian, saya membuat dan mengaktifkan Virtual Environment sebelum membuat proyek Django dengan perintah startproject. Setelah itu, saya membuat file .env, .env.prod, dan modifikasi file settings.py mengikuti Tutorial 0. Sesudahnya, saya membuat aplikasi main dalam proyek tersebut dengan perintah startapp dan mendaftarkannya ke INSTALLED_APPS di settings.py. 
Untuk template, saya membuat direktori templates dalam aplikasi main lalu membuat berkas main.html yang berisi format tulisan nama dan kelas yang saya isi di views.py. Selain itu, saya mengimplementasi model dalam models.py untuk memiliki atribut yang disebutkan di soal. Terakhir, saya melakukan git add, commit, dan push, tidak lupa push ke pws juga.


Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
urls.py meneruskan request client ke views.py yang sesuai. views.py menggabungkan template dari berkas html dengan data di models.py dan menampilkannya di laman web html.


Jelaskan peran settings.py dalam proyek Django!
settings.py berperan sebagai konfigurasi proyek. Terdapat allowed_hosts untuk siapa yang bisa mengakses proyek, installed_apps untuk menghubungkan dengan aplikasi yang dibuat, dan lain sebagainya.


Bagaimana cara kerja migrasi database di Django?
Migrasi database di Django dilakukan dalam dua tahap, yaitu makemigrations untuk membuat migrasi dari perubahan sebagai persiapan lalu migrate untuk menerapkan perubahan tersebut ke dalam database Django lokal.


Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, Django cukup mudah untuk dipelajari dan digunakan, salah satunya karena menggunakan Python yang syntax-nya beginner friendly.
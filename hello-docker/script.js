JavaScript;
// Fungsi untuk mengubah pesan saat tombol diklik
function ubahPesan() {
  const greeting = document.getElementById("greeting");
  const messages = [
    "Hello World dari Docker! 🐳",
    "Selamat Belajar Docker!",
    "Container itu keren!",
    "JavaScript + Docker = ❤️",
    "Halo dari dalam Container!",
  ];

  // Pilih pesan secara acak
  const randomIndex = Math.floor(Math.random() * messages.length);
  greeting.textContent = messages[randomIndex];

  // Efek animasi sederhana
  greeting.style.transform = "scale(1.2)";
  setTimeout(() => {
    greeting.style.transform = "scale(1)";
  }, 300);
}

// Fungsi ini berjalan otomatis saat halaman dimuat
window.onload = function () {
  const greeting = document.getElementById("greeting");
  greeting.textContent = "Hello World! 🌍";
  console.log("Aplikasi berhasil dijalankan di Docker!");
};

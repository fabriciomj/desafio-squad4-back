const reservaModal = document.getElementById("reserva-modal");
const closeReserva = reservaModal.querySelector(".close");

// Todos os botões que devem abrir o modal
const reservaBtns = [
  document.getElementById("reserva-btn"),
  document.getElementById("reserva-btn-2"),
  document.getElementById("open-reserva")
];

reservaBtns.forEach(btn => {
  if (btn) {
    btn.addEventListener("click", () => {
      reservaModal.style.display = "flex"; // garante centralização
    });
  }
});

closeReserva.addEventListener("click", () => {
  reservaModal.style.display = "none";
});

window.addEventListener("click", (e) => {
  if (e.target === reservaModal) {
    reservaModal.style.display = "none";
  }
});

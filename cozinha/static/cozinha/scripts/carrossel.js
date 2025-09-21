const carouselTrack = document.querySelector('.carousel-track');
const prevBtn = document.querySelector('.nav.prev');
const nextBtn = document.querySelector('.nav.next');

function updateCarousel() {
  const items = carouselTrack.querySelectorAll('.item');
  const middle = Math.floor(items.length / 2);

  items.forEach((item, i) => {
    item.style.transform = "scale(0.1)";
    item.style.transition = "transform 0.3s";
    
    if (i === middle) {
  item.style.transform = "scale(0.9)";
} else if (i === middle - 1 || i === middle + 1) {
  item.style.transform = "scale(0.8) translateX(10px)";
} else if (i === middle - 2 || i === middle + 2) {
  item.style.transform = "scale(0.7) translateX(10px)";
}
const caption = item.querySelector('.caption');
    caption.classList.remove('center');

    // aplica bold somente no item central
    if (i === middle) {
      caption.classList.add('center');
    }
  });
}

// botão "anterior"
prevBtn.addEventListener('click', () => {
  const items = carouselTrack.querySelectorAll('.item');
  const last = items[items.length - 1];
  carouselTrack.insertBefore(last, items[0]);
  updateCarousel();
});

// botão "próximo"
nextBtn.addEventListener('click', () => {
  const items = carouselTrack.querySelectorAll('.item');
  const first = items[0];
  carouselTrack.appendChild(first);
  updateCarousel();
});

updateCarousel();

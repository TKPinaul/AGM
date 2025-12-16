document.addEventListener('DOMContentLoaded', function () {
    const slides = document.querySelectorAll('.image-slider .slide');
    const radios = document.querySelectorAll('.radio-buttons input');
    const totalSlides = slides.length;
    let currentSlide = 0;

    function changeSlide(direction) {
        slides[currentSlide].classList.remove('current-slide');
        radios[currentSlide].checked = false;

        currentSlide = (currentSlide + totalSlides + direction) % totalSlides;

        slides[currentSlide].classList.add('current-slide');
        radios[currentSlide].checked = true;

        updateSlider();
    }

    document.querySelector('.prev-button').addEventListener('click', () => changeSlide(-1));
    document.querySelector('.next-button').addEventListener('click', () => changeSlide(1));

    radios.forEach((radio, index) => {
        radio.addEventListener('change', () => {
            slides.forEach((slide, i) => {
                slide.classList.toggle('current-slide', i === index);
            });

            radios.forEach(r => (r.checked = false));

            currentSlide = index;
            radios[currentSlide].checked = true;

            updateSlider();
        });
    });

    // Initialiser le carrousel
    changeSlide(0);

    setInterval(() => changeSlide(1), 4000);

    function updateSlider() {
        const offset = currentSlide * -20; // Modifier en fonction du nombre d'images
        const slider = document.querySelector('.image-slider');
        slider.style.transform = `translateX(${offset}%)`;
    }
});

const slides = document.querySelectorAll(".hero-carousel .slide");
const anterior = document.querySelector(".hero-carousel .anterior");
const proxima = document.querySelector(".hero-carousel .proxima");

if (slides.length > 0 && anterior && proxima) {
    let indiceAtual = 0;
    let timer = iniciarTimer();

    function mostrarSlide(novoIndice) {
        slides[indiceAtual].classList.remove("active");
        indiceAtual = (novoIndice + slides.length) % slides.length;
        slides[indiceAtual].classList.add("active");
    }

    function iniciarTimer() {
        return setInterval(() => {
            mostrarSlide(indiceAtual + 1);
        }, 5000);
    }

    function reiniciarTimer() {
        clearInterval(timer);
        timer = iniciarTimer();
    }

    anterior.addEventListener("click", () => {
        mostrarSlide(indiceAtual - 1);
        reiniciarTimer();
    });

    proxima.addEventListener("click", () => {
        mostrarSlide(indiceAtual + 1);
        reiniciarTimer();
    });
}
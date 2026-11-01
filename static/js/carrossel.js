
const slides = document.querySelectorAll(".hero-carousel .slide");
const anterior = document.querySelector(".hero-carousel .anterior");
const proxima = document.querySelector(".hero-carousel .proxima");

let indiceAtual = 0;

function mostrarSlide(novoIndice) {
    slides[indiceAtual].classList.remove("active");

    indiceAtual = (novoIndice + slides.length) % slides.length;

    slides[indiceAtual].classList.add("active");
}

anterior.addEventListener("click", () => {
    mostrarSlide(indiceAtual - 1);
});

proxima.addEventListener("click", () => {
    mostrarSlide(indiceAtual + 1);
});

setInterval(() => {
    mostrarSlide(indiceAtual + 1);
}, 5000);

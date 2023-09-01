// For .ml3 animation
var textWrapper = document.querySelector(".ml3");
textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");

const predictionResult = document.querySelector(".prediction-result");
const featuresForm = document.querySelector("form");

featuresForm.addEventListener("submit", e => {
    e.preventDefault();
    let data = new FormData(e.currentTarget);
    data = Object.fromEntries(data.entries());
    for (key in data) {
        data[key] = Number(data[key]);
    }

    fetch("/predict_price", {
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data),
        method: "POST"
    })
        .then(data => data.json())
        .then(predicted_price => {
            console.log(predicted_price);
            predictionResult.textContent = `Predicted Price: $${predicted_price.value}`;
        })
        .catch(err => {
            predictionResult.textContent = `...`;
            console.log(err);
        });
});

anime
    .timeline({ loop: true })
    .add({
        targets: ".ml3 .letter",
        opacity: [0, 1],
        easing: "easeInOutQuad",
        duration: 2250,
        delay: (el, i) => 150 * (i + 1)
    })
    .add({
        targets: ".ml3",
        opacity: 0,
        duration: 1000,
        easing: "easeOutExpo",
        delay: 1000
    });

// For .ml2 animation
var textWrapper2 = document.querySelector(".ml2");
textWrapper2.innerHTML = textWrapper2.textContent.replace(/\S/g, "<span class='letter'>$&</span>");

anime
    .timeline({ loop: true })
    .add({
        targets: ".ml2 .letter",
        scale: [4, 1],
        opacity: [0, 1],
        translateZ: 0,
        easing: "easeOutExpo",
        duration: 950,
        delay: (el, i) => 70 * i
    })
    .add({
        targets: ".ml2",
        opacity: 0,
        duration: 1000,
        easing: "easeOutExpo",
        delay: 1000
    });

const slider = document.querySelector(".slider");
const sliderItems = document.querySelectorAll(".care");
const leftButton = document.querySelector(".left-button");
const rightButton = document.querySelector(".right-button");

let currentIndex = 0;

function slideTo(index) {
    if (index < 0) index = sliderItems.length - 1;
    if (index >= sliderItems.length) index = 0;

    currentIndex = index;

    const offset = -currentIndex * (sliderItems[0].offsetWidth + 20); /* Adjust the card spacing (margin) */
    slider.style.transform = `translateX(${offset}px)`;
}

leftButton.addEventListener("click", () => {
    slideTo(currentIndex - 1);
});

rightButton.addEventListener("click", () => {
    slideTo(currentIndex + 1);
});

slideTo(currentIndex); // Initial slide

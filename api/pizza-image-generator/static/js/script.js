document.addEventListener("DOMContentLoaded", function() {
    const generatePizzasButton = document.getElementById("generate-button");
    const slider = document.getElementById("slider");
    const sliderValue = document.getElementById("image-size-label");

    slider.oninput = function() {
        sliderValue.innerText = slider.value + "x" + slider.value;
    };

    generatePizzasButton.addEventListener("click", () => {
        fetch("/generate_images?image_size=" + slider.value)
            .then(response => response.json())
            .then(data => {
                const images = data.images;
                const imagesContainer = document.getElementById("image-grid");
                imagesContainer.innerHTML = "";

                images.forEach(image => {
                    const img = new Image();
                    img.src = `data:image/png;base64,${image}`;
                    img.classList.add("generated-image");
                    imagesContainer.appendChild(img);
                })
            })
    });
});

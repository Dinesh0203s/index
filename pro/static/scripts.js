document.addEventListener("DOMContentLoaded", function() {
    const selfieInput = document.getElementById("selfie");
    const groupPhotosInput = document.getElementById("group_photos");
    const selfiePreview = document.getElementById("selfie-preview");
    const groupPhotosPreview = document.getElementById("group-photos-preview");

    selfieInput.addEventListener("change", function() {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(event) {
                selfiePreview.src = event.target.result;
                selfiePreview.style.display = "block";
            };
            reader.readAsDataURL(file);
        }
    });

    groupPhotosInput.addEventListener("change", function() {
        groupPhotosPreview.innerHTML = ""; // Clear previous previews
        Array.from(this.files).forEach(file => {
            const reader = new FileReader();
            reader.onload = function(event) {
                const img = document.createElement("img");
                img.src = event.target.result;
                img.classList.add("group-photo-preview");
                groupPhotosPreview.appendChild(img);
            };
            reader.readAsDataURL(file);
        });
    });
});

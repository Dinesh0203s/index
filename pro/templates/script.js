document.getElementById('uploadBtn').addEventListener('click', () => {
    const fileInput = document.getElementById('fileInput');
    const files = fileInput.files;
    
    if (files.length === 0) {
        alert('Please select files.');
        return;
    }
    
    const formData = new FormData();
    for (let i = 0; i < files.length; i++) {
        formData.append('files', files[i]);
    }
    
    fetch('http://localhost:5000/filter', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        displayImages(data.selfies, 'filteredPhotos');
        displayImages(Array.from(files).map(file => URL.createObjectURL(file)), 'uploadedPhotos');
    })
    .catch(error => console.error('Error:', error));
});

function displayImages(imagePaths, elementId) {
    const gallery = document.getElementById(elementId);
    gallery.innerHTML = '';
    imagePaths.forEach(src => {
        const img = document.createElement('img');
        img.src = src;
        gallery.appendChild(img);
    });
}

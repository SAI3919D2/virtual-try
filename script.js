document.getElementById('tryOnButton').addEventListener('click', () => {
    const fileInput = document.getElementById('upload');
    if (fileInput.files.length > 0) {
        const file = fileInput.files[0];
        const img = document.createElement('img');
        img.src = URL.createObjectURL(file);
        img.style.maxWidth = '300px';
        document.getElementById('result').innerHTML = '';
        document.getElementById('result').appendChild(img);
    } else {
        alert('Please upload an image!');
    }
});

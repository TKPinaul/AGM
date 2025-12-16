document.addEventListener('DOMContentLoaded', function() {
    const profileImageContainer = document.querySelector('.profile-image-container');
    const profileImageInput = document.getElementById('profile-image-input');
    const profileImage = document.querySelector('.profile-image');

    profileImageContainer.addEventListener('click', function() {
        profileImageInput.click();
    });

    profileImageInput.addEventListener('change', function(event) {
        const selectedFile = event.target.files[0];

        if (selectedFile) {
            const reader = new FileReader();
            reader.onload = function(e) {
                profileImage.src = e.target.result;

                // Videz la valeur de l'input file pour permettre la sélection de la même image
                profileImageInput.value = '';
            };
            reader.readAsDataURL(selectedFile);
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    var boutonRetour = document.getElementById('btn-retour');

    boutonRetour.addEventListener('click', function() {
        window.history.back();
    });
});
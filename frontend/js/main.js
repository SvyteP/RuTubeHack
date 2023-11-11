document.getElementById('upload-form').addEventListener('submit', function(e) {
   e.preventDefault();

   let formData = new FormData(this);

   fetch('!!!апи для аплоуда!!!', {
       method: 'POST',
       body: formData
   }).then(response => {
       if (response.ok) {
           return response.json();
       } else {
           throw new Error('Ошибка загрузки видео');
       }
   }).then(data => {
       document.getElementById('original-video').src = data.videoUrl;
   }).catch(error => {
       console.error(error);
   });
});

document.getElementById('translate-button').addEventListener('click', function() {
   let videoUrl = document.getElementById('original-video').src;

   fetch('!!!апишник для транслейта!!!', {
       method: 'POST',
       headers: {
           'Content-Type': 'application/json'
       },
       body: JSON.stringify({ videoUrl: videoUrl })
   }).then(response => {
       if (response.ok) {
           return response.json();
       } else {
           throw new Error('Ошибка перевода видео');
       }
   }).then(data => {
       document.getElementById('translated-video').src = data.translatedVideoUrl;
   }).catch(error => {
       console.error(error);
   });
});
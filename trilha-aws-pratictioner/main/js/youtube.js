const sidebar = document.getElementById('sidebar');
const videoPlayer = document.getElementById('videoPlayer');
const videoFrame = document.getElementById('videoFrame');
const tituloVideo = document.getElementById('tituloVideo');
const contador = document.getElementById('contador');

const items = document.querySelectorAll('.playlist-item');

const videos = Array.from(items).map(item => ({
  src: item.dataset.video,
  titulo: item.dataset.titulo
}));

let assistidos = JSON.parse(localStorage.getItem('assistidos')) || [];
let atual = 0;

function atualizarContador() {
  contador.textContent = assistidos.length;
}

function carregarVideo(index) {
  atual = index;
  const video = videos[index];
  tituloVideo.textContent = video.titulo;

  const isYouTube = video.src.includes('youtu');

  if (isYouTube) {
    // Extrai o ID do vídeo
    const videoId = video.src.includes('watch?v=') 
      ? video.src.split('v=')[1].split('&')[0] 
      : video.src.split('/').pop().split('?')[0];

    videoFrame.src = `https://www.youtube.com/embed/${videoId}`;
    videoFrame.style.display = 'block';
    videoPlayer.style.display = 'none';
    videoPlayer.pause();
    videoPlayer.removeAttribute('src');
  } else {
    videoPlayer.src = video.src;
    videoPlayer.style.display = 'block';
    videoFrame.style.display = 'none';
    videoFrame.removeAttribute('src');
    videoPlayer.play();
  }
}

function marcarConcluido() {
  const src = videos[atual].src;
  if (!assistidos.includes(src)) {
    assistidos.push(src);
    localStorage.setItem('assistidos', JSON.stringify(assistidos));
    document.querySelectorAll('.playlist-item').forEach(item => {
      if (item.dataset.video === src) {
        item.classList.add('assistido');
      }
    });
    atualizarContador();
  }
}

function proximo() {
  if (atual < videos.length - 1) {
    carregarVideo(atual + 1);
  }
}

function voltar() {
  if (atual > 0) {
    carregarVideo(atual - 1);
  }
}

function toggleSidebar() {
  sidebar.classList.toggle('open');
}

// Eventos da playlist
items.forEach((item, index) => {
  item.addEventListener('click', () => {
    carregarVideo(index);
  });

  if (assistidos.includes(item.dataset.video)) {
    item.classList.add('assistido');
  }
});

// Inicialização
carregarVideo(0);
atualizarContador();

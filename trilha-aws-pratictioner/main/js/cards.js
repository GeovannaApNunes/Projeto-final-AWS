function filtrarCards(categoria) {
    // Seleciona todos os cards
    let cards = document.querySelectorAll('.card');
    
    // Se a categoria for 'todos', mostra todos os cards
    if (categoria === 'todos') {
        cards.forEach(card => {
            card.style.display = 'block'; // ou 'flex', dependendo do seu layout
        });
    } else {
        // Filtra os cards de acordo com a categoria
        cards.forEach(card => {
            if (card.classList.contains(categoria)) {
                card.style.display = 'block'; // Exibe os cards correspondentes
            } else {
                card.style.display = 'none'; // Esconde os outros cards
            }
        });
    }
}

// Função para girar o card
function flipCard(card) {
  const cardInner = card.querySelector('.card-inner');
  
  // Se o card já estiver virado, viramos de volta
  if (cardInner.style.transform === "rotateY(180deg)") {
      cardInner.style.transform = "rotateY(0deg)";
  } else {
      // Viramos o card clicado
      cardInner.style.transform = "rotateY(180deg)";
  }
}



// Função que filtra os cards
function filterCards() {
  const searchQuery = document.getElementById('search-bar').value.toLowerCase();
  const cards = document.querySelectorAll('.card');

  cards.forEach(card => {
      const titleText = card.querySelector('.card-front h2') ? card.querySelector('.card-front h2').textContent.toLowerCase() : '';
      const descriptionText = card.querySelector('.card-front p') ? card.querySelector('.card-front p').textContent.toLowerCase() : '';
      
      // Se a pesquisa estiver vazia, mostra todos os cards
      if (searchQuery === "" || titleText.includes(searchQuery) || descriptionText.includes(searchQuery)) {
          card.style.display = 'inline-flex';  // Exibe o card com flexbox
      } else {
          card.style.display = 'none';  // Oculta o card
      }
  });
}
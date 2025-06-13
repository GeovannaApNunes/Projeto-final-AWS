// script.js

const form = document.getElementById('material-form');
const grid = document.getElementById('material-grid');
const feedback = document.getElementById('feedback');
const searchInput = document.getElementById('search');

let materiais = JSON.parse(localStorage.getItem('materiais')) || [];

function renderMateriais(filtro = '') {
  grid.innerHTML = '';

  const filtrados = materiais.filter(mat =>
    mat.titulo.toLowerCase().includes(filtro.toLowerCase()) ||
    mat.descricao.toLowerCase().includes(filtro.toLowerCase()) ||
    mat.categoria.toLowerCase().includes(filtro.toLowerCase())
  );

  if (filtrados.length === 0) {
    grid.innerHTML = '<p>Nenhum material encontrado.</p>';
    return;
  }

  filtrados.forEach((mat, index) => {
    const card = document.createElement('div');
    card.className = 'card';

    card.innerHTML = `
      <span class="categoria">${mat.categoria}</span>
      <h3>${mat.titulo}</h3>
      <p>${mat.descricao || 'Sem descrição.'}</p>
      <a href="${mat.link}" target="_blank">Acessar →</a>
      <div class="actions">
        <button onclick="editMaterial(${index})"><i class="ph ph-pencil"></i></button>
        <button onclick="removeMaterial(${index})"><i class="ph ph-trash"></i></button>
      </div>
    `;

    grid.appendChild(card);
  });
}

function addMaterial(material) {
  materiais.push(material);
  saveMateriais();
  renderMateriais();
  showFeedback('Material adicionado!');
}

function removeMaterial(index) {
  materiais.splice(index, 1);
  saveMateriais();
  renderMateriais(searchInput.value);
  showFeedback('Material removido!');
}

function editMaterial(index) {
  const mat = materiais[index];
  const titulo = prompt('Editar título:', mat.titulo);
  if (!titulo) return;
  const link = prompt('Editar link:', mat.link);
  if (!link) return;
  const descricao = prompt('Editar descrição:', mat.descricao);
  if (descricao === null) return;
  const categoria = prompt('Editar categoria:', mat.categoria);
  if (!categoria) return;

  materiais[index] = { titulo, link, descricao, categoria };
  saveMateriais();
  renderMateriais(searchInput.value);
  showFeedback('Material editado!');
}

function saveMateriais() {
  localStorage.setItem('materiais', JSON.stringify(materiais));
}

function showFeedback(msg) {
  feedback.textContent = msg;
  setTimeout(() => feedback.textContent = '', 2000);
}

form.addEventListener('submit', e => {
  e.preventDefault();
  const titulo = form.titulo.value.trim();
  const link = form.link.value.trim();
  const descricao = form.descricao.value.trim();
  const categoria = form.categoria.value;

  if (!titulo || !link || !categoria) {
    showFeedback('Preencha todos os campos!');
    return;
  }

  addMaterial({ titulo, link, descricao, categoria });
  form.reset();
});

searchInput.addEventListener('input', e => {
  renderMateriais(e.target.value);
});

renderMateriais();

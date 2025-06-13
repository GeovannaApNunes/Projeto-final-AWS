let totalItens = 0;
let itensConcluidos = 0;

function adicionarMeta() {
  const input = document.getElementById('metaInput');
  const metaTexto = input.value.trim();
  if (metaTexto === '') return;

  const li = document.createElement('li');

  const checkbox = document.createElement('input');
  checkbox.type = 'checkbox';
  checkbox.addEventListener('change', atualizarProgresso);

  const span = document.createElement('span');
  span.textContent = metaTexto;

  // Botão para adicionar submeta
  const botaoSubmeta = document.createElement('button');
  botaoSubmeta.textContent = 'Adicionar Submeta';
  botaoSubmeta.addEventListener('click', function() {
    adicionarSubmeta(li);
  });

  li.appendChild(checkbox);
  li.appendChild(span);
  li.appendChild(botaoSubmeta);

  // Sublista de submetas
  const subLista = document.createElement('ul');
  li.appendChild(subLista);

  document.getElementById('metaList').appendChild(li);

  totalItens++;
  atualizarProgresso();
  input.value = '';
}

function adicionarSubmeta(metaLi) {
  const submetaTexto = prompt('Digite a submeta:');
  if (!submetaTexto) return;

  const subLi = document.createElement('li');

  const subCheckbox = document.createElement('input');
  subCheckbox.type = 'checkbox';
  subCheckbox.addEventListener('change', atualizarProgresso);

  const subSpan = document.createElement('span');
  subSpan.textContent = submetaTexto;

  subLi.appendChild(subCheckbox);
  subLi.appendChild(subSpan);

  metaLi.querySelector('ul').appendChild(subLi);

  totalItens++;
  atualizarProgresso();
}

function atualizarProgresso() {
  const checkboxes = document.querySelectorAll('#metaList input[type="checkbox"]');
  const checked = Array.from(checkboxes).filter(cb => cb.checked).length;

  const total = checkboxes.length;
  const progresso = total === 0 ? 0 : Math.round((checked / total) * 100);

  document.getElementById('progress-bar').style.width = progresso + '%';
  document.getElementById('progressoText').textContent = `${progresso}% Concluído`;
}

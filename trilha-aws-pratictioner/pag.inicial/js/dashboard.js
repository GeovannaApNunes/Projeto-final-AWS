// Elementos da barra de progresso
const progressBar = document.getElementById('progress-bar');
const progressoText = document.getElementById('progressoText');

// Função para adicionar metas
function adicionarMeta() {
    const metaInput = document.getElementById('metaInput');
    const metaText = metaInput.value.trim();

    if (metaText) {
        const li = document.createElement('li');
        li.innerHTML = `<input type="checkbox" onclick="updateProgress()"> ${metaText}`;
        document.getElementById('metaList').appendChild(li);
        metaInput.value = '';
        updateProgress();
    }
}

// Função que atualiza a barra de progresso
function updateProgress() {
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    const total = checkboxes.length;
    const marcados = Array.from(checkboxes).filter(checkbox => checkbox.checked).length;

    const progresso = total > 0 ? (marcados / total) * 100 : 0;
    progressBar.style.width = progresso + '%';
    progressoText.textContent = Math.round(progresso) + '% Concluído';
}

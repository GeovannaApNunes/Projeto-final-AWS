// Seleção do Card
const teamMembers = document.querySelectorAll('.team-member');

teamMembers.forEach(member => {
    member.addEventListener('click', () => {
        // Se o card já estiver ativo, remover a classe "active"
        if (member.classList.contains('active')) {
            member.classList.remove('active');
        } else {
            // Remover "active" de todos os cards
            teamMembers.forEach(member => {
                member.classList.remove('active');
            });
            // Adicionar "active" ao card clicado
            member.classList.add('active');
        }
    });
});


const button = document.getElementById("toggle-theme");
const body = document.body;

button.addEventListener("click", () => {
    body.classList.toggle("dark-mode");

    if (body.classList.contains("dark-mode")) {
        button.innerHTML = "☀"; // Muda para sol
    } else {
        button.innerHTML = "🌙"; // Muda para lua
    }
});
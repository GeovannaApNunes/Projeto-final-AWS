// Obtém os elementos do DOM
const emailInput = document.getElementById('email');
const loginButton = document.getElementById('loginBtn');

// Adiciona um ouvinte de evento para o botão de login com email
loginButton.addEventListener('click', () => {
    const email = emailInput.value;

    // Validação básica do e-mail
    if (isValidEmail(email)) {
        alert('Login com e-mail bem-sucedido!'); // Substitua com o redirecionamento ou funcionalidade desejada
        emailInput.value = ''; // Limpa o campo de e-mail
    } else {
        alert('Por favor, insira um e-mail válido.');
    }
});

// Função para validar o e-mail
function isValidEmail(email) {
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailPattern.test(email);
}


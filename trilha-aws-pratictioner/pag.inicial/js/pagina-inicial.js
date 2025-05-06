const ctx = document.getElementById('graficoAWS').getContext('2d');
new Chart(ctx, {
  type: 'pie',
  data: {
    labels: [
      'Conceitos da Nuvem (24%)',
      'Segurança e Conformidade (30%)',
      'Tecnologia e Serviços da Nuvem (34%)',
      'Cobrança, Preços e Suporte (12%)'
    ],
    datasets: [{
      data: [24, 30, 34, 12],
      backgroundColor: ['#4c72b0', '#55a868', '#c44e52', '#8172b2'],
      borderColor: '#fff',
      borderWidth: 2
    }]
  },
  options: {
    responsive: true,
    plugins: {
      legend: {
        position: 'bottom'
      },
      title: {
        display: false
      }
    }
  }
});
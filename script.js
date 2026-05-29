// Selectors
const container = document.querySelector('.seat-grid');
const count = document.getElementById('count');
const total = document.getElementById('total');

// Busca os assentos diretamente da API Flask
async function carregarAssentos() {
  const resposta = await fetch('http://localhost:5000/api/assentos');
  const assentos = await resposta.json();

  const elementosAssentos = document.querySelectorAll('.seat');

  // Atualiza a interface com os dados vindos do servidor
  elementosAssentos.forEach((elemento, index) => {
    const assento = assentos[index];

    if (!assento) return;

    elemento.setAttribute('data-codigo', assento.codigo);
    elemento.setAttribute('data-price', assento.preco);

    elemento.classList.remove('unavailable');
    elemento.classList.remove('selected');

    if (assento.status === 'RESERVADO') {
      elemento.classList.add('unavailable');
    }
  });

  updateSelectedCount();
}

// Atualiza quantidade selecionada e valor total
function updateSelectedCount() {
  const selectedSeats = document.querySelectorAll('.seat.selected');
  const selectedSeatsCount = selectedSeats.length;

  const totalPrice = Array.from(selectedSeats).reduce((total, seat) => {
    return total + parseFloat(seat.getAttribute('data-price'));
  }, 0);

  count.innerText = selectedSeatsCount;
  total.innerText = totalPrice;
}

// Permite selecionar apenas assentos disponíveis
container.addEventListener('click', (e) => {
  if (e.target.classList.contains('seat') && !e.target.classList.contains('unavailable')) {
    e.target.classList.toggle('selected');
    updateSelectedCount();
  }
});

// Carrega os assentos ao abrir a página
carregarAssentos();

// Seleciona o botão de reserva
const botaoReservar = document.getElementById('reservar');

// Envia os assentos selecionados para a API
botaoReservar.addEventListener('click', async () => {
  const selecionados = document.querySelectorAll('.seat.selected');

  const assentos = Array.from(selecionados).map(seat =>
    seat.getAttribute('data-codigo')
  );

  if (assentos.length === 0) {
    alert('Selecione pelo menos um assento');
    return;
  }

  const resposta = await fetch('http://localhost:5000/api/reservas', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      assentos: assentos
    })
  });

  const resultado = await resposta.json();

  alert(resultado.mensagem || resultado.erro);

  carregarAssentos();
});
const form = document.getElementById('escolheSala');




async function LoadRooms() {
    //TODO Busca resposta do forms
    
}



form.addEventListener('submit', async (event) => {
    event.preventDefault(); // Evita o reload da página
    
    // Recupera o valor do input
    const sala = parseInt(document.getElementById('salas').value);
    
    try {
        
        const resposta = await fetch(`http://localhost:5000/api/get_list?num=${sala}`); //TODO vamos precisar trocar isso pra uma variavel com o IP onde o servidor ta rodando
        const html = await resposta.text();
        console.log(html)
        
        document.getElementById('resultado').innerHTML = 
            html
            //JSON.stringify(usuario, null, 2);
    } catch (error) {
        console.error('Erro:', error);
    }
});
const form = document.getElementById('escolheSala');
const botaoSoma = document.getElementById('botaoSoma');
const botaoTira = document.getElementById('botaoTira')




async function LoadRooms(html) {
    document.getElementById('resultado').innerHTML = 
        html
    
}



form.addEventListener('submit', async (event) => {
    event.preventDefault(); // Evita o reload da página
    
    // Recupera o valor do input
    const sala = parseInt(document.getElementById('salas').value);
    
    try {
        
        const resposta = await fetch(`http://localhost:5000/api/get_list?num=${sala}`); //TODO vamos precisar trocar isso pra uma variavel com o IP onde o servidor ta rodando
        const dados = await resposta.json();
        html = dados[0]
        
        LoadRooms(html)
        
    } catch (error) {
        console.error('Erro:', error);
    }
});

botaoSoma.addEventListener('click', async(event)=>{
    const sala = parseInt(document.getElementById('salas').value)

    try {
        const resposta1 = await fetch(`http://localhost:5000/api/add_seat?num=${sala}`, {
            method: 'POST'
        });
        const resposta2 = await fetch(`http://localhost:5000/api/get_list?num=${sala}`);
        const dados = await resposta2.json();
        html = dados[0]
        console.log(await resposta1.json())

        LoadRooms(html)


    } catch (error) {
        console.error('Erro:', error);
    }
});
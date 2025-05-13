const paises = [
  { nome: "Brasil", bandeira: "https://flagcdn.com/w320/br.png", info: "Capital: Brasília\nPopulação: 213 milhões" },
  { nome: "França", bandeira: "https://flagcdn.com/w320/fr.png", info: "Capital: Paris\nPopulação: 67 milhões" },
  { nome: "Japão", bandeira: "https://flagcdn.com/w320/jp.png", info: "Capital: Tóquio\nPopulação: 125 milhões" },
  { nome: "Alemanha", bandeira: "https://flagcdn.com/w320/de.png", info: "Capital: Berlim\nPopulação: 83 milhões" },
  { nome: "Canadá", bandeira: "https://flagcdn.com/w320/ca.png", info: "Capital: Ottawa\nPopulação: 38 milhões" },
  { nome: "Austrália", bandeira: "https://flagcdn.com/w320/au.png", info: "Capital: Canberra\nPopulação: 26 milhões" },
  { nome: "Argentina", bandeira: "https://flagcdn.com/w320/ar.png", info: "Capital: Buenos Aires\nPopulação: 45 milhões" },
  { nome: "China", bandeira: "https://flagcdn.com/w320/cn.png", info: "Capital: Pequim\nPopulação: 1,4 bilhão" },
  { nome: "Estados Unidos", bandeira: "https://flagcdn.com/w320/us.png", info: "Capital: Washington, D.C.\nPopulação: 331 milhões" },
  { nome: "Itália", bandeira: "https://flagcdn.com/w320/it.png", info: "Capital: Roma\nPopulação: 60 milhões" }
];

let pontuacaoMaxima = 0;
let pontuacao = 0;
let perguntaAtual = 0;
let paisesEmbaralhados = [];

const app = document.getElementById('app');

function limparTela() {
  app.innerHTML = '';
}

function telaInicial() {
  limparTela();

  const titulo = document.createElement('h1');
  titulo.textContent = "🌎 InfoCountry";
  app.appendChild(titulo);

  const pontuacaoTexto = document.createElement('p');
  pontuacaoTexto.textContent = `🏆 Maior pontuação: ${pontuacaoMaxima}`;
  app.appendChild(pontuacaoTexto);

  const botaoJogar = document.createElement('button');
  botaoJogar.textContent = "▶️ Jogar";
  botaoJogar.onclick = iniciarQuiz;
  app.appendChild(botaoJogar);

  const botaoInfo = document.createElement('button');
  botaoInfo.textContent = "ℹ️ Informações dos Países";
  botaoInfo.onclick = mostrarInfos;
  app.appendChild(botaoInfo);
}

function iniciarQuiz() {
  pontuacao = 0;
  perguntaAtual = 0;
  paisesEmbaralhados = paises.sort(() => Math.random() - 0.5);
  mostrarPergunta();
}

function mostrarPergunta() {
  limparTela();

  if (perguntaAtual >= paisesEmbaralhados.length) {
    mostrarResultado();
    return;
  }

  const pais = paisesEmbaralhados[perguntaAtual];

  const img = document.createElement('img');
  img.src = pais.bandeira;
  img.width = 300;
  img.height = 200;
  app.appendChild(img);

  const pergunta = document.createElement('p');
  pergunta.textContent = "De qual país é esta bandeira?";
  app.appendChild(pergunta);

  const input = document.createElement('input');
  input.id = "resposta";
  app.appendChild(input);

  const botao = document.createElement('button');
  botao.textContent = "Responder";
  botao.onclick = verificarResposta;
  app.appendChild(botao);
}

function verificarResposta() {
  const input = document.getElementById("resposta");
  const resposta = input.value.trim().toUpperCase();
  const correta = paisesEmbaralhados[perguntaAtual].nome.toUpperCase();

  if (resposta === correta) {
    pontuacao += 1;
  }

  perguntaAtual += 1;
  mostrarPergunta();
}

function mostrarResultado() {
  limparTela();

  if (pontuacao > pontuacaoMaxima) {
    pontuacaoMaxima = pontuacao;
  }

  const resultado = document.createElement('h2');
  resultado.textContent = `Você acertou ${pontuacao} de ${paises.length}!`;
  app.appendChild(resultado);

  const botao = document.createElement('button');
  botao.textContent = "Voltar ao Início";
  botao.onclick = telaInicial;
  app.appendChild(botao);
}

function mostrarInfos() {
  limparTela();

  const titulo = document.createElement('h2');
  titulo.textContent = "📘 Informações dos Países";
  app.appendChild(titulo);

  const container = document.createElement('div');
  container.style.textAlign = "left";
  container.style.maxHeight = "400px";
  container.style.overflowY = "scroll";
  container.style.border = "1px solid #ccc";
  container.style.padding = "10px";
  container.style.backgroundColor = "#fff";

  paises.forEach(pais => {
    const info = document.createElement('p');
    info.innerText = `🌍 ${pais.nome}\n${pais.info}`;
    container.appendChild(info);
  });

  app.appendChild(container);

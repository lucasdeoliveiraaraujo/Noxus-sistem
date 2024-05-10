function  bloquearBotao(botao){
    document.getElementById(botao).disabled = true
    sessionStorage.setItem("botaoValor", document.getElementById(botao).innerHTML.trim())
    document.getElementById(botao).innerHTML = `<div class="spinner-grow text-dark" role="status">
                                                  <span class="visually-hidden">Aguarde...</span>
                                                </div>`
}

function desbloquearBotao(botao){
    document.getElementById(botao).disabled = false
    document.getElementById(botao).innerHTML = sessionStorage.getItem("botaoValor") ?? document.getElementById(botao).innerHTML
}
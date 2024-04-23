const obterCookie= (valor)=>{
    return document.cookie.split("=")[document.cookie.split("=").indexOf(valor) + 1]
}

const construirDados = (identificador) =>{
    let jsonEnvio = {}
    document.querySelectorAll(`${identificador}`).forEach(json => {
        jsonEnvio[json.name] = json.value
    })

    return jsonEnvio
}

const realizarRequisicao= async({origemRequisicao,conteudoRequisicao,tipoRequisicao})=>{
  let dadosEnvio = {
    url: origemRequisicao,
    options: {
        method: tipoRequisicao,
        headers: {
            "X-CSRFToken": obterCookie("csrftoken"),
            "Content-Type": "application/json",
        }
    }
  }

   
  if(tipoRequisicao.toUpperCase() !== "GET"){
    dadosEnvio.options.body =  JSON.stringify(conteudoRequisicao)
  }
  
  let requisicao = await fetch(dadosEnvio.url,dadosEnvio.options)
  if(requisicao.ok){
    return requisicao
  }else{
    document.querySelector("#notificacao").innerHTML = 
      toastr({
        theme:"danger",
        title:"Falha ao requisitar",
        message:"Requisição inválida, tente novamente mais tarde. Caso o erro persista verifique a sua conexão com a internet"
      })

    $('#toast').toast('show')

    return {ok:requisicao.ok}
  }

}
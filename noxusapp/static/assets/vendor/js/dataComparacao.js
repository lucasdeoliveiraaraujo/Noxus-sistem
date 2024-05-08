const entreDatas = (dataInitGlobal,dataFimGlobal,data) =>{
    let aux = dataInitGlobal.value.split("-")
    let dataInicialGlobal = negetw Date(aux[0],aux[1]-1,aux[2])
    aux = dataFimGlobal.value.split("-")
    let dataFinalGlobal = new Date(aux[0],aux[1]-1,aux[2])
    aux = data.value.split("-")
    let dataInicial = new Date(aux[0],aux[1]-1,aux[2])
   
    if ( dataInicial.getTime() >= dataInicialGlobal.getTime() && dataInicial.getTime() <= dataFinalGlobal.getTime()) return true 
    return false
}
const entradaTextoValidar = (entradas) =>{
    let validador = []
    entradas.forEach(i => {
        if (i.value.trim() == "") validador.push({campo:i,descricao:i.title})
    });
    return validador
}

const emailValidar = (entradas) =>{
    let re = /\S+@\S+\.\S+/
    let validador = entradas.filter(el=>{
        return !re.test(el.value)
    })
    return validador
}
const validarSeletor = (seletores,termoGenerico = "Selecione") =>{
    const validador = []
    seletores.forEach(i =>{       
        if (i.value.trim() == "" || i.selectedOptions[0].innerHTML.trim().replaceAll("\n","").indexOf(termoGenerico) == 0) validador.push({campo:i,descricao:i.title})        
    })

    return validador
}
function adicionarItem(valor){
    const atual = document.getElementById('visor').value
    document.getElementById('visor').value = `${atual} ${valor}`
}
function limpar(){
    document.getElementById('visor').value = ""
}
function calcular(){
    const expressao = document.getElementById('visor').value
    const resultado = eval(expressao)
    document.getElementById('visor').value = resultado
}
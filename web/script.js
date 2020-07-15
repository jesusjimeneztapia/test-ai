const restApi = 'http://localhost:5010/api/books'

const showBook = document.getElementById('book')
const infoBook = document.getElementById('info')
const containerSearch = document.getElementsByClassName('container-search')[0]

function search(element) {
    const {value} = element
    var info = `<h1>Cargando...</h1>`
    element.value = 1
    infoBook.innerHTML = info
    containerSearch.classList.toggle('invisible')
    showBook.classList.toggle('invisible')
    fetch(`${restApi}/${value}`)
        .then(response => response.json())
        .then(({status, message, ...rest}) => {
            info = ''
            if (status === undefined) {
                for (const property in rest) {
                    info += `<p><strong>${property}: </strong>${rest[property]}</p>`
                }
            } else {
                info = `<h3><strong><span>${message}</span></strong></h3>`
            }
        })
        .catch(error => console.error(error))
        .finally(() => {
            infoBook.innerHTML = info
        })
}

function returnSearch() {
    showBook.classList.toggle('invisible')
    containerSearch.classList.toggle('invisible')
}
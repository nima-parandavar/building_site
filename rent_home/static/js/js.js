var price = document.getElementById('price')
price.addEventListener('change', displayPrice)

function displayPrice(){
    document.getElementById('priceDisplay').innerHTML = price.value + '$'
}
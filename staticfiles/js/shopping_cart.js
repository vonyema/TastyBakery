const updateButton= document.getElementsByClassName("update-cart")

for (let i=0; i < updateButton.length; i++){
    updateButton[i].addEventListener('click', function(){
        const bakedgoodId= this.dataset.bakedgood
        const action= this.dataset.action
        console.log('bakedgoodId:', bakedgoodId, 'action:', action)

        console.log('User:',user)
        if(user=='AnonymousUser'){
            alert('Must log in to continue!');
        }else{
            addToUserCart(bakedgoodId, action)
            alert('Added to cart')
        }
    })
}
function addToUserCart (bakedgoodId, action){
    var url='/add_order/'
    fetch(url, {
        method: 'POST',
        header:{
            'Content-Type':'application/json',
        },
        body:JSON.stringify({'bakedgoodId': bakedgoodId, 'action' : action})
    })
    .then((response)=>{
        return response.text();
    })
    .then((data)=>{
        console.log('data:', data)
    });
}
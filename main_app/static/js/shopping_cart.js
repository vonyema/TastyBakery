const updateButton= document.getElementsByClassName("update-cart")

for (let i=0; i < updateButton.length; i++){
    updateButton[i].addEventListener('click', function(){
        const bakedgoodId= this.dataset.bakedgood
        const action= this.dataset.action
        console.log('bakedgoodId:', bakedgoodId, 'action:', action)

        console.log('User:',user)
        if(user=='AnonymousUser'){
            console.log('Not logged in');
        }else{
            addToUserCart(bakedgoodId, action)
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
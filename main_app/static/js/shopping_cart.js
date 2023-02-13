const updateButton= document.getElementsByClassName("update-cart")

for (let i=0; i< updateButton.length; i++){
    updateButton[i].addEventListener('click', function(){
        const bakedgoodId= this.dataset.bakedgood
        const action= this.dataset.action
        console.log('bakedgoodId:', bakedgoodId, 'action:', action)

        console.log('User:',user)
        if(user=='AnonymousUser'){
            console.log('Not logged in');
        }else{
            console.log('User logged in');
        }
    })
}
function addToUserCart (bakedgoodId, action){
    const url='/add_order/'
    fetch (url, {
        method: 'POST',
        header:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'bakedgoodId': bakedgoodId, 'action' : action})
    })
    .then((response)=>{
        return response.json();
    })
    .then((data)=>{
        console.log('data:', data)
        location.reload()
    });
}
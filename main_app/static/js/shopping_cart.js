const updateButton= document.getElementsByClassName("update-cart")

for (let i=0; i< updateButton.length; i++){
    updateButton[i].addEventListener('click', function(){
        const bakedgoodId= this.dataset.bakedgood
        const action= this.dataset.action
        console.log('bakedgoodId:', bakedgoodId, 'action:', action)
    })
}
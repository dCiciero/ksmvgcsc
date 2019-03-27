document.addEventListener('DOMContentLoaded', () => {
    // alert('Welcome')
    caption = document.querySelector('#photoCaption');
    options = document.querySelector('#galleryOptionsWrapper');
    captionText = document.querySelector('#txtcaption');
    file = document.querySelector('#txtFileUpload');
    caption.style.display = "none";
    options.style.display = "none";
    
    let pageSel = document.querySelector('#gallerySelection');
    let optSel = document.querySelector('#galleryOptions');
    let btnUpload = document.querySelector('#btnUpload')
    // optSel.onchange = () =>{
    //     console.log(optSel.value)
    // }
    pageSel.value = 1
    caption.style.display = "block";
    pageSel.onchange = ()=>{
        if (pageSel.value == 1)
            caption.style.display = "block";
        else
            caption.style.display = "none";
            options.style.display = "block";
    }

    btnUpload.onclick = (e) => {
        e.preventDefault();
        alert(optSel.value + ' '+ pageSel.value)
        alert(captionText.innerText + ' '+ file.value)
    }

    function uploadImage(){
        const req = new XMLHttpRequest();
        req.open("POST", "/uploads");
        req.onload = () => {

        }
        const data = FormData();

        data.append('gallerySelection', getGallerySelection)
        data.append('gallerySelection', getGallerySelection)

        req.send(data)
    }
    



})
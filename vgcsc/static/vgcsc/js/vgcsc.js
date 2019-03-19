document.addEventListener('DOMContentLoaded', () => {
    // alert('Welcome')
    caption = document.querySelector('#photoCaption');
    console.log(caption)
    
    
    let optSel = document.querySelector('#gallerySelection');
    console.log('test: ' + optSel.text)
    optSel.onchange = ()=>{
        if (optSel.value == 1)
            caption.style.display = "block";
        else
            caption.style.display = "none";
    }
})
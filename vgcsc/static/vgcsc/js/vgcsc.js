document.addEventListener('DOMContentLoaded', () => {
    // alert('Welcome')
    caption = document.querySelector('#photoCaption');
    options = document.querySelector('#galleryOptionsWrapper');
    captionText = document.querySelector('#txtcaption');
    file = document.querySelector('#txtFileUpload');
    caption.style.display = "none";
    options.style.display = "none";
    
    let gallerySection = document.querySelector('#gallerySelection'); //gets the gallery section's dropdown
    let galleryOptions = document.querySelector('#galleryOptions'); //gets the galler option's dropdown
    let btnUpload = document.querySelector('#btnUpload')
    let alert_box = document.querySelector('.alert')
    let setupScreen = document.querySelector('#setupScreen');
    // galleryOptions.onchange = () =>{
    //     console.log(galleryOptions.value)
    // }
    gallerySection.value = 1
    caption.style.display = "block";
    gallerySection.onchange = ()=>{
        if (gallerySection.value == 1)
        {
            caption.style.display = "block";
            options.style.display = "none";
        }
        else
        {
            caption.style.display = "none";
            options.style.display = "block";
        }
    }

    // document.querySelector('#frm-upload').onsubmit = () => {
    //     alert("form submitted");
    //     console.log("Form Submitted");
    // }

    btnUpload.onclick = (e) => {
         //e.preventDefault();
        // alert(galleryOptions.value + ' '+ gallerySection.value)
        // alert(captionText.innerText + ' '+ file.value)
        // setTimeout(()=>{
        //     alert("OK");
            
        // },3000)
        //alert("After")
        uploadImage();
        //return false;
    }

    function uploadImg() {
        fetch('/upload', {
            method: 'POST',

            //
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                "greeting": "Hello from the browser!"
            })
        }).then((response) =>{
            return response.text();
        }).then((text) => {
            console.log("POST response: ");
            console.log(text);
        })
    }

    function uploadImage(){
        const req = new XMLHttpRequest();
        req.headers = {
            'Content-Type': 'application/json'
        }
        req.open("POST", "/upload");
        req.onload = () => {
            if (req.readyState == 4 && req.status == 200) {
               // alert('READY')
            }
            //alert('loded')
            //console.log(req.text)
            console.log(req.responseText)
            const data = JSON.parse(req.responseText)
            console.log(data.success)
            // document.querySelector('.alert').alert('show');
        }
        console.log(`Caption: ${captionText.value}`)
        console.log(`Gallery Type: ${galleryOptions.value}`)
        console.log(`Photo Type: ${gallerySection.options[galleryOptions.selectedIndex].text}`)
        console.log(`File: ${file.value}`)
        const data = new FormData();
        captionText = document.querySelector('#txtcaption');
        data.append('galleryType', galleryOptions)
        data.append('fototype', gallerySection)
        data.append('file', file)
        data.append('caption', captionText.value)

        //req.send(data)
        alert("DONE")
        return false;
    }
    
    $('#setupScreen').on('show.bs.modal', function (event) {
        let menu = $(event.relatedTarget)
        let modalTitle = menu.data('whatever');
        let modal = $(this)
        switch (modalTitle) {
            case "Gallery Section":
                modal.find('.modal-title').text(modalTitle)
                modal.find('.modal-label').text("Event Name")
                break;
            case "Sub Council Executives":
                modal.find('.modal-title').text(modalTitle)
                modal.find('.modal-label').text("Name of Executive")
                break;
            case "Zonal Executives":
                modal.find('.modal-title').text(modalTitle)
                modal.find('.modal-label').text("Name of Exco")
                break;
            case "Offices":
                modal.find('.modal-title').text(modalTitle)
                modal.find('.modal-label').text("Position")
                break;
    
        
            default:
                break;
        }
            
    })

    function uploadImageAjax(){
        const req = new XMLHttpRequest();
        req.headers = {
            'Content-Type': 'application/json'
        }
        req.open("POST", "/uploadAjax");
        req.onload = () => {
            if (req.readyState == 4 && req.status == 200) {
                alert('READY')
            }
            alert('loded')
            //console.log(req.text)
            console.log(req.responseText)
            const data = JSON.parse(req.responseText)
            console.log(data.success)
            // document.querySelector('.alert').alert();
        }
        console.log(`Caption: ${captionText.value}`)
        console.log(`Gallery Type: ${galleryOptions.value}`)
        console.log(`Photo Type: ${gallerySection.options[galleryOptions.selectedIndex].text}`)
        console.log(`File: ${file.value}`)
        const data = new FormData();
        captionText = document.querySelector('#txtcaption');
        data.append('galleryType', galleryOptions)
        data.append('fototype', gallerySection)
        data.append('file', file)
        data.append('caption', captionText.value)

        req.send(data)
        alert("DONE")
        // return false;
    }
    //setupScreen.on('show.bs.modal') = function(event)  {
    
    // $('#exampleModal').on('show.bs.modal', function (event) {
    //     var button = $(event.relatedTarget) // Button that triggered the modal
    //     var recipient = button.data('whatever') // Extract info from data-* attributes
    //     // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
    //     // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
    //     var modal = $(this)
    //     modal.find('.modal-title').text('New message to ' + recipient)
    //     modal.find('.modal-body input').val(recipient)
    //   })
})
document.addEventListener("DOMContentLoaded", function(){


    async function cargarAves(){
        const respuesta= await fetch("http://127.0.0.1:5000/aves/")
    
        if (!respuesta.ok){
            // console.log("Error al cargar eves.", (await respuesta).statusText)
            console.log("Error al cargar eves.", respuesta.statusText)
            return
        }

        const aves=await respuesta.json()
        // console.log(aves)

        const tbody= document.getElementById("i-table-arboles").querySelector("tbody")
        tbody.innerHTML=""

        aves.forEach(ave => {
            const row=tbody.insertRow()
            row.insertCell(0).textContent=ave.id
            row.insertCell(1).textContent=ave.nombre
            row.insertCell(2).textContent=ave.tamano
            row.insertCell(3).textContent=ave.color
            row.insertCell(4).textContent=ave.caracteristica
            row.insertCell(5).textContent=ave.comportamiento
        });
    }

    cargarAves()

})





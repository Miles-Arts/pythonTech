document.addEventListener('DOMContentLoaded', function () {

    const mostrarBosque =  () => {

        const cardSection = document.getElementById("i-card-section")

        const bosques = [
             {nombre: "Pino Floral", especie: "arbolis", img: "pino.jpg", visto: "Tuta", fecha: new Date(2024, 3, 14 )  }, 
             {nombre: "Árbol Agua", especie: "arbolis", img:"agua.jpg", visto: "Agua Blanca", fecha: new Date(2024, 4, 17 )},
             {nombre: "Árbol Nubeloso", especie: "arbolete", img:"boyaca-florar-01.jpg", visto: "Rio de Piedras", fecha: new Date(2024, 5, 22 )},
             {nombre: "Árbol Motoso", especie: "arbolastro", img:"boyaca-florar-07.jpg", visto: "El Cruce", fecha: new Date(2024, 5, 15 )},
             {nombre: "Árbol Cristal", especie: "arbofilia", img:"boyaca-florar-06.jpg", visto: "Rio Chicamocha", fecha: new Date(2024, 8, 4 )},
             {nombre: "Árbol Estrella", especie: "arboluna", img:"boyaca-florar-05.jpg", visto: "San Nicolás", fecha: new Date(2024, 6, 1 )}
            ] 

           bosques.forEach( bosque => { 
            const verBosque = document.createElement("div")
            verBosque.className = "col-lg-4 col-md-6 col-sm-6 "
            verBosque.innerHTML =  `  
                    <div class="card" style="width: 18rem;">
                        <img src="./img/${bosque.img}" class="card-img-top" alt="Imagen de Bosque de ${bosque.nombre}">
                        <div class="card-body">
                            <h5 class="card-title">${bosque.nombre }</h5>
                            <p class="card-text">${bosque.especie}</p>
                            <p class="card-text">${bosque.visto}</p>
                            <p class="card-text">${bosque.fecha.toLocaleDateString()}</p>
                            <a href="#" class="btn btn-primary">Ver más</a>
                        </div>
                    </div>
            ` 

            cardSection.appendChild(verBosque)

        }) 

    }

    mostrarBosque()

})
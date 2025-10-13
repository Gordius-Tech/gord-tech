// A fájlok tartalmának betöltése
function loadFile(filename) {
    // Mivel a fájlok a 'pysource' mappában vannak, az elérési utat is hozzáadjuk
    fetch('pysource/' + filename)
        .then(response => {
            if (!response.ok) {
                throw new Error('Hiba történt a fájl betöltésekor');
            }
            return response.text();
        })
        .then(data => {
            document.getElementById('file-content').textContent = data;
            document.getElementById('file-content').classList.remove('hidden');
        })
        .catch(error => {
            document.getElementById('file-content').textContent = 'Hiba történt a fájl betöltésekor: ' + error.message;
            document.getElementById('file-content').classList.remove('hidden');
        });
}

// A fájl tartalom megjelenítésének ki- és bekapcsolása
function toggleFileVisibility() {
    const fileContent = document.getElementById('file-content');
    fileContent.classList.toggle('hidden');
}

function toggleSzoveg(elem) {
    const szoveg = elem.querySelector(".hosszabb-szoveg");
  
    if (szoveg.style.maxHeight) {
      szoveg.style.maxHeight = null;
    } else {
      szoveg.style.maxHeight = szoveg.scrollHeight + "px";
    }
  }
  
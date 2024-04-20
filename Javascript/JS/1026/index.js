const player1Choice = document.querySelector("#player1-img");
const player2Choice = document.querySelector("#player2-img");
const btnList = document.querySelectorAll('button');
const imgList = document.querySelectorAll('button>img');
const player1Count = document.querySelector(".countA");
const player2Count = document.querySelector(".countB");

btnList.forEach((btn, index) => {
    btn.addEventListener("click",(e) => {
        btn.value = index;
        player1Choice.src = e.target.src;
        let selectIndex = Math.random()*3;
        let checkIndex = 0;
        selectIndex = Math.floor(selectIndex);
        const changeImg = setInterval(() => {
            player2Choice.src = imgList[checkIndex].src;
            checkIndex++;
            if (checkIndex > 2) {
                checkIndex = 0;
            }
        }, 100)
        setTimeout(() => { clearInterval(changeImg);
            player2Choice.src = imgList[selectIndex].src;
            const modalPrint = document.querySelector(".modal-content");
            const p = document.createElement("p");
            if (selectIndex == btn.value) {
                p.textContent = "무승부입니다."
            }
            else if (selectIndex == 1 && btn.value == 0) {
                p.textContent = "player2 의 승리입니다."
                player2Count.textContent = Number(player2Count.innerText) + 1;
            }
            else if (selectIndex == 1 && btn.value == 2) {
                p.textContent = "player1 의 승리입니다."
                player1Count.textContent = Number(player1Count.innerText) + 1;
            }
            else if (selectIndex == 0 && btn.value == 1) {
                p.textContent = "player1 의 승리입니다."
                player1Count.textContent = Number(player1Count.innerText) + 1;
            }
            else if (selectIndex == 0 && btn.value == 2) {
                p.textContent = "player2 의 승리입니다."
                player2Count.textContent = Number(player2Count.innerText) + 1;
            }
            else if (selectIndex == 2 && btn.value == 0) {
                p.textContent = "player1 의 승리입니다."
                player1Count.textContent = Number(player1Count.innerText) + 1;
            }
            else if (selectIndex == 2 && btn.value == 1) {
                p.textContent = "player2 의 승리입니다."
                player2Count.textContent = Number(player2Count.innerText) + 1;
            }
            modalPrint.innerHTML = "";
            modalPrint.appendChild(p);
            const parentModal = modalPrint.parentElement;
            parentModal.style.display = "flex";
            parentModal.style.justifyContent = "center";
            parentModal.style.alignContent = "center";
            parentModal.addEventListener("click", function(e) {
                parentModal.style.display = "none";
            })
        }, 3000)
    })
})
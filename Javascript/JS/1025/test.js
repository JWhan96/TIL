const ages = [18, 20, 21, 29, 11, 31]
    const names = ['홍길동', '이춘향', '금나래', '장보고', '임꺽정', '강감찬']

    ages.forEach ((num) => {
        if (num < 20) {
            console.log(num)
        }
    }) 

    const create = (age,name) => {
        return { age : age, name : name}
    }
    
    const actors = []
    for (let i = 0; i<names.length; i++) {
        actors.push(create(ages[i], names[i]));
    }
    console.log(actors)

    const adult_actors = []
    actors.forEach((infos) => {
        if (infos.age >= 20) {
            adult_actors.push(infos)
        }
    })
    console.log(adult_actors)
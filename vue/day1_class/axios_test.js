// const getData = function() {
//   console.log('동현바보')
// }
const backendURL = 'http://127.0.0.1:8000/api/v1/articles/'


const getData = function() {
  axios({
    method: 'GET',
    url: backendURL
  }).then((response) => {
    console.log(response)
  }).catch((error) => {
    console.error(error)
  })
}

const postData = function() {
  axios({
    method : 'POST',
    url: backendURL,
    data:{
      title: 'test',
      content: 'test',
    }
  }).then((response) => {
    console.log(response)
  }).catch((error) => {
    console.error(error)
  })
}


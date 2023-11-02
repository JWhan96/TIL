const { createApp, ref, computed,} = Vue

const app = createApp({
  // setup(): 앱이 생성될 때 호출되는 메서드
  setup() {
    // 할일 목록
    const todos = ref([])
    // 사용자의 입력을 받을 변수
    const newTodo = ref('')

    // 새로운 할 일을 추가하는 메서드
    let todoID = 1;
    const addTodo = () => {
      if (newTodo.value.trim()) {
        const tmp = {
          id: todoID++,
          text : newTodo.value,
          completed: false,
        }
        // todos 안에 newTodo를 추가      
        todos.value.push(tmp)
        newTodo.value = '' // 입력 필드 초기화
      } else {
        alert('값을 입력해 주세요')
      }    
      
    }

    const delTodo = (index) => {
      // 해당 인덱스 삭제
      todos.value.splice(index, 1)
      
    }

    const toggleTodoStatus = (todo) => {
      todo.completed = !todo.completed
      // todos.value = todos.value.filter((todo) => !todo.completed)
    }
    
    const delCompletedTodos = () => {
      // todo.completed가 true인것만 삭제
      // todos.value = todos.value.filter((todo) => {
      //   return todo.completed === false
      // })
      // 축약본
      todos.value = todos.value.filter((todo) => !todo.completed)
      
    }

    // const todoCount = () => {
    //   return false
    // }

    // computed: 계산된 속성
    // 기존 변수를 수정하지않고, 계산된 값만 가지고 새로운 변수를 만들고 싶을 때
    // computed메서드 내에서 사용하는 변수가 변경이 생길 때 마다 새로 계산
    // 아래 예시에는 todos변수가 변경되면 바로 계산
    const todoCount = computed(() => {
      return todos.value.filter((todo) => todo.completed).length > 0
    })
    

    return {
      todos,
      newTodo,
      addTodo,
      delTodo,
      toggleTodoStatus,
      delCompletedTodos,
      todoCount,
    }
  }
})

app.mount('#app')
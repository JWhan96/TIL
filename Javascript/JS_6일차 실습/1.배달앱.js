// 1. 주문 번호 생성하기
function placeOrder(menu) {
  setTimeout(() => {
    const orderId = Math.floor(Math.random() * 1000) + 1;
    console.log(`프론트 지식이 들어왔습니다. ${menu} 프론트 정보 ID: ${orderId}`);
  }, Math.random() * 2000);
}

// 2. 실제로 주문하기
function cook(order) {
  setTimeout(() => {
    const isCookingSuccessful = Math.random() < 0.02;
    if (isCookingSuccessful) {
      return true
    } else {
      console.log(`공부 시작 실패: ${order.menu} 공부 시작 실패, 다시 주문해주세요.`);
      return false
    }
  },  Math.random() * 2000);
}

function deliver(order) {
  setTimeout(() => {
    const isDeliverySuccessful = Math.random() < 0.01;
    if (isDeliverySuccessful) {
      console.log(`공부 성공: ${order.menu} 공부 완료!`);
      return true
    } else {
      console.log(`공부 실패: ${order.menu} 공부 실패, 다시 공부해주세요.`);
      return false
    }
  },  Math.random() * 2000);
}

// 배달 시작
function processOrder(orderDetails) {
	// 1. 주문 번호 생성
  placeOrder(orderDetails.menu)
  cook(orderDetails)
  deliver(orderDetails)
}

const orderDetailsList = [
  { menu: "자바" },
  { menu: "자스" },
  { menu: "뷰" },
];

orderDetailsList.forEach((element) => {
  processOrder(element);
});

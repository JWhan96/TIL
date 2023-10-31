// 1. 주문 번호 생성하기
function placeOrder(menu, goCook) {
  setTimeout(() => {
    const orderId = Math.floor(Math.random() * 1000) + 1;
    goCook({ orderId, menu })
  }, Math.random() * 20);
}

// 2. 실제로 주문하기
function cook(order, goDelivery) {
  setTimeout(() => {
    const isCookingSuccessful = Math.random() < 0.002;
    if (isCookingSuccessful) {
      // 요리를 성공했다는 의미
      // 다음에 할 일: 배달
      goDelivery(order)
    } else {
      console.log(`공부 실패: ${order.menu} 공부 실패, 다시 공부해주세요.`);
    }
  }, Math.random() * 20);
}

function deliver(order, orderComplete) {
  setTimeout(() => {
    const isDeliverySuccessful = Math.random() < 0.001;
    if (isDeliverySuccessful) {
      orderComplete(`마스터 성공: ${order.menu} 마스터 완료!`)
    } else {
      console.log(`마스터 실패: ${order.menu} 마스터 실패, 다시 마스터해주세요.`);
    }
  }, Math.random() * 20);
}

// 배달 시작
function processOrder(orderDetails) {
  placeOrder(orderDetails.menu, (order) => {
    console.log(`프론트 지식이 들어왔습니다. ${order.menu} 프론트 정보 ID: ${order.orderId}`);

    cook(order, (order) => {
      console.log(`${order.menu} 공부 완료!`)

      deliver(order, (status) => {
        console.log(status)
        console.log('-----------------------')
      })
    })
  })
}

const orderDetailsList = [
  { menu: "자바" },
  { menu: "자스" },
  { menu: "뷰" },
];

orderDetailsList.forEach((element) => {
  processOrder(element);
});

// Массив с предсказаниями
const predictions = [
    "Сегодня твой день!",
    "Удача на твоей стороне.",
    "Ты встретишь старого друга.",
    "Будь осторожен с новыми знакомствами.",
    "Завтра принесет новые возможности.",
    "Скоро ты получишь хорошие новости.",
    "Не бойся принимать решения — ты на правильном пути.",
    "Настало время попробовать что-то новое.",
    "Уделите больше времени себе — это пойдет на пользу.",
    "Вас ждет неожиданное приключение!"
];

// Функция для генерации случайного предсказания
function generatePrediction() {
    const randomIndex = Math.floor(Math.random() * predictions.length);
    const predictionElement = document.getElementById("prediction");
    predictionElement.textContent = predictions[randomIndex];
}

const moves = document.getElementById("moves-count");
const timeValue = document.getElementById("time");
const startButton = document.getElementById("start");
const stopButton = document.getElementById("stop");
const gameContainer = document.querySelector(".game-container");
const result = document.getElementById("result");
const controls = document.querySelector(".controls-container");
let cards;
let interval;
let firstCard = false;
let secondCard = false;
let movesCount = 0;
let winCount = 0;
let seconds = 0;
let minutes = 0;

const items = [
  { name: "bee", image: "https://media.istockphoto.com/id/1174366497/photo/cyber-security-and-digital-data-protection-concept.jpg?s=612x612&w=0&k=20&c=thysejfubQ81RBkRoDtkKGmb4390eyv3P8L_lQ7_5aU=" },
  { name: "crocodile", image: "https://previews.123rf.com/images/yupiramos/yupiramos1706/yupiramos170638934/81143932-bomb-with-at-symbol-and-cyber-security-related-objects-over-white-background-vector-illustration.jpg" },
  { name: "macaw", image: "https://static.vecteezy.com/system/resources/previews/007/894/277/non_2x/set-of-icons-related-to-cyber-security-contains-such-icons-as-authentication-backdoor-cloud-computer-cyber-security-cybercrime-and-more-vector.jpg" },
  { name: "gorilla", image: "https://images.indianexpress.com/2023/05/cyber-crime-2-4.jpg?w=414" },
  { name: "panther", image: "https://www.thesslstore.com/blog/wp-content/uploads/2019/10/what-is-ddos-botmaster.png" },
  { name: "chimpa", image: "https://www.shiksha.com/online-courses/articles/wp-content/uploads/sites/11/2022/05/Dos-768x776.png" },
  { name: "dog", image: "https://assets.website-files.com/5ff66329429d880392f6cba2/6128ad5432348b429b19330f_Trojans%20Preview.png" },
  { name: "cat", image: "https://i0.wp.com/blog.frontiersin.org/wp-content/uploads/2021/02/shutterstock_749866270.jpg?fit=5510%2C4133&ssl=1" },
  
];


const timeGenerator = () => {
  seconds += 1;

  if (seconds >= 60) {
    minutes += 1;
    seconds = 0;
  }

  let secondsValue = seconds < 10 ? `0${seconds}` : seconds;
  let minutesValue = minutes < 10 ? `0${minutes}` : minutes;
  timeValue.innerHTML = `<span>Time:</span> ${minutesValue}:${secondsValue}`;

  if (minutes === 0 && seconds === 45) {
    stopGame();
    result.innerHTML = `<h2>Time's Up!</h2><h4>Moves: ${movesCount}</h4>`
    
    
  }
};

const movesCounter = () => {
  movesCount += 1;
  moves.innerHTML = `<span>Moves:</span> ${movesCount}`;

  if (movesCount === 10) {
    stopGame();
    result.innerHTML = `<h2>Move Limit Reached!</h2><h4>Moves: ${movesCount}</h4>`;
  }
};

const generateRandom = (size = 4) => {
  let tempArray = [...items];
  let cardValues = [];

  size = (size * size) / 2;

  for (let i = 0; i < size; i++) {
    const randomIndex = Math.floor(Math.random() * tempArray.length);
    cardValues.push(tempArray[randomIndex]);
    tempArray.splice(randomIndex, 1);
  }

  return cardValues;
};

const matrixGenerator = (cardValues, size = 4) => {
  gameContainer.innerHTML = "";
  cardValues = [...cardValues, ...cardValues];
  cardValues.sort(() => Math.random() - 0.5);
  for (let i = 0; i < size * size; i++) {
    gameContainer.innerHTML += `
      <div class="card-container" data-card-value="${cardValues[i].name}">
        <div class="card-before">?</div>
        <div class="card-after">
          <div class="image-container">
            <img src="${cardValues[i].image}" class="image"/>
          </div>
        </div>
      </div>
    `;
  }
  gameContainer.style.gridTemplateColumns = `repeat(${size}, auto)`;

  cards = document.querySelectorAll(".card-container");
  const movesCounter = () => {
    movesCount += 1;
    moves.innerHTML = `<span>Moves:</span> ${movesCount}`;
  
    if (movesCount === 10) {
      stopGame();
      result.innerHTML = `<h2>Move Limit Reached!</h2><h4>Moves: ${movesCount}</h4>`;
    }
  };
  
  cards.forEach((card) => {
    card.addEventListener("click", () => {
      if (!card.classList.contains("matched") && !card.classList.contains("flipped")) {
        card.classList.add("flipped");
  
        if (!firstCard) {
          firstCard = card;
          firstCardValue = card.getAttribute("data-card-value");
        } else if (!secondCard) {
          secondCard = card;
          let secondCardValue = card.getAttribute("data-card-value");
  
          if (firstCardValue === secondCardValue) {
            firstCard.classList.add("matched");
            secondCard.classList.add("matched");
            firstCard = null;
            secondCard = null;
            winCount += 1;
  
            if (winCount === Math.floor(cardValues.length / 2)) {
              result.innerHTML = `<h2>You Won</h2><h4>Moves: ${movesCount}</h4>`;
              stopGame();
            } else {
              // Activate the options for the next card
              // Code to activate the options for Card 2 goes here
            }
          } else {
            let [tempFirst, tempSecond] = [firstCard, secondCard];
            firstCard = null;
            secondCard = null;
            let delay = setTimeout(() => {
              tempFirst.classList.remove("flipped");
              tempSecond.classList.remove("flipped");
            }, 900);
          }
  
          movesCounter();
        }
      }
    });
  });
  
};

const checkCardMatch = () => {
  //To fix this, you can add a call to setTimeout in the checkCardMatch function to remove the flipped class from the first and second cards after a delay, regardless of whether they match or not. Here's an updated version of the checkCardMatch function that includes this change:                                                                                                        const checkCardMatch = () => {
    if (firstCard === secondCard) {
      // If the first and second cards are the same element, do nothing
      return;
    }
  
    const firstCardValue = firstCard.getAttribute("data-card-value");
    const secondCardValue = secondCard.getAttribute("data-card-value");
  
    if (firstCardValue === secondCardValue) {
      firstCard.classList.add("matched");
      secondCard.classList.add("matched");
      winCount += 1;
  
      if (winCount === cards.length / 2) {
        stopGame();
        result.innerHTML = `<h2>You Won!</h2><h4>Moves: ${movesCount}</h4>`;
      }
    }
  
    setTimeout(() => {
      firstCard.classList.remove("flipped");
      secondCard.classList.remove("flipped");
      firstCard = null;
      secondCard = null;
    }, 1000);
  };                                                         

  firstCard = null;
  secondCard = null;


const startGame = () => {
  movesCount = 0;
  seconds = 0;
  minutes = 0;
  moves.innerHTML = `<span>Moves:</span> ${movesCount}`;
  result.innerHTML = "";
  winCount = 0;
  controls.classList.add("hide");
  stopButton.classList.remove("hide");
  startButton.classList.add("hide");
  interval = setInterval(timeGenerator, 1000);
  const cardValues = generateRandom();
  matrixGenerator(cardValues);
};

const stopGame = () => {
  controls.classList.remove("hide");
  stopButton.classList.add("hide");
  startButton.classList.remove("hide");
  clearInterval(interval);
};

startButton.addEventListener("click", startGame);
stopButton.addEventListener("click", stopGame);
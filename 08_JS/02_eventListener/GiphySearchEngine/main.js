/* 1. <input> 태그 안의 값을 잡는다. */



const init = () => {
    const inputArea = document.querySelector('#js-userinput');
    const button = document.querySelector('#js-go');

    inputArea.addEventListener('keydown', e => {
        if (e.key === 'Enter') {
            searchAndPush(inputArea.value);
        }
    });

    button.addEventListener('click', e => {
        searchAndPush(inputArea.value);
    });
};


const searchAndPush = keyword => {
    const resultArea = document.querySelector('#result-area');
    resultArea.innerHTML = null;
    const KEY ='eQurkeR4ILDoKtvORUl03NBSXDIg42w9';
    const URL = `http://api.giphy.com/v1/gifs/search?q=${keyword}&api_key=${KEY}`;

    const AJAXCall = new XMLHttpRequest(); // 객체 생성 - AJAX 요청 보내주는 역할
    AJAXCall.open('GET', URL); // 요청을 발사할 준비
    AJAXCall.send();
    AJAXCall.addEventListener('load', e => {
        const parseData = JSON.parse(e.target.response);
        pushToDOM(parseData);
    });

    const pushToDOM = dataset => {
        const dataArray = dataset.data;
        let imageURL;
        let element;
        for (const imgData of dataArray) {
            imageURL = imgData.images.fixed_height.url;
            element = document.createElement('img'); // <img >
            element.classList.add('container-image'); // <img class="c-i">
            element.src = imageURL;
            element.alt = imgData.id;
            resultArea.appendChild(element);
        }
    };
};

init();

/* 2. Giphy API 를 통해 data 를 받아서 가공한다. */

// Asynchronous Javascript And XML - AJAX
/*
    기존의 요청
    1. 링크를 누른다.
    2. href 으로 요청이 간다.
    3. 브라우저가 새로고침 되며, 응답을 render 한다.

    AJAX 요청
    1. 어떤 event 가 발생한다.
    2. 요청을 전송하고, 응답이 도착할 때까지 기다린다. 화면 전환은 없다.
    3. 응답이 오면, 지금 문서에서 응답 내용을 추가로 render 한다.
 */



/* 3. GIF 파일들을 index.html(DOM)에 밀어 넣어서 보여준다. */

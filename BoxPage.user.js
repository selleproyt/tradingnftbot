// ==UserScript==
// @name         BoxPage
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  04.12.21
// @author       selletech
// @match        https://www.binance.com/ru/nft/goods/mystery-box/detail?productId=*&isOpen=false&isProduct=1
// @icon         https://www.google.com/s2/favicons?domain=binance.com
// @grant        none
// ==/UserScript==

setTimeout(function(){
    let divs = document.getElementsByClassName('css-u5990');
    let div1=divs[0];
    let buts = div1.getElementsByTagName('button');
    let but = buts[0];
    but.click();
    setTimeout(function(){
        let divs2 = document.getElementsByClassName('css-sr9689');
        let div2= divs2[0];
        let buts2 = div2.getElementsByTagName('button');
        let but2 = buts2[1];
        but2.click();
        setTimeout(function(){
            window.location.href='https://www.binance.com/ru/nft/balance?tab=boxes';
        },10000);
    },3000);
},3000);
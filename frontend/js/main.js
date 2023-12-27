/* load나 resize, reset 시에 초기화 부분 */

addEventListener('load',()=>{
  initalize()
})
addEventListener('resize',()=>{
  initalize()
})
addEventListener('reset',()=>{
  initalize()
})

const initalize = ()=>{
  windowHeight = window.outerHeight
  history.scrollRestoration = "manual";
}


const introText = document.querySelector('.h1')
const introSkip = document.querySelector('.h2')
const introAnimation = document.querySelector('.lottie-player')

window.onload = ()=>{
setTimeout(()=>{
  introText.style.display="block"
  },400)
}
setTimeout(()=>{
  introAnimation.style.display="block"
  },1000)
setTimeout(()=>{
  introSkip.style.display="block"
  },800)

  const skipButton = document.querySelector(".skip-button");

  skipButton.addEventListener("click", (event) => {
    event.preventDefault();

    const targetElement = document.getElementById("home");
    const targetPosition = targetElement.offsetTop;

    window.scrollTo({
      top: targetPosition,
      behavior: "smooth"
    });
  });

let windowHeight = window.innerHeight
initalize()

const h3Text = document.querySelector('.h3')

let observer1 = new IntersectionObserver(entries=>{
  observer1cb(entries[0])
},{root: null,threshold:0.8})
const observer1cb = entry=>{
if(entry.isIntersecting){
  setTimeout(()=>{
      h3Text.style.display = "block"
      h3Text.style.opacity = 1
      h3Text.style.animation = `appear_from_bottom ease 2s`
      },800)

  // 화면에 시간간격마다 차례대로 화면에 요소를 띄움, 띄어지는 요소는 CSS animation 이 걸려있어서 부드럽게 동작
}
}
observer1.observe(h3Text)

const h4Text = document.querySelector('.h4')
const h4Png = document.querySelector('.char')

let observer2 = new IntersectionObserver(entries=>{
  observer2cb(entries[0])
},{root: null,threshold:0.8})
const observer2cb = entry=>{
if(entry.isIntersecting){
  setTimeout(()=>{
      h4Text.style.display = "block"
      h4Text.style.opacity = 1
      h4Text.style.animation = `appear_from_bottom ease 2s`
      },600)
      setTimeout(()=>{
        h4Png.style.display = "block"
        h4Png.style.opacity = 1
        h4Png.style.animation = `appear_from_bottom ease 2s`
        },600)

  // 화면에 시간간격마다 차례대로 화면에 요소를 띄움, 띄어지는 요소는 CSS animation 이 걸려있어서 부드럽게 동작
}
}
observer2.observe(h4Text)
observer2.observe(h4Png)

const logo = document.querySelector('.logo')
const btLogin = document.querySelector('.loginButton')
const btCal = document.querySelector('.calButton')
const btApply = document.querySelector('.applyButton')
const btMypage = document.querySelector('.mypageButton')


let observer3 = new IntersectionObserver(entries=>{
observer3cb(entries[0])
})
const observer3cb = entry=>{
if(entry.isIntersecting){
  logo.style.opacity = 1
  setTimeout(()=>{
    btLogin.style.display = "flex"
    setTimeout(()=>{
      btCal.style.display = "flex"
      //console.log(home3TextSpans)
      setTimeout(()=>{
        btApply.style.display = "flex"
        setTimeout(()=>{
          btMypage.style.display = "flex"
        },400)
        },400)                   
      },400)
  },400)
  observer3.unobserve(logo)
}
}
observer3.observe(logo)


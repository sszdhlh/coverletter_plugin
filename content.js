function extractJD() {
    let site = window.location.hostname;
    let jdText = '';
  
    if (site.includes('linkedin.com')) {
      const el = document.querySelector('.description__text') || document.querySelector('.show-more-less-html__markup');
      if (el) jdText = el.innerText;
    } else if (site.includes('seek.com.au')) {
      const el = document.querySelector('[data-automation="jobAdDetails"]');
      if (el) jdText = el.innerText;
    } else if (site.includes('indeed.com')) {
      const el = document.querySelector('#jobDescriptionText');
      if (el) jdText = el.innerText;
    }
  
    if (jdText) {
      chrome.storage.local.set({ jdText });
    }
  }
  
  window.onload = () => setTimeout(extractJD, 1000);  // 等待页面加载完
  
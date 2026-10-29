(() => {
  const box = document.querySelector('.embedded-video');
  if (!box) return;
  box.querySelector('button').addEventListener('click', () => {
    const frame = document.createElement('iframe');
    frame.src = 'https://www.youtube-nocookie.com/embed/IiDuY4scFeY?autoplay=0';
    frame.title = '2024 深山拜年';
    frame.allow = 'fullscreen; picture-in-picture; encrypted-media';
    frame.allowFullscreen = true;
    frame.referrerPolicy = 'strict-origin-when-cross-origin';
    box.replaceChildren(frame);
  });
})();

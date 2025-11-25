const setOgp = async(url, element) => {
  const proxyUrl = `https://corsproxy.io/?${encodeURIComponent(url)}`;
  const response = await fetch(proxyUrl);
  const html = await response.text();
  const domParser = new DOMParser();
  const dom = domParser.parseFromString(html, 'text/html');
  const ogp = Object.fromEntries(
    [...dom.head.children]
      .filter(
        (element) =>
          element.tagName === 'META' &&
          element.getAttribute('property')?.startsWith('og:image')
      )
      .map((element) => {
        return [
          'ogpImage',
          element.getAttribute('content')
        ];
      })
  );

  if (ogp.ogpImage) {
    ogpHtml = `
    <div class="requirements--contents__article-img">
      <img src="${ogp.ogpImage}" alt="article-image" style="width: 200px; height: auto; display: block;">
    </div>
    `
    element.insertAdjacentHTML('afterbegin', ogpHtml);
  } else {
    opgHtml = `<div class="requirements--contents__article-img" style='height: 110px; background-color: #9AB292;'></div>`
  }
};

const getAnkerByOgp = () => {
  const ogpElements = document.querySelectorAll('a[id^="ogp-"]');
  ogpElements.forEach(element => {
    setOgp(element.href, element);
  });
};
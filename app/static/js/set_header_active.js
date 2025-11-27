const setHeaderActiveByPath = () => {
  const currentPath = window.location.pathname;

  if (currentPath.startsWith('/portral/')) {
    const element = document.getElementById('portral');
    element.classList.add('header--active');
  } else if (currentPath === '/inquiry/') {
    const element = document.getElementById('inquiry');
    element.classList.add('header--active');
  }
};
const setHeaderActiveByPath = () => {
  const currentPath = window.location.pathname;

  if (currentPath.startsWith('/portral/')) {
    const element = document.getElementById('portral');
    element.classList.add('header--active');
  } else if (currentPath.startsWith('/inquiry/') || currentPath.startsWith('/answers/')) {
    const element = document.getElementById('inquiry');
    element.classList.add('header--active');
  }
};
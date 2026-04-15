function mostrarMensagem(texto, tipo) {
  const el = document.getElementById('mensagem');
  const icone = tipo === 'sucesso' ? '✓' : '✕';
  el.innerHTML = `<span>${icone}</span> ${texto}`;
  el.className = 'mensagem ' + tipo;
  clearTimeout(window._msgTimer);
  window._msgTimer = setTimeout(() => { el.className = 'mensagem hidden'; }, 3500);
}
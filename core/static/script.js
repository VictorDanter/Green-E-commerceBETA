document.addEventListener('DOMContentLoaded', () => {
    
    // Selecionando os elementos do DOM
    const menuBtn = document.getElementById('menuBtn');
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('overlay');

    // Função para abrir o menu lateral
    function openMenu() {
        sidebar.classList.add('active');
        overlay.classList.add('active');
        // Trava a rolagem da página principal para focar no menu
        document.body.style.overflow = 'hidden'; 
    }

    // Função para fechar o menu lateral
    function closeMenu() {
        sidebar.classList.remove('active');
        overlay.classList.remove('active');
        // Libera a rolagem da página novamente
        document.body.style.overflow = 'auto';
    }

    // Evento de clique no botão "Hambúrguer"
    if (menuBtn) {
        menuBtn.addEventListener('click', openMenu);
    }

    // Evento de clique no Overlay (fundo escuro) para fechar
    if (overlay) {
        overlay.addEventListener('click', closeMenu);
    }
    
    // Opcional: Fechar ao pressionar a tecla ESC
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && sidebar.classList.contains('active')) {
            closeMenu();
        }
    });
    // --- LÓGICA DE BUSCA INSTANTÂNEA ---
    
    const searchInput = document.getElementById('searchInput');
    const resultsBox = document.getElementById('searchResultsBox');

    if (searchInput && resultsBox) {
        
        // Escuta quando o usuário digita
        searchInput.addEventListener('input', function(e) {
            const termo = e.target.value.trim();

            if (termo.length > 0) {
                // Chama nosso Back-end Django
                fetch(`/buscar_produtos/?q=${termo}`)
                    .then(response => response.json())
                    .then(data => {
                        resultsBox.innerHTML = ''; // Limpa resultados antigos

                        if (data.results.length > 0) {
                            resultsBox.classList.add('active'); // Mostra a caixa
                            
                            // Cria o HTML para cada produto encontrado
                            data.results.forEach(produto => {
                                const link = document.createElement('a');
                                link.href = `/produto/${produto.id}/`; // Link para a página que criamos
                                link.classList.add('search-item');
                                
                                link.innerHTML = `
                                    <img src="${produto.imagem}" alt="${produto.nome}">
                                    <div class="search-info">
                                        <h4>${produto.nome}</h4>
                                        <span>R$ ${produto.preco}</span>
                                    </div>
                                `;
                                resultsBox.appendChild(link);
                            });
                        } else {
                            // Se não achar nada
                            resultsBox.innerHTML = '<div style="padding:15px; text-align:center; color:#999;">Nenhum produto encontrado.</div>';
                            resultsBox.classList.add('active');
                        }
                    });
            } else {
                // Se apagar o texto, esconde a caixa
                resultsBox.classList.remove('active');
            }
        });

        // Fecha a busca se clicar fora dela
        document.addEventListener('click', function(e) {
            if (!searchInput.contains(e.target) && !resultsBox.contains(e.target)) {
                resultsBox.classList.remove('active');
            }
        });
    }
});
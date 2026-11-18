# Bloco 02 — Motor de animação inicial

Execute a partir da raiz do projeto com o ambiente virtual ativo:

```bash
python src/main.py
```

Teste repouso, teclado, mouse e ambos simultaneamente dentro da janela. A piscada dura 350 ms e ocorre após um intervalo aleatório de 3 a 6 segundos em repouso. A atividade de teclado ou mouse interrompe a piscada e reinicia a espera. ESC encerra. Os eventos são locais à janela; o programa não registra o conteúdo digitado nem grava áudio.

Sem PNGs oficiais, aparece um círculo temporário e o nome BUSTER. Os sprites devem ser adicionados a assets/sprites/. A captura global será implementada em etapa posterior. Janela e estados de entrada validados pelo usuário no Kali; novo temporizador de piscada e Windows ainda aguardam validação.

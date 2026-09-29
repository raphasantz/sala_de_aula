<?php include "includes/cabecalho.php"; ?>
<!-- ============================================================
     CONTATO + LOCALIZAÇÃO (página única) — formulário POST + mapa
     ============================================================ -->
<h2 class="secao">Fale com a loja</h2>

<div class="contato-grid">
    <form class="cartao" action="processar_contato.php" method="post" style="max-width:none">
        <label for="nome">Nome completo *</label>
        <input type="text" id="nome" name="nome" placeholder="Ex.: Maria da Silva" required>

        <label for="email">E-mail *</label>
        <input type="email" id="email" name="email" placeholder="voce@exemplo.com" required>

        <label for="assunto">Assunto</label>
        <select id="assunto" name="assunto">
            <option value="" disabled selected>Selecione…</option>
            <option value="duvida">Dúvida sobre produto</option>
            <option value="orcamento">Orçamento</option>
            <option value="suporte">Suporte pós-venda</option>
            <option value="outro">Outro</option>
        </select>

        <label for="mensagem">Mensagem *</label>
        <textarea id="mensagem" name="mensagem" rows="5" placeholder="Escreva sua mensagem…" required></textarea>

        <div class="radio-linha">
            <input type="checkbox" id="novidades" name="novidades" value="sim">
            <label for="novidades" style="margin:0">Quero receber novidades da loja</label>
        </div>

        <button type="submit">Enviar mensagem</button>
    </form>

    <div class="mapa-card">
        <img src="imagens/mapa.png" alt="Mapa de localização da Loja Tech da Turma">
        <h3>📍 Onde estamos</h3>
        <p><b>Loja Tech da Turma</b><br>
           Av. das Turmas, 42 — Centro<br>
           (esquina com a Rua dos Bits, em frente à Praça)<br>
           Muriaé — MG · CEP 36880-000</p>
        <h3>🕒 Horário de atendimento</h3>
        <p>Segunda a sexta: 8h às 18h<br>
           Sábado: 8h às 12h<br>
           Domingo e feriados: fechado (mas o site compra sozinho!)</p>
        <h3>🚌 Como chegar</h3>
        <p>Ônibus linhas 02 e 07 até a Praça; 5 min a pé pela Av. das Turmas.
           De carro: estacionamento gratuito na Rua dos Bits.</p>
    </div>
</div>

<?php include "includes/rodape.php"; ?>

<?php include "includes/cabecalho.php"; ?>
<!-- ============================================================
     CADASTRO DE CLIENTES — formulário completo (PI-I semanas 15-17)
     label + id + name em TUDO; types adequados; required no essencial
     ============================================================ -->
<h2 class="secao">Cadastre-se na loja</h2>

<form class="cartao" action="processar_cadastro.php" method="post">
    <label for="nome">Nome completo *</label>
    <input type="text" id="nome" name="nome" placeholder="Ex.: João Pereira" required>

    <label for="email">E-mail *</label>
    <input type="email" id="email" name="email" placeholder="voce@exemplo.com" required>

    <label for="telefone">Telefone</label>
    <input type="text" id="telefone" name="telefone" placeholder="(32) 99999-0000">

    <label for="nascimento">Data de nascimento</label>
    <input type="date" id="nascimento" name="nascimento">

    <label for="cidade">Cidade</label>
    <select id="cidade" name="cidade">
        <option value="" disabled selected>Selecione…</option>
        <option value="Muriaé">Muriaé</option>
        <option value="Ubá">Ubá</option>
        <option value="Leopoldina">Leopoldina</option>
        <option value="Outra">Outra</option>
    </select>

    <p style="margin:14px 0 4px; font-weight:700; color:#0d2b4e; font-size:14.5px">Como conheceu a loja?</p>
    <div class="radio-linha">
        <input type="radio" id="r1" name="origem" value="instagram">
        <label for="r1" style="margin:0">Instagram</label>
        <input type="radio" id="r2" name="origem" value="amigos">
        <label for="r2" style="margin:0">Amigos</label>
        <input type="radio" id="r3" name="origem" value="escola">
        <label for="r3" style="margin:0">Escola</label>
    </div>

    <div class="radio-linha" style="margin-top:10px">
        <input type="checkbox" id="termos" name="termos" value="sim" required>
        <label for="termos" style="margin:0">Li e aceito os termos da loja *</label>
    </div>

    <button type="submit">Cadastrar</button>
</form>

<?php include "includes/rodape.php"; ?>

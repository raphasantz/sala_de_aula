Attribute VB_Name = "mdlRelatorios"
' ============================================================
' MÓDULO DE RELATÓRIOS E ARQUIVOS  ·  LP2 (semanas 13, 14, 19 e 20)
' Projeto Loja Tech da Turma — gerencial em VB6
' ============================================================

' ---------- Relatório de estoque via Printer (semanas 19-20) ----------
Public Sub RelatorioEstoque()
    Dim rs As ADODB.Recordset
    Set rs = cn.Execute("SELECT nome, categoria, preco, estoque " & _
                        "FROM produtos ORDER BY nome")

    Printer.FontName = "Courier New"          'monoespaçada: colunas fecham
    Printer.Print Tab(18); "LOJA TECH DA TURMA - RELATORIO DE ESTOQUE"
    Printer.Print String(64, "-")
    Printer.Print "PRODUTO"; Tab(34); "CATEGORIA"; Tab(50); "PRECO"; Tab(60); "ESTOQUE"
    Printer.Print String(64, "-")

    Do While Not rs.EOF
        Printer.Print Left(rs!nome & Space(32), 32); _
                  Left(rs!categoria & Space(16), 16); _
                  Right(Space(9) & Format(rs!preco, "0.00"), 9); _
                  Right(Space(8) & rs!estoque, 8)
        rs.MoveNext
    Loop

    Printer.Print String(64, "-")
    Printer.Print "Emitido em " & Format(Now, "dd/mm/yyyy hh:nn")
    Printer.EndDoc                            'sem EndDoc o job nao sai!
    rs.Close
    MsgBox "Relatório enviado à impressora (ou PDF).", vbInformation
End Sub

' ---------- Exportar produtos para arquivo texto (semanas 13-14) ----------
Public Sub ExportarProdutosTxt(caminho As String)
    Dim rs As ADODB.Recordset, n As Integer, linhas As Long
    Set rs = cn.Execute("SELECT nome, categoria, preco, estoque FROM produtos ORDER BY nome")

    n = FreeFile                                   'número de arquivo livre
    Open caminho For Output As #n                  'Output: cria/substitui
    Print #n, "nome;categoria;preco;estoque"       'cabeçalho CSV-like
    Do While Not rs.EOF
        Print #n, rs!nome & ";" & rs!categoria & ";" & _
                  Format(rs!preco, "0.00") & ";" & rs!estoque
        linhas = linhas + 1
        rs.MoveNext
    Loop
    Close #n                                       'SEM Close = dado perdido!
    rs.Close
    MsgBox "Exportadas " & linhas & " linhas para:" & vbCrLf & caminho, vbInformation
End Sub

' ---------- Importar preços de um arquivo texto (semanas 13-14) ----------
Public Sub ImportarPrecosTxt(caminho As String)
    Dim n As Integer, linha As String, partes() As String
    Dim atualizados As Long, recusadas As Long

    If Dir(caminho) = "" Then
        MsgBox "Arquivo não encontrado: " & caminho, vbExclamation
        Exit Sub
    End If

    n = FreeFile
    Open caminho For Input As #n                   'Input: somente leitura
    Do While Not EOF(n)                            'EOF: fim do arquivo
        Line Input #n, linha
        partes = Split(linha, ";")
        If UBound(partes) >= 1 And IsNumeric(partes(1)) Then
            cn.Execute "UPDATE produtos SET preco = " & _
                       Format(CSng(partes(1)), "0.00") & _
                       " WHERE id = " & CLng(partes(0))
            atualizados = atualizados + 1
        Else
            recusadas = recusadas + 1              'linha inválida: conta e segue
        End If
    Loop
    Close #n
    MsgBox "Atualizados: " & atualizados & vbCrLf & _
           "Recusadas: " & recusadas, vbInformation, "Importação"
End Sub

' ---------- Backup "didático" via arquivo (complemento ao mysqldump) ----------
Public Sub BackupTxt(caminho As String)
    ExportarProdutosTxt caminho     'mesma rotina: cópia simples dos dados
End Sub

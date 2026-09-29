Attribute VB_Name = "mdlConexao"
' ============================================================
' MÓDULO DE CONEXÃO + CRUD  ·  LP2 (semanas 3, 15 e 16)
' Projeto Loja Tech da Turma — gerencial em VB6
'
' ANTES DE USAR (no VB6):
'  1) Projeto > Referências > marque "Microsoft ActiveX Data Objects 2.8 Library"
'  2) Instale o MySQL Connector/ODBC (painel de controle > ODBC >
'     confirme o driver "MySQL ODBC 8.0 ANSI Driver")
'  3) Importe banco/loja_turma.sql no phpMyAdmin
' ============================================================
Public cn As ADODB.Connection

' ---------- Abrir conexão (semana 3) ----------
Public Function Conectar() As Boolean
    On Error GoTo Falha
    Set cn = New ADODB.Connection
    cn.ConnectionString = "Driver={MySQL ODBC 8.0 ANSI Driver};" & _
                          "Server=localhost;Database=loja_turma;" & _
                          "Uid=root;Pwd=;"
    cn.Open
    Conectar = True
    Exit Function
Falha:
    MsgBox "Falha na conexão: " & Err.Description, vbCritical, "Conexão"
    Conectar = False
End Function

' ---------- Fechar conexão ----------
Public Sub Desconectar()
    On Error Resume Next
    If Not cn Is Nothing Then cn.Close
End Sub

' ---------- Consultar produtos (semana 6: SELECT) ----------
Public Function ListarProdutos() As ADODB.Recordset
    Set ListarProdutos = cn.Execute( _
        "SELECT id, nome, categoria, preco, estoque FROM produtos ORDER BY nome")
End Function

' ---------- Inserir produto (semana 5: INSERT) ----------
Public Sub InserirProduto(nome As String, categoria As String, _
                          preco As Single, estoque As Integer)
    cn.Execute "INSERT INTO produtos (nome, categoria, preco, estoque) " & _
               "VALUES ('" & Replace(nome, "'", "''") & "', '" & _
               Replace(categoria, "'", "''") & "', " & _
               Format(preco, "0.00") & ", " & estoque & ")"
End Sub

' ---------- Baixar estoque (semana 5: UPDATE) ----------
Public Sub BaixarEstoque(idProduto As Integer, qtd As Integer)
    cn.Execute "UPDATE produtos SET estoque = estoque - " & qtd & _
               " WHERE id = " & idProduto
End Sub

' ---------- Excluir produto (semana 5: DELETE com WHERE!) ----------
Public Sub ExcluirProduto(idProduto As Integer)
    cn.Execute "DELETE FROM produtos WHERE id = " & idProduto
End Sub

' ---------- Consulta com filtro (String + montagem de SQL, semana 11) ----------
Public Function BuscarPorNome(parte As String) As ADODB.Recordset
    Dim filtro As String
    filtro = Replace(Trim(parte), "'", "''")          'escapar aspas
    Set BuscarPorNome = cn.Execute( _
        "SELECT id, nome, preco, estoque FROM produtos " & _
        "WHERE nome LIKE '%" & filtro & "%' ORDER BY nome")
End Function

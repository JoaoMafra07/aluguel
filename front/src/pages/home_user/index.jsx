import React, { useEffect, useState } from 'react'
import axios from 'axios'

export default function HomeUser() {
    const [usuariosGerais, setUsuariosGerais] = useState([])
    const [usuariosFiltrados, setUsuariosFiltrados] = useState([])
    const [password, setPassword] = useState('')
    const [filtro, setFiltro] = useState('')
    const [nome, setNome] = useState('')
    const [tipo, setTipo] = useState('')

    const token = localStorage.getItem('token')

    const buscarTodos = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/usuarios', {
                headers: { Authorization: `Bearer ${token}` },
            })
            setUsuariosGerais(response.data)
        } catch (error) {
            console.log(error);
        }
    }

    const filtrar = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/usuarios', {
                headers: { Authorization: `Bearer ${token}` },
                params: {
                    nome: nome,
                    tipo: tipo
                }
            })
            setUsuariosFiltrados(response.data)
        } catch (error) {
            console.log(error);
        }
    }

    useEffect(() => { buscarTodos() }, [])

    return (
        <div style={{
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'center',
            alignItems: 'center',
            minHeight: '100vh',
            width: '100%'
        }}>
            <h2>Lista de Usuários</h2>

            {/*Tabela principal */}
            <table border='1' cellPadding='6' style={{ width: '100%' }}>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Nome</th>
                        <th>Email</th>
                        <th>Telefone</th>
                        <th>Tipo</th>
                    </tr>
                </thead>
                <tbody>
                    {usuariosGerais.map((u) => (
                        <tr key={u.id}>
                            <td>{u.id}</td>
                            <td>{u.nome}</td>
                            <td>{u.email}</td>
                            <td>{u.telefone}</td>
                            <td>{u.tipo}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
            <hr style={{ margin: '20px 0' }} />

            <div style={{ marginBottom: '20px' }}>
                <select
                    value={filtro}
                    onChange={(e) => {
                        setFiltro(e.target.value);
                        setNome('');
                        setTipo('');
                        setUsuariosFiltrados([]);
                    }}
                    style={{ marginRight: '10px', padding: '5px', fontWeight: 'bold' }}
                >
                    <option value=''>Nenhum</option>
                    <option value='nome'>Filtrar por Nome</option>
                    <option value='tipo'>Filtrar por Tipo</option>
                </select>

                {filtro === 'nome' && (
                    <input
                        type='text'
                        placeholder='Digite o nome'
                        value={nome}
                        onChange={(e) => setNome(e.target.value)}
                        style={{ marginRight: '10px', padding: '5px' }}
                    />
                )}

                {filtro === 'tipo' && (
                    <select
                        value={tipo}
                        onChange={(e) => setTipo(e.target.value)}
                        style={{ marginRight: '10px', padding: '5px', fontWeight: 'bold' }}
                    >
                        <option value=''>Nenhum</option>
                        <option value='LOCADOR'>Locador</option>
                        <option value='LOCATARIO'>Locatário</option>
                    </select>
                )}

                <button onClick={filtrar} style={{ padding: '5px 15px' }}>
                    Pesquisar
                </button>
            </div>

            <table border='1' cellPadding='6' style={{ width: '100%' }}>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Nome</th>
                        <th>Email</th>
                        <th>Telefone</th>
                        <th>Tipo</th>
                    </tr>
                </thead>
                <tbody>
                    {usuariosFiltrados.map((u) => (
                        <tr key={u.id}>
                            <td>{u.id}</td>
                            <td>{u.nome}</td>
                            <td>{u.email}</td>
                            <td>{u.telefone}</td>
                            <td>{u.tipo}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
}
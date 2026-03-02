import React, { useEffect, useState } from 'react'
import axios from 'axios'

export default function ImovelUser() {
    const [imoveisGerais, setImoveisGerais] = useState([])
    const [imoveisFiltrados, setImoveisFiltrados] = useState([])
    const [password, setPassword] = useState('')
    const [filtro, setFiltro] = useState('')
    const [titulo, setTitulo] = useState('')
    const [status, setStatus] = useState('')
    const [tipo, setTipo] = useState('')
    const [valor, setValor] = useState('')
    const [valorMin, setValorMin] = useState('')
    const [valorMax, setValorMax] = useState('')
    const [locador, setLocador] = useState('')

    const token = localStorage.getItem('token')

    const buscarTodos = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/imoveis', {
                headers: { Authorization: `Bearer ${token}` },
            })
            setImoveisGerais(response.data)
        } catch (error) {
            console.log(error);
        }
    }

    const filtrar = async () => {
    try {
        const params = {};

        if (filtro === 'status') {
            params.status = status;
        } else if (filtro === 'tipo') {
            params.tipo = tipo;
        } else if (filtro === 'valor') {
            params.valor_min = valorMin;
            params.valor_max = valorMax;
        }

        const response = await axios.get('http://127.0.0.1:8000/api/imoveis', {
            headers: { Authorization: `Bearer ${token}` },
            params: params
        });
        setImoveisFiltrados(response.data);
    } catch (error) {
        console.log("Erro na filtragem de imóveis:", error);
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
            <h2>Lista de Imóveis</h2>

            {/*Tabela principal */}
            <table border='1' cellPadding='6' style={{ width: '100%' }}>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Titulo</th>
                        <th>Tipo</th>
                        <th>Valor</th>
                        <th>Status</th>
                        <th>Locador</th>
                    </tr>
                </thead>
                <tbody>
                    {imoveisGerais.map((u) => (
                        <tr key={u.id}>
                            <td>{u.id}</td>
                            <td>{u.titulo}</td>
                            <td>{u.tipo}</td>
                            <td>
                                {Number(u.valor_aluguel).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}
                            </td>
                            <td>{u.status}</td>
                            <td>{u.locador}</td>
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
                        setStatus('');
                        setValor('');
                        setTipo('');
                        setImoveisFiltrados([]);
                    }}
                    style={{ marginRight: '10px', padding: '5px', fontWeight: 'bold' }}
                >
                    <option value=''>Nenhum</option>
                    <option value='status'>Filtrar por Status</option>
                    <option value='tipo'>Filtrar por Tipo</option>
                    <option value='valor'>Filtrar por Valor</option>
                </select>
                
                {filtro === 'status' && (
                    <select
                        value={status}
                        onChange={(e) => setStatus(e.target.value)}
                        style={{ marginRight: '10px', padding: '5px', fontWeight: 'bold' }}
                    >
                        <option value=''>Nenhum</option>
                        <option value='DISPONIVEL'>Disponivel</option>
                        <option value='ALUGADO'>Alugado</option>
                    </select>
                )}

                {filtro === 'tipo' && (
                    <input
                        type='text'
                        placeholder='Digite o tipo'
                        value={tipo}
                        onChange={(e) => setTipo(e.target.value)}
                        style={{ marginRight: '10px', padding: '5px' }}
                    />
                )}

                {filtro === 'valor' && (
                    <>
                        <input
                            type='text'
                            placeholder='Digite o valor mínimo'
                            value={valorMin}
                            onChange={(e) => setValorMin(e.target.value)}
                            style={{ marginRight: '10px', padding: '5px' }}
                        />

                        <input
                            type='text'
                            placeholder='Digite o valor máximo'
                            value={valorMax}
                            onChange={(e) => setValorMax(e.target.value)}
                            style={{ marginRight: '10px', padding: '5px' }}
                        />
                    </>
                )}


                <button onClick={filtrar} style={{ padding: '5px 15px' }}>
                    Pesquisar
                </button>
            </div>

            <table border='1' cellPadding='6' style={{ width: '100%' }}>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Titulo</th>
                        <th>Tipo</th>
                        <th>Valor</th>
                        <th>Status</th>
                        <th>Locador</th>
                    </tr>
                </thead>
                <tbody>
                    {imoveisFiltrados.map((u) => (
                        <tr key={u.id}>
                            <td>{u.id}</td>
                            <td>{u.titulo}</td>
                            <td>{u.tipo}</td>
                            <td>
                                {Number(u.valor_aluguel).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}
                            </td>
                            <td>{u.status}</td>
                            <td>{u.locador}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
}
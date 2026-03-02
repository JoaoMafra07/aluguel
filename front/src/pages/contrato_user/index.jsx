import React, { useEffect, useState } from 'react'
import axios from 'axios'

export default function ContratoUser() {
    const [contratosGerais, setContratosGerais] = useState([])
    const [contratosFiltrados, setContratosFiltrados] = useState([])
    const [password, setPassword] = useState('')
    const [filtro, setFiltro] = useState('')
    const [data, setData] = useState('')
    const [dataInicio, setDataInicio] = useState('')
    const [dataFim, setDataFim] = useState('')
    const [valor, setValor] = useState('')
    const [valorMin, setValorMin] = useState('')
    const [valorMax, setValorMax] = useState('')
    const [imovel, setImovel] = useState('')
    const [locador, setLocador] = useState('')
    const [locatario, setLocatario] = useState('')

    const token = localStorage.getItem('token')

    const buscarTodos = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/contratos', {
                headers: { Authorization: `Bearer ${token}` },
            })
            setContratosGerais(response.data)
        } catch (error) {
            console.log(error);
        }
    }

    const filtrar = async () => {
    try {
        const params = {};

        if (filtro === 'data') {
            params.data_inicio = dataInicio;
            params.data_fim = dataFim;
        } 
        else if (filtro === 'valor') {
            params.valor_min = valorMin;
            params.valor_max = valorMax;
        }

        const response = await axios.get('http://127.0.0.1:8000/api/contratos', {
            headers: { Authorization: `Bearer ${token}` },
            params: params
        });
        setContratosFiltrados(response.data);
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
            <h2>Lista de Contratos</h2>

            {/*Tabela principal */}
            <table border='1' cellPadding='6' style={{ width: '100%' }}>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Data Início</th>
                        <th>Data Fim</th>
                        <th>Valor</th>
                        <th>Imovel</th>
                        <th>Locador</th>
                        <th>Locatário</th>
                    </tr>
                </thead>
                <tbody>
                    {contratosGerais.map((u) => (
                        <tr key={u.id}>
                            <td>{u.id}</td>
                            <td>{u.data_inicio}</td>
                            <td>{u.data_fim}</td>
                            <td>
                                {Number(u.valor).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}
                            </td>
                            <td>{u.imovel}</td>
                            <td>{u.locador}</td>
                            <td>{u.locatario}</td>
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
                        setDataInicio('');
                        setDataFim('');
                        setValorMin('');
                        setValorMax('');
                        setContratosFiltrados([]);
                    }}
                    style={{ marginRight: '10px', padding: '5px', fontWeight: 'bold' }}
                >
                    <option value=''>Nenhum</option>
                    <option value='data'>Filtrar por Data</option>
                    <option value='valor'>Filtrar por Valor</option>
                </select>

                {filtro === 'data' && (
                    <>
                        <input
                            type='date'
                            placeholder='Digite a data de início'
                            value={dataInicio}
                            onChange={(e) => setDataInicio(e.target.value)}
                            style={{ marginRight: '10px', padding: '5px' }}
                        />

                        <input
                            type='date'
                            placeholder='Digite a data de fim'
                            value={dataFim}
                            onChange={(e) => setDataFim(e.target.value)}
                            style={{ marginRight: '10px', padding: '5px' }}
                        />
                    </>
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
                        <th>Data Início</th>
                        <th>Data Fim</th>
                        <th>Valor</th>
                        <th>Imovel</th>
                        <th>Locador</th>
                        <th>Locatário</th>
                    </tr>
                </thead>
                <tbody>
                    {contratosFiltrados.map((u) => (
                        <tr key={u.id}>
                            <td>{u.id}</td>
                            <td>{u.data_inicio}</td>
                            <td>{u.data_fim}</td>
                            <td>
                                {Number(u.valor).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}
                            </td>
                            <td>{u.imovel}</td>
                            <td>{u.locador}</td>
                            <td>{u.locatario}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
}
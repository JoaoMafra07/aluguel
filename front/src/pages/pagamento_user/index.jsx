import React, { useEffect, useState } from 'react'
import axios from 'axios'

export default function PagamentoUser() {
    const [pagamentosGerais, setPagamentosGerais] = useState([])
    const [pagamentosFiltrados, setPagamentosFiltrados] = useState([])
    const [password, setPassword] = useState('')
    const [filtro, setFiltro] = useState('')
    const [data, setData] = useState('')
    const [dataMin, setDataMin] = useState('')
    const [dataMax, setDataMax] = useState('')
    const [valor, setValor] = useState('')
    const [status, setStatus] = useState('')
    const [contrato, setContrato] = useState('')

    const token = localStorage.getItem('token')

    const buscarTodos = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/pagamentos', {
                headers: { Authorization: `Bearer ${token}` },
            })
            setPagamentosGerais(response.data)
        } catch (error) {
            console.log(error);
        }
    }

    const filtrar = async () => {
        try {
            const params = {};

            if (filtro === 'data') {
                params.data_min = dataMin;
                params.data_max = dataMax;
            } else if (filtro === 'status') {
                if (status !== '') {
                    params.status = status;
                }
            } else if (filtro === 'contrato') {
                params.contrato = contrato;
            }

            const response = await axios.get('http://127.0.0.1:8000/api/pagamentos', {
                headers: { Authorization: `Bearer ${token}` },
                params: params
            });
            setPagamentosFiltrados(response.data);
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
            <h2>Lista de pagamentos</h2>

            {/*Tabela principal */}
            <table border='1' cellPadding='6' style={{ width: '100%' }}>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Data</th>
                        <th>Valor</th>
                        <th>Status</th>
                        <th>Contrato</th>
                    </tr>
                </thead>
                <tbody>
                    {pagamentosGerais.map((u) => (
                        <tr key={u.id}>
                            <td>{u.id}</td>
                            <td>{u.data_pagamento}</td>
                            <td>
                                {Number(u.valor).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}
                            </td>
                            <td>{u.status === 1 || u.status === true ? 'Pago' : 'Não Pago'}</td>
                            <td>{u.contrato}</td>
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
                        setDataMin('');
                        setDataMax('');
                        setStatus('');
                        setContrato('');
                        setPagamentosFiltrados([]);
                    }}
                    style={{ marginRight: '10px', padding: '5px', fontWeight: 'bold' }}
                >
                    <option value=''>Nenhum</option>
                    <option value='data'>Filtrar por Data</option>
                    <option value='status'>Filtrar por Status</option>
                    <option value='contrato'>Filtrar por Contrato</option>
                </select>

                {filtro === 'data' && (
                    <>
                        <input
                            type='date'
                            placeholder='Digite a data de início'
                            value={dataMin}
                            onChange={(e) => setDataMin(e.target.value)}
                            style={{ marginRight: '10px', padding: '5px' }}
                        />

                        <input
                            type='date'
                            placeholder='Digite a data de fim'
                            value={dataMax}
                            onChange={(e) => setDataMax(e.target.value)}
                            style={{ marginRight: '10px', padding: '5px' }}
                        />
                    </>
                )}

                {filtro === 'status' && (
                    <select
                        value={status}
                        onChange={(e) => setStatus(e.target.value)}
                        style={{ marginRight: '10px', padding: '5px', fontWeight: 'bold' }}
                    >
                        <option value=''>Nenhum</option>
                        <option value='true'>Pago</option>
                        <option value='false'>Não pago</option>
                    </select>
                )}

                {filtro === 'contrato' && (
                    <input
                        type='text'
                        placeholder='Digite o contrato'
                        value={contrato}
                        onChange={(e) => setContrato(e.target.value)}
                        style={{ marginRight: '10px', padding: '5px' }}
                    />
                )}

                <button onClick={filtrar} style={{ padding: '5px 15px' }}>
                    Pesquisar
                </button>
            </div>

            <table border='1' cellPadding='6' style={{ width: '100%' }}>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Data</th>
                        <th>Valor</th>
                        <th>Status</th>
                        <th>Contrato</th>
                    </tr>
                </thead>
                <tbody>
                    {pagamentosFiltrados.map((u) => (
                        <tr key={u.id}>
                            <td>{u.id}</td>
                            <td>{u.data_pagamento}</td>
                            <td>
                                {Number(u.valor).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}
                            </td>
                            <td>{u.status === 1 || u.status === true ? 'Pago' : 'Não Pago'}</td>
                            <td>{u.contrato}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
}